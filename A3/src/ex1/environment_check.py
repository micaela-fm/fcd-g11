import importlib
import sys

import pandas as pd

from A3.src.utils.paths import get_a3_root, relative_to_project
from A3.src.utils.tables import (
    print_dataframe_summary,
    save_dataframe_as_csv_and_latex,
)


PACKAGES = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn"]


def get_package_version(package_name):
    """Return the installed package version."""
    try:
        package = importlib.import_module(package_name)
        return getattr(package, "__version__", "versão não disponível")
    except ImportError:
        return "não instalado"


def build_versions_table():
    """Build the Python environment versions table."""
    rows = [{"component": "python", "version": sys.version.split()[0]}]

    for package_name in PACKAGES:
        rows.append(
            {
                "component": package_name,
                "version": get_package_version(package_name),
            }
        )

    return pd.DataFrame(rows)


def save_versions_table(versions_dataframe):
    """Save the versions table as CSV and LaTeX."""
    output_dir = get_a3_root() / "output" / "ex1" / "tables"
    csv_path = output_dir / "environment_versions.csv"
    tex_path = output_dir / "environment_versions.tex"

    return save_dataframe_as_csv_and_latex(
        versions_dataframe,
        csv_path,
        tex_path,
        "Versões do ambiente Python utilizado no módulo A.3",
        "tab:environment-versions",
    )


def main():
    """Run the Python environment check."""
    versions_dataframe = build_versions_table()
    csv_path, tex_path = save_versions_table(versions_dataframe)

    print_dataframe_summary("Versões do ambiente Python", versions_dataframe)
    print()
    print(f"CSV guardado em: {relative_to_project(csv_path)}")
    print(f"LaTeX guardado em: {relative_to_project(tex_path)}")


if __name__ == "__main__":
    main()
