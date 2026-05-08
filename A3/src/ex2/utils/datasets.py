from pathlib import Path

import pandas as pd
from pandas.api.types import is_numeric_dtype


def get_project_root():
    return Path(__file__).resolve().parents[4]


def get_a3_root():
    return get_project_root() / "A3"


def relative_to_project(path):
    return Path(path).relative_to(get_project_root()).as_posix()


def get_dataset_configs():
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
            "source_file": a3_root / "data" / "raw" / "diabetes" / "diabetes.csv",
            "source_url": "https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database",
            "target_column": "Outcome",
            "task_type": "classificação binária",
            "read_options": {},
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
    ex2a_dataset_ids = {"diabetes", "iris", "forest_fires"}
    return [
        dataset_config
        for dataset_config in get_dataset_configs()
        if dataset_config["dataset_id"] in ex2a_dataset_ids
    ]


def load_dataset(dataset_config):
    return pd.read_csv(
        dataset_config["source_file"],
        **dataset_config.get("read_options", {}),
    )


def count_feature_types(dataframe, target_column):
    feature_columns = [column for column in dataframe.columns if column != target_column]
    numeric_features = sum(is_numeric_dtype(dataframe[column]) for column in feature_columns)
    categorical_features = len(feature_columns) - numeric_features

    return len(feature_columns), numeric_features, categorical_features
