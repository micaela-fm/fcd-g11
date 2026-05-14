import pandas as pd

from A3.src.ex2.utils.datasets import (
    get_ex2a_dataset_configs,
    get_dataset_profile,
    load_dataset,
)
from A3.src.utils.paths import get_a3_root, relative_to_project
from A3.src.utils.tables import (
    print_dataframe_summary,
    save_dataframe_as_csv_and_latex,
)


OUTPUT_TABLES_DIR = get_a3_root() / "output" / "ex2" / "a" / "tables"

METHODOLOGICAL_NOTE = [
    "A tabela corresponde aos três datasets escolhidos para o Exercício 2(a).",
    "A contagem de features exclui a variável target.",
    "A percentagem de missing values considera apenas valores formalmente ausentes.",
    "No dataset Diabetes, o ficheiro pima-diabetes.csv já representa alguns "
    "valores clínicos ausentes como campos vazios, que foram contabilizados como missing values.",
    "O dataset Forest Fires é identificado como regressão porque o target area é numérico contínuo.",
    "O dataset Wine Quality - White será usado posteriormente no Exercício 3, "
    "mas não integra a tabela do Exercício 2(a).",
]


def summarize_dataset(dataset_config):
    """Build one dataset characterization row."""
    dataframe = load_dataset(dataset_config)
    dataset_profile = get_dataset_profile(dataframe, dataset_config)
    target_column = dataset_config["target_column"]

    return {
        "dataset_name": dataset_config["dataset_name"],
        "source_file": dataset_profile["source_file_name"],
        "source_url": dataset_config["source_url"],
        "n_instances": dataset_profile["n_instances"],
        "n_columns_total": dataset_profile["n_columns_total"],
        "target_column": target_column,
        "n_predictive_features": dataset_profile["n_predictive_features"],
        "n_numeric_features": dataset_profile["n_numeric_features"],
        "n_categorical_features": dataset_profile["n_categorical_features"],
        "missing_values_total": dataset_profile["missing_values_total"],
        "missing_values_percentage": dataset_profile["missing_values_percentage"],
        "task_type": dataset_config["task_type"],
        "target_unique_values": dataset_profile["target_unique_values"],
    }


def save_summary(summary_dataframe):
    """Save the dataset summary table as CSV and LaTeX."""
    csv_path = OUTPUT_TABLES_DIR / "ex2a_dataset_summary.csv"
    tex_path = OUTPUT_TABLES_DIR / "ex2a_dataset_summary.tex"

    return save_dataframe_as_csv_and_latex(
        summary_dataframe,
        csv_path,
        tex_path,
        "Caracterização dos datasets - Exercício 2(a)",
        "tab:ex2a-dataset-summary",
    )


def main():
    """Generate the Ex.2(a) dataset characterization table."""
    summary_rows = [
        summarize_dataset(dataset_config)
        for dataset_config in get_ex2a_dataset_configs()
    ]
    summary_dataframe = pd.DataFrame(summary_rows)
    csv_path, tex_path = save_summary(summary_dataframe)

    print_dataframe_summary("Caracterização dos datasets - Exercício 2(a)", summary_dataframe)
    print()
    print("Nota metodológica:")
    for note in METHODOLOGICAL_NOTE:
        print(f"- {note}")
    print()
    print(f"CSV guardado em: {relative_to_project(csv_path)}")
    print(f"LaTeX guardado em: {relative_to_project(tex_path)}")


if __name__ == "__main__":
    main()
