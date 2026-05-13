import matplotlib.pyplot as plt

from A3.src.utils.tables import ensure_parent_dir


def get_class_color(class_name, color_index, class_colors=None):
    """Return a plot color for one class."""
    if class_colors and class_name in class_colors:
        return class_colors[class_name]

    default_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    return default_colors[color_index % len(default_colors)]


def plot_scatter_by_class(
    dataframe,
    target_column,
    dataset_name,
    x_column,
    y_column,
    output_path,
    class_colors=None,
):
    """Save one scatter plot colored by class."""
    ensure_parent_dir(output_path)
    figure, axis = plt.subplots(figsize=(7, 5))

    class_names = sorted(dataframe[target_column].unique())
    for color_index, class_name in enumerate(class_names):
        class_rows = dataframe[dataframe[target_column] == class_name]
        axis.scatter(
            class_rows[x_column],
            class_rows[y_column],
            label=class_name,
            color=get_class_color(class_name, color_index, class_colors),
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


def create_scatter_plots(
    dataframe,
    target_column,
    dataset_name,
    scatter_pairs,
    figures_dir,
    output_prefix,
    class_colors=None,
):
    """Create scatter plots for the selected variable pairs."""
    output_paths = []

    for x_column, y_column, file_suffix in scatter_pairs:
        output_path = figures_dir / f"{output_prefix}_{file_suffix}.png"
        plot_scatter_by_class(
            dataframe,
            target_column,
            dataset_name,
            x_column,
            y_column,
            output_path,
            class_colors,
        )
        output_paths.append(output_path)

    return output_paths


def get_class_distribution(dataframe, target_column):
    """Count instances by class."""
    class_counts = dataframe[target_column].value_counts().sort_index()
    return class_counts.rename_axis(target_column).reset_index(name="n_instances")


def create_class_distribution_plot(
    class_distribution,
    target_column,
    dataset_name,
    output_path,
    class_colors=None,
):
    """Save a class distribution bar chart."""
    ensure_parent_dir(output_path)
    figure, axis = plt.subplots(figsize=(7, 4.5))

    class_names = list(class_distribution[target_column])
    axis.bar(
        class_names,
        class_distribution["n_instances"],
        color=[
            get_class_color(class_name, color_index, class_colors)
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
