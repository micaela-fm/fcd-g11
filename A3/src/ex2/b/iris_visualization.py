import pandas as pd

from A3.src.ex2.utils.datasets import (
    get_dataset_config_by_id,
    load_dataset,
)
from A3.src.ex2.utils.visualization import (
    create_class_distribution_plot,
    create_scatter_plots,
    get_class_distribution,
)
from A3.src.utils.paths import get_a3_root
from A3.src.utils.tables import (
    print_dataframe_summary,
    save_dataframe_as_csv_and_latex,
)


FIGURES_DIR = get_a3_root() / "output" / "ex2" / "b" / "figures"
TABLES_DIR = get_a3_root() / "output" / "ex2" / "b" / "tables"

DATASET_ID = "iris"
OUTPUT_PREFIX = "2b_Iris"
TABLE_PREFIX = OUTPUT_PREFIX.lower()

SCATTER_PAIRS = [
    ("petal_length", "petal_width", "PetalLength_PetalWidth"),
    ("sepal_length", "sepal_width", "SepalLength_SepalWidth"),
    ("sepal_length", "petal_length", "SepalLength_PetalLength"),
]

CLASS_COLORS = {
    "Iris-setosa": "tab:blue",
    "Iris-versicolor": "tab:orange",
    "Iris-virginica": "tab:green",
}


def load_visualization_dataset(dataset_id):
    """Load the dataset selected for visualization."""
    dataset_config = get_dataset_config_by_id(dataset_id)
    dataframe = load_dataset(dataset_config)
    target_column = dataset_config["target_column"]
    dataset_name = dataset_config["dataset_name"]

    return dataframe, target_column, dataset_name


def build_scatter_plot_index(dataset_name, target_column):
    """Build the scatter plot index table."""
    rows = []
    for x_column, y_column, file_suffix in SCATTER_PAIRS:
        rows.append(
            {
                "plot_file": f"{OUTPUT_PREFIX}_{file_suffix}.png",
                "dataset_name": dataset_name,
                "variable_x": x_column,
                "variable_y": y_column,
                "target_column": target_column,
            }
        )

    return pd.DataFrame(rows)


def save_class_distribution_table(class_distribution, dataset_name):
    """Save the class distribution table as CSV and LaTeX."""
    csv_path = TABLES_DIR / f"{TABLE_PREFIX}_class_distribution.csv"
    tex_path = TABLES_DIR / f"{TABLE_PREFIX}_class_distribution.tex"

    return save_dataframe_as_csv_and_latex(
        class_distribution,
        csv_path,
        tex_path,
        f"Distribuição das classes {dataset_name} - Exercício 2(b)",
        "tab:ex2b-iris-class-distribution",
    )


def save_scatter_plot_index_table(scatter_plot_index):
    """Save the scatter plot index table as CSV and LaTeX."""
    csv_path = TABLES_DIR / f"{TABLE_PREFIX}_scatter_plot_index.csv"
    tex_path = TABLES_DIR / f"{TABLE_PREFIX}_scatter_plot_index.tex"

    return save_dataframe_as_csv_and_latex(
        scatter_plot_index,
        csv_path,
        tex_path,
        "Índice dos scatter plots do Iris - Exercício 2(b)",
        "tab:ex2b-iris-scatter-plot-index",
    )


def main():
    """Generate the Iris visualizations for Ex.2(b)."""
    dataframe, target_column, dataset_name = load_visualization_dataset(DATASET_ID)
    class_distribution = get_class_distribution(dataframe, target_column)
    scatter_plot_index = build_scatter_plot_index(dataset_name, target_column)

    scatter_paths = create_scatter_plots(
        dataframe,
        target_column,
        dataset_name,
        SCATTER_PAIRS,
        FIGURES_DIR,
        OUTPUT_PREFIX,
        CLASS_COLORS,
    )
    bar_path = create_class_distribution_plot(
        class_distribution,
        target_column,
        dataset_name,
        FIGURES_DIR / f"{OUTPUT_PREFIX}_ClassDistribution.png",
        CLASS_COLORS,
    )
    distribution_csv_path, distribution_tex_path = save_class_distribution_table(
        class_distribution,
        dataset_name,
    )
    index_csv_path, index_tex_path = save_scatter_plot_index_table(scatter_plot_index)

    print_dataframe_summary("Distribuição das classes - Iris", class_distribution)
    print_dataframe_summary("Índice dos scatter plots - Iris", scatter_plot_index)
    print()
    for scatter_path in scatter_paths:
        print(f"Scatter plot guardado em: {scatter_path.name}")
    print(f"Gráfico de barras guardado em: {bar_path.name}")
    print(f"CSV distribuição guardado em: {distribution_csv_path.name}")
    print(f"LaTeX distribuição guardado em: {distribution_tex_path.name}")
    print(f"CSV índice guardado em: {index_csv_path.name}")
    print(f"LaTeX índice guardado em: {index_tex_path.name}")


if __name__ == "__main__":
    main()
