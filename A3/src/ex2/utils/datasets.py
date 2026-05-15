import pandas as pd
from pandas.api.types import is_numeric_dtype

from A3.src.utils import paths as project_paths


def get_project_root():
    """Return the repository root path."""
    return project_paths.get_project_root()


def get_a3_root():
    """Return the A3 project root path."""
    return project_paths.get_a3_root()


def relative_to_project(path):
    """Return a path relative to the repository root."""
    return project_paths.relative_to_project(path)


def get_dataset_configs():
    """Return static dataset metadata."""
    a3_root = get_a3_root()
    iris_columns = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "class",
    ]

    return [
        {
            "dataset_id": "diabetes",
            "dataset_name": "Diabetes",
            "source_file": a3_root / "data" / "raw" / "diabetes" / "pima-diabetes.csv",
            "source_url": "https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database",
            "target_column": "Outcome",
            "task_type": "classificação binária",
            "read_options": {"skiprows": [1, 2]},
        },
        {
            "dataset_id": "iris",
            "dataset_name": "Iris",
            "source_file": a3_root / "data" / "raw" / "iris" / "iris.data",
            "source_url": "https://archive.ics.uci.edu/dataset/53/iris",
            "target_column": "class",
            "task_type": "classificação multiclasse",
            "read_options": {"header": None, "names": iris_columns},
        },
        {
            "dataset_id": "wine_quality_white",
            "dataset_name": "Wine Quality - White",
            "source_file": a3_root
            / "data"
            / "raw"
            / "wine+quality"
            / "winequality-white.csv",
            "source_url": "https://archive.ics.uci.edu/dataset/186/wine+quality",
            "target_column": "quality",
            "task_type": "classificação ordinal/multiclasse",
            "read_options": {"sep": ";"},
        },
        {
            "dataset_id": "forest_fires",
            "dataset_name": "Forest Fires",
            "source_file": a3_root
            / "data"
            / "raw"
            / "forest+fires"
            / "forestfires.csv",
            "source_url": "https://archive.ics.uci.edu/dataset/162/forest+fires",
            "target_column": "area",
            "task_type": "regressão",
            "read_options": {},
        },
    ]


def get_ex2a_dataset_configs():
    """Return the datasets selected for Ex.2(a)."""
    ex2a_dataset_ids = {"diabetes", "iris", "forest_fires"}
    return [
        dataset_config
        for dataset_config in get_dataset_configs()
        if dataset_config["dataset_id"] in ex2a_dataset_ids
    ]


def get_dataset_config_by_id(dataset_id):
    """Return one dataset metadata config by id."""
    for dataset_config in get_dataset_configs():
        if dataset_config["dataset_id"] == dataset_id:
            return dataset_config

    raise ValueError(f"Dataset não configurado: {dataset_id}")


def load_dataset(dataset_config):
    """Load a dataset using its metadata config."""
    return pd.read_csv(
        dataset_config["source_file"],
        **dataset_config.get("read_options", {}),
    )


def count_feature_types(dataframe, target_column):
    """Count feature types excluding the target column."""
    feature_columns = [column for column in dataframe.columns if column != target_column]
    numeric_features = sum(is_numeric_dtype(dataframe[column]) for column in feature_columns)
    categorical_features = len(feature_columns) - numeric_features

    return len(feature_columns), numeric_features, categorical_features


def get_file_format(path):
    """Return the file extension without dot."""
    return path.suffix.replace(".", "").lower()


def get_dataset_profile(dataframe, dataset_config):
    """Infer dataset profile values from a loaded dataframe."""
    target_column = dataset_config["target_column"]
    feature_columns = [column for column in dataframe.columns if column != target_column]
    total_feature_values = len(dataframe) * len(feature_columns)
    missing_values_total = int(dataframe[feature_columns].isna().sum().sum())
    missing_values_percentage = (
        (missing_values_total / total_feature_values) * 100
        if total_feature_values
        else 0
    )
    n_features, n_numeric_features, n_categorical_features = count_feature_types(
        dataframe,
        target_column,
    )

    return {
        "source_file_name": dataset_config["source_file"].name,
        "source_format": get_file_format(dataset_config["source_file"]),
        "n_instances": len(dataframe),
        "n_columns_total": len(dataframe.columns),
        "n_predictive_features": n_features,
        "n_numeric_features": n_numeric_features,
        "n_categorical_features": n_categorical_features,
        "missing_values_total": missing_values_total,
        "missing_values_percentage": round(missing_values_percentage, 2),
        "target_unique_values": int(dataframe[target_column].nunique(dropna=True)),
    }
