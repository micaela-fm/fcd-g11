import pandas as pd

from A3.src.ex2.utils.datasets import (
    count_feature_types,
    get_a3_root,
    get_ex2a_dataset_configs,
    load_dataset,
    relative_to_project,
)
from A3.src.ex2.utils.output import save_dataframe_as_csv_and_markdown


OUTPUT_TABLES_DIR = get_a3_root() / "output" / "ex2" / "a" / "tables"

METHODOLOGICAL_NOTE = """
## Nota metodológica

* A tabela corresponde aos três conjuntos de dados escolhidos para o Exercício 2(a).
* A contagem de características exclui a variável alvo.
* A percentagem de valores omissos considera apenas valores formalmente ausentes.
* No dataset Diabetes existem valores zero em atributos clínicos que podem ser interpretados como valores inválidos/suspeitos, mas não foram tratados como omissos nesta caracterização inicial.
* O dataset Forest Fires é identificado como regressão porque a variável alvo `area` é numérica contínua.
* O dataset Wine Quality - White será usado posteriormente no Exercício 3, mas não integra a tabela do Exercício 2(a).
"""


def summarize_dataset(dataset_config):
    dataframe = load_dataset(dataset_config)
    target_column = dataset_config["target_column"]
    missing_values_total = int(dataframe.isna().sum().sum())
    total_values = dataframe.size
    missing_values_percentage = (
        (missing_values_total / total_values) * 100 if total_values else 0
    )
    n_features, n_numeric_features, n_categorical_features = count_feature_types(
        dataframe, target_column
    )

    return {
        "dataset_name": dataset_config["dataset_name"],
        "source_file": relative_to_project(dataset_config["source_file"]),
        "source_url": dataset_config["source_url"],
        "n_instances": len(dataframe),
        "n_columns_total": len(dataframe.columns),
        "target_column": target_column,
        "n_predictive_features": n_features,
        "n_numeric_features": n_numeric_features,
        "n_categorical_features": n_categorical_features,
        "missing_values_total": missing_values_total,
        "missing_values_percentage": round(missing_values_percentage, 2),
        "task_type": dataset_config["task_type"],
        "target_unique_values": int(dataframe[target_column].nunique(dropna=True)),
    }


def save_summary(summary_dataframe):
    csv_path = OUTPUT_TABLES_DIR / "ex2a_dataset_summary.csv"
    markdown_path = OUTPUT_TABLES_DIR / "ex2a_dataset_summary.md"

    return save_dataframe_as_csv_and_markdown(
        summary_dataframe,
        csv_path,
        markdown_path,
        "Caracterização dos datasets - Exercício 2(a)",
        METHODOLOGICAL_NOTE,
    )


def main():
    summary_rows = [
        summarize_dataset(dataset_config)
        for dataset_config in get_ex2a_dataset_configs()
    ]
    summary_dataframe = pd.DataFrame(summary_rows)
    csv_path, markdown_path = save_summary(summary_dataframe)

    print(summary_dataframe.to_string(index=False))
    print()
    print(f"CSV guardado em: {relative_to_project(csv_path)}")
    print(f"Markdown guardado em: {relative_to_project(markdown_path)}")


if __name__ == "__main__":
    main()
