from A3.src.ex2.utils.datasets import (
    get_dataset_configs,
    load_dataset,
    relative_to_project,
)


def print_dataset_summary(dataset_config, dataframe):
    total_values = dataframe.size
    missing_values = int(dataframe.isna().sum().sum())
    missing_percentage = (missing_values / total_values) * 100 if total_values else 0

    print("=" * 80)
    print(f"Dataset: {dataset_config['dataset_name']}")
    print(f"Dataset id: {dataset_config['dataset_id']}")
    if dataset_config["dataset_id"] == "wine_quality_white":
        print("Usage note: dataset reservado para classificação no Exercício 3.")
    print(f"Path: {relative_to_project(dataset_config['source_file'])}")
    print(f"Shape: {dataframe.shape}")
    print("\nFirst 5 rows:")
    print(dataframe.head())
    print("\nColumns:")
    print(list(dataframe.columns))
    print("\nData types:")
    print(dataframe.dtypes)
    print("\nMissing values by column:")
    print(dataframe.isna().sum())
    print(f"\nTotal missing values percentage: {missing_percentage:.2f}%")
    print()


def main():
    for dataset_config in get_dataset_configs():
        dataframe = load_dataset(dataset_config)
        print_dataset_summary(dataset_config, dataframe)


if __name__ == "__main__":
    main()
