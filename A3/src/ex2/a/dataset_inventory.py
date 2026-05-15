from A3.src.ex2.utils.datasets import (
    get_dataset_configs,
    load_dataset,
)
from A3.src.utils.paths import relative_to_project


def print_dataset_summary(dataset_config, dataframe):
    """Print a dataset inventory summary."""
    target_column = dataset_config["target_column"]
    feature_columns = [column for column in dataframe.columns if column != target_column]
    total_feature_values = len(dataframe) * len(feature_columns)
    missing_values = int(dataframe[feature_columns].isna().sum().sum())
    missing_percentage = (
        (missing_values / total_feature_values) * 100 if total_feature_values else 0
    )

    print("=" * 80)
    print(f"Dataset: {dataset_config['dataset_name']}")
    print(f"Dataset id: {dataset_config['dataset_id']}")
    print(f"Path: {relative_to_project(dataset_config['source_file'])}")
    print(f"Shape: {dataframe.shape}")
    print("\nFirst 5 rows:")
    print(dataframe.head())
    print("\nColumns:")
    print(list(dataframe.columns))
    print("\nData types:")
    print(dataframe.dtypes)
    print("\nMissing values by predictive column:")
    print(dataframe[feature_columns].isna().sum())
    print(f"\nPredictive missing values percentage: {missing_percentage:.2f}%")
    print()


def main():
    """Print the inventory for all configured datasets."""
    for dataset_config in get_dataset_configs():
        dataframe = load_dataset(dataset_config)
        print_dataset_summary(dataset_config, dataframe)


if __name__ == "__main__":
    main()
