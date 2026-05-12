import numpy as np


def ensure_parent_dir(path):
    """Create the parent directory for a file path."""
    path.parent.mkdir(parents=True, exist_ok=True)


def escape_latex(text):
    """Escape special LaTeX characters in text."""
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    escaped = str(text)
    for old, new in replacements.items():
        escaped = escaped.replace(old, new)
    return escaped


def format_latex_cell(value, float_format="%.4f"):
    """Format one table cell for LaTeX output."""
    if isinstance(value, (float, np.floating)):
        return float_format % value
    return escape_latex(value)


def dataframe_to_latex(dataframe, index=False, float_format="%.4f"):
    """Convert a dataframe to a simple LaTeX tabular."""
    latex_dataframe = dataframe.copy()

    if index:
        index_name = latex_dataframe.index.name or "index"
        latex_dataframe.insert(0, index_name, latex_dataframe.index)

    columns = [escape_latex(column) for column in latex_dataframe.columns]
    column_spec = "l" * len(columns)
    lines = [
        rf"\begin{{tabular}}{{{column_spec}}}",
        r"\hline",
        " & ".join(columns) + r" \\",
        r"\hline",
    ]

    for _, row in latex_dataframe.iterrows():
        cells = [
            format_latex_cell(value, float_format=float_format)
            for value in row.tolist()
        ]
        lines.append(" & ".join(cells) + r" \\")

    lines.extend([r"\hline", r"\end{tabular}"])
    return "\n".join(lines)


def wrap_latex_table(tabular_body, caption, label):
    """Wrap a LaTeX tabular in a table environment."""
    return "\n".join(
        [
            r"\begin{table}[htbp]",
            r"\centering",
            tabular_body,
            rf"\caption{{{escape_latex(caption)}}}",
            rf"\label{{{escape_latex(label)}}}",
            r"\end{table}",
        ]
    )


def save_dataframe_as_csv_and_latex(
    dataframe,
    csv_path,
    tex_path,
    caption,
    label,
    index=False,
):
    """Save a dataframe as CSV and LaTeX table."""
    ensure_parent_dir(csv_path)
    ensure_parent_dir(tex_path)

    dataframe.to_csv(csv_path, index=index)
    tex_text = wrap_latex_table(
        dataframe_to_latex(dataframe, index=index),
        caption,
        label,
    )
    tex_path.write_text(tex_text, encoding="utf-8")

    return csv_path, tex_path


def print_dataframe_summary(title, dataframe):
    """Print a short dataframe summary to the console."""
    print()
    print(title)
    print(dataframe.to_string(index=False))
