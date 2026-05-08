import pandas as pd

from A3.src.ex2.utils.datasets import (
    get_a3_root,
    get_ex2a_dataset_configs,
    load_dataset,
    relative_to_project,
)


CONVERTED_DIR = get_a3_root() / "output" / "ex2" / "a" / "converted"
TABLES_DIR = get_a3_root() / "output" / "ex2" / "a" / "tables"

METHODOLOGICAL_NOTE = """
## Nota metodológica

* Os datasets foram carregados com pandas a partir dos ficheiros originais em A3/data/raw.
* A conversão principal foi feita para JSON.
* O dataset Iris foi também exportado para CSV porque o ficheiro original `.data` não contém cabeçalho explícito.
* Os ficheiros originais não foram alterados.
"""


def dataframe_to_markdown(dataframe):
    columns = list(dataframe.columns)
    rows = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]

    for _, row in dataframe.iterrows():
        values = [str(row[column]) for column in columns]
        rows.append("| " + " | ".join(values) + " |")

    return "\n".join(rows)


def get_file_format(path):
    return path.suffix.replace(".", "").lower()


def save_json(dataframe, output_path):
    dataframe.to_json(output_path, orient="records", indent=2, force_ascii=False)


def save_csv(dataframe, output_path):
    dataframe.to_csv(output_path, index=False)


def add_conversion_row(rows, dataset_config, dataframe, converted_file):
    rows.append(
        {
            "dataset_name": dataset_config["dataset_name"],
            "source_file": relative_to_project(dataset_config["source_file"]),
            "original_format": get_file_format(dataset_config["source_file"]),
            "converted_file": relative_to_project(converted_file),
            "converted_format": get_file_format(converted_file),
            "n_instances": len(dataframe),
            "n_columns": len(dataframe.columns),
        }
    )


def convert_dataset(dataset_config):
    dataframe = load_dataset(dataset_config)
    dataset_output_dir = CONVERTED_DIR / dataset_config["dataset_id"]
    dataset_output_dir.mkdir(parents=True, exist_ok=True)

    conversion_rows = []

    json_path = dataset_output_dir / f"{dataset_config['dataset_id']}.json"
    save_json(dataframe, json_path)
    add_conversion_row(conversion_rows, dataset_config, dataframe, json_path)

    if dataset_config["dataset_id"] == "iris":
        csv_path = dataset_output_dir / "iris.csv"
        save_csv(dataframe, csv_path)
        add_conversion_row(conversion_rows, dataset_config, dataframe, csv_path)

    return conversion_rows


def save_conversions_table(conversions_dataframe):
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    csv_path = TABLES_DIR / "ex2a_converted_files.csv"
    markdown_path = TABLES_DIR / "ex2a_converted_files.md"

    conversions_dataframe.to_csv(csv_path, index=False)
    markdown_path.write_text(
        "# Ficheiros convertidos - Exercício 2(a)\n\n"
        f"{dataframe_to_markdown(conversions_dataframe)}\n"
        f"{METHODOLOGICAL_NOTE}",
        encoding="utf-8",
    )

    return csv_path, markdown_path


def main():
    conversion_rows = []

    for dataset_config in get_ex2a_dataset_configs():
        conversion_rows.extend(convert_dataset(dataset_config))

    conversions_dataframe = pd.DataFrame(conversion_rows)
    csv_path, markdown_path = save_conversions_table(conversions_dataframe)

    print(conversions_dataframe.to_string(index=False))
    print()
    print(f"CSV guardado em: {relative_to_project(csv_path)}")
    print(f"Markdown guardado em: {relative_to_project(markdown_path)}")


if __name__ == "__main__":
    main()
