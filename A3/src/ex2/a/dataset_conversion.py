import pandas as pd

from A3.src.ex2.utils.datasets import (
    get_ex2a_dataset_configs,
    load_dataset,
)
from A3.src.utils.paths import get_a3_root
from A3.src.utils.tables import (
    ensure_parent_dir,
    print_dataframe_summary,
    save_dataframe_as_csv_and_latex,
)


CONVERTED_DIR = get_a3_root() / "output" / "ex2" / "a" / "converted"
TABLES_DIR = get_a3_root() / "output" / "ex2" / "a" / "tables"

METHODOLOGICAL_NOTE = [
    "Os datasets foram carregados com pandas a partir dos ficheiros originais.",
    "A conversão principal foi feita para JSON.",
    "O dataset Iris foi também exportado para CSV porque o ficheiro original .data não contém cabeçalho explícito.",
    "Os ficheiros originais não foram alterados.",
]


def get_file_format(path):
    """Return the file extension without dot."""
    return path.suffix.replace(".", "").lower()


def save_json(dataframe, output_path):
    """Save a dataframe as JSON records."""
    ensure_parent_dir(output_path)
    dataframe.to_json(output_path, orient="records", indent=2, force_ascii=False)


def save_csv(dataframe, output_path):
    """Save a dataframe as CSV."""
    ensure_parent_dir(output_path)
    dataframe.to_csv(output_path, index=False)


def add_conversion_row(rows, dataset_config, converted_file):
    """Add one conversion summary row."""
    rows.append(
        {
            "dataset_name": dataset_config["dataset_name"],
            "source_file": dataset_config["source_file"].name,
            "original_format": get_file_format(dataset_config["source_file"]),
            "converted_file": converted_file.name,
            "converted_format": get_file_format(converted_file),
        }
    )


def convert_dataset(dataset_config):
    """Convert one dataset to the selected output formats."""
    dataframe = load_dataset(dataset_config)
    dataset_output_dir = CONVERTED_DIR / dataset_config["dataset_id"]

    conversion_rows = []

    json_path = dataset_output_dir / f"{dataset_config['dataset_id']}.json"
    save_json(dataframe, json_path)
    add_conversion_row(conversion_rows, dataset_config, json_path)

    if dataset_config["dataset_id"] == "iris":
        csv_path = dataset_output_dir / "iris.csv"
        save_csv(dataframe, csv_path)
        add_conversion_row(conversion_rows, dataset_config, csv_path)

    return conversion_rows


def save_conversions_table(conversions_dataframe):
    """Save the conversion summary table as CSV and LaTeX."""
    csv_path = TABLES_DIR / "ex2a_converted_files.csv"
    tex_path = TABLES_DIR / "ex2a_converted_files.tex"

    return save_dataframe_as_csv_and_latex(
        conversions_dataframe,
        csv_path,
        tex_path,
        "Ficheiros convertidos - Exercício 2(a)",
        "tab:ex2a-converted-files",
    )


def main():
    """Convert Ex.2(a) datasets and save the conversion summary."""
    conversion_rows = []

    for dataset_config in get_ex2a_dataset_configs():
        conversion_rows.extend(convert_dataset(dataset_config))

    conversions_dataframe = pd.DataFrame(conversion_rows)
    csv_path, tex_path = save_conversions_table(conversions_dataframe)

    print_dataframe_summary("Ficheiros convertidos - Exercício 2(a)", conversions_dataframe)
    print()
    print("Nota metodológica:")
    for note in METHODOLOGICAL_NOTE:
        print(f"- {note}")
    print()
    print(f"CSV guardado em: {csv_path.name}")
    print(f"LaTeX guardado em: {tex_path.name}")


if __name__ == "__main__":
    main()
