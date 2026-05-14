def dataframe_to_markdown(dataframe):
    """Convert a dataframe to a Markdown table."""
    columns = list(dataframe.columns)
    rows = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]

    for _, row in dataframe.iterrows():
        values = [str(row[column]) for column in columns]
        rows.append("| " + " | ".join(values) + " |")

    return "\n".join(rows)


def ensure_parent_dir(path):
    """Create the parent directory for an output path."""
    path.parent.mkdir(parents=True, exist_ok=True)


def save_dataframe_as_csv_and_markdown(
    dataframe,
    csv_path,
    markdown_path,
    title,
    note="",
):
    """Save a dataframe as CSV and Markdown files."""
    ensure_parent_dir(csv_path)
    ensure_parent_dir(markdown_path)

    dataframe.to_csv(csv_path, index=False)

    markdown_text = f"# {title}\n\n{dataframe_to_markdown(dataframe)}\n"
    if note:
        markdown_text += note

    markdown_path.write_text(markdown_text, encoding="utf-8")

    return csv_path, markdown_path
