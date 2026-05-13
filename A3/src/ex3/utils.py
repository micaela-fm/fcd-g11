import pandas as pd

from A3.src.utils.paths import get_a3_root


DATASET_CONFIGS = {
    "diabetes": {
        "file_name": "diabetes.csv",
        "target_column": "Outcome",
        "read_options": {"sep": ","},
    },
    "iris": {
        "file_name": "iris.csv",
        "target_column": "class",
        "read_options": {"sep": ","},
    },
    "winequality": {
        "file_name": "winequality-white.csv",
        "target_column": "quality",
        "read_options": {"sep": ";"},
    },
    "zoo": {
        "file_name": "zoo.csv",
        "target_column": "class",
        "read_options": {},
        "drop_columns": ["animal_name"],
    },
}


def load_dataset_for_classification(dataset_name):
    """Load and prepare a classification dataset.

    Returns: X, y, feature_names, class_names
    """
    if dataset_name not in DATASET_CONFIGS:
        raise ValueError(f"Unknown dataset: {dataset_name}")

    processed_dir = get_a3_root() / "data" / "processed"
    dataset_config = DATASET_CONFIGS[dataset_name]

    df = pd.read_csv(
        processed_dir / dataset_config["file_name"],
        **dataset_config["read_options"],
    )
    df = df.drop(columns=dataset_config.get("drop_columns", []))

    target_column = dataset_config["target_column"]
    y = df[target_column]
    X = df.drop(columns=target_column)

    return X, y, X.columns.tolist(), sorted(y.unique().tolist())
