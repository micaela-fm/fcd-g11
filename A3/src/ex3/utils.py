import pandas as pd

def load_dataset_for_classification(dataset_name):
    """Load and prepare a classification dataset.

    Returns: X, y, feature_names, class_names
    """
    if dataset_name == "diabetes":
        df = pd.read_csv("data/processed/diabetes.csv", sep=",")
        target_col = "Outcome"
    elif dataset_name == "iris":
        df = pd.read_csv("data/processed/iris.csv", sep=",")
        target_col = "class"
    elif dataset_name == "winequality":
        df = pd.read_csv("data/processed/winequality-white.csv", sep=";")
        target_col = "quality"
    elif dataset_name == "zoo":
        df = pd.read_csv("data/processed/zoo.csv")
        df = df.drop(columns="animal_name")
        target_col = "class"
    else:
        raise ValueError(f"Unknown dataset: {dataset_name}")

    y = df[target_col]
    X = df.drop(columns=target_col)

    return X, y, X.columns.tolist(), sorted(y.unique().tolist())


