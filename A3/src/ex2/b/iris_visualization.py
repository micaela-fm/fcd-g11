import matplotlib.pyplot as plt

from A3.src.ex2.utils.datasets import (
    get_a3_root,
    get_dataset_config_by_id,
    load_dataset,
    relative_to_project,
)
from A3.src.ex2.utils.output import save_dataframe_as_csv_and_markdown


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
    "Iris-setosa": "#1f77b4",
    "Iris-versicolor": "#ff7f0e",
    "Iris-virginica": "#2ca02c",
}


def load_visualization_dataset(dataset_id):
    dataset_config = get_dataset_config_by_id(dataset_id)
    dataframe = load_dataset(dataset_config)
    target_column = dataset_config["target_column"]
    dataset_name = dataset_config["dataset_name"]

    return dataframe, target_column, dataset_name


def get_class_color(class_name, color_index):
    if class_name in CLASS_COLORS:
        return CLASS_COLORS[class_name]

    default_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    return default_colors[color_index % len(default_colors)]


def plot_scatter_by_class(
    dataframe,
    target_column,
    dataset_name,
    x_column,
    y_column,
    output_path,
):
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots(figsize=(7, 5))

    class_names = sorted(dataframe[target_column].unique())
    for color_index, class_name in enumerate(class_names):
        class_rows = dataframe[dataframe[target_column] == class_name]
        axis.scatter(
            class_rows[x_column],
            class_rows[y_column],
            label=class_name,
            color=get_class_color(class_name, color_index),
            alpha=0.75,
            edgecolors="black",
            linewidths=0.3,
        )

    axis.set_title(f"{dataset_name} - {x_column} vs {y_column}")
    axis.set_xlabel(x_column)
    axis.set_ylabel(y_column)
    axis.grid(True, alpha=0.25)
    axis.legend(title=target_column)
    figure.tight_layout()

    figure.savefig(output_path, dpi=150)
    plt.close(figure)

    return output_path


def create_scatter_plots(dataframe, target_column, dataset_name):
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    output_paths = []

    for x_column, y_column, file_suffix in SCATTER_PAIRS:
        output_path = FIGURES_DIR / f"{OUTPUT_PREFIX}_{file_suffix}.png"
        plot_scatter_by_class(
            dataframe,
            target_column,
            dataset_name,
            x_column,
            y_column,
            output_path,
        )
        output_paths.append(output_path)

    old_output_path = FIGURES_DIR / f"{OUTPUT_PREFIX}_ScatterPlots.png"
    if old_output_path.exists():
        old_output_path.unlink()

    return output_paths


def get_class_distribution(dataframe, target_column):
    class_counts = dataframe[target_column].value_counts().sort_index()
    return class_counts.rename_axis(target_column).reset_index(name="n_instances")


def create_class_distribution_plot(
    class_distribution,
    target_column,
    dataset_name,
    output_path,
):
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots(figsize=(7, 4.5))

    class_names = list(class_distribution[target_column])
    axis.bar(
        class_names,
        class_distribution["n_instances"],
        color=[
            get_class_color(class_name, color_index)
            for color_index, class_name in enumerate(class_names)
        ],
        edgecolor="black",
        linewidth=0.5,
    )
    axis.set_title(f"{dataset_name} - número de instâncias por classe")
    axis.set_xlabel(target_column)
    axis.set_ylabel("número de instâncias")
    axis.grid(axis="y", alpha=0.25)

    figure.tight_layout()

    figure.savefig(output_path, dpi=150)
    plt.close(figure)

    return output_path


def save_class_distribution_table(class_distribution, dataset_name):
    csv_path = TABLES_DIR / f"{TABLE_PREFIX}_class_distribution.csv"
    markdown_path = TABLES_DIR / f"{TABLE_PREFIX}_class_distribution.md"

    return save_dataframe_as_csv_and_markdown(
        class_distribution,
        csv_path,
        markdown_path,
        f"Distribuição das classes {dataset_name} - Exercício 2(b)",
    )


def main():
    dataframe, target_column, dataset_name = load_visualization_dataset(DATASET_ID)
    class_distribution = get_class_distribution(dataframe, target_column)

    scatter_paths = create_scatter_plots(dataframe, target_column, dataset_name)
    bar_path = create_class_distribution_plot(
        class_distribution,
        target_column,
        dataset_name,
        FIGURES_DIR / f"{OUTPUT_PREFIX}_ClassDistribution.png",
    )
    csv_path, markdown_path = save_class_distribution_table(
        class_distribution,
        dataset_name,
    )

    print(class_distribution.to_string(index=False))
    print()
    for scatter_path in scatter_paths:
        print(f"Scatter-plot guardado em: {relative_to_project(scatter_path)}")
    print(f"Gráfico de barras guardado em: {relative_to_project(bar_path)}")
    print(f"CSV guardado em: {relative_to_project(csv_path)}")
    print(f"Markdown guardado em: {relative_to_project(markdown_path)}")


if __name__ == "__main__":
    main()
