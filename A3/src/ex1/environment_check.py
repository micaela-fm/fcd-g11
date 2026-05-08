import csv
import importlib
import sys
from pathlib import Path


PACKAGES = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn"]


def get_a3_root():
    return Path(__file__).resolve().parents[2]


def get_package_version(package_name):
    try:
        package = importlib.import_module(package_name)
        return getattr(package, "__version__", "versão não disponível")
    except ImportError:
        return "não instalado"


def rows_to_markdown(rows):
    columns = list(rows[0].keys())
    rows = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ] + [
        "| " + " | ".join(str(row[column]) for column in columns) + " |"
        for row in rows
    ]

    return "\n".join(rows)


def build_versions_table():
    rows = [{"package": "python", "version": sys.version.split()[0]}]

    for package_name in PACKAGES:
        rows.append(
            {
                "package": package_name,
                "version": get_package_version(package_name),
            }
        )

    return rows


def save_versions_table(version_rows):
    output_dir = get_a3_root() / "output" / "ex1" / "tables"
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = output_dir / "environment_versions.csv"
    markdown_path = output_dir / "environment_versions.md"

    with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["package", "version"])
        writer.writeheader()
        writer.writerows(version_rows)

    markdown_path.write_text(
        "# Versões do ambiente - Exercício 1\n\n"
        f"{rows_to_markdown(version_rows)}\n",
        encoding="utf-8",
    )

    return csv_path, markdown_path


def main():
    version_rows = build_versions_table()
    csv_path, markdown_path = save_versions_table(version_rows)

    for row in version_rows:
        print(f"{row['package']}: {row['version']}")
    print()
    print(f"CSV guardado em: {csv_path.relative_to(get_a3_root().parent)}")
    print(f"Markdown guardado em: {markdown_path.relative_to(get_a3_root().parent)}")


if __name__ == "__main__":
    main()
