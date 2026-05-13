import pandas as pd
import numpy as np

from A3.src.utils.paths import get_a3_root, relative_to_project
from A3.src.ex3.classification import (
    create_decision_tree_classifier,
    create_knn_classifier,
    create_svm_classifier,
    plot_decision_tree_classifier,
)
from A3.src.ex3.evaluation import evaluate_classifier_cv
from A3.src.ex3.utils import load_dataset_for_classification


DATASETS = ["diabetes", "iris", "winequality", "zoo"]
CLASSIFIERS = {
    "Decision Tree": create_decision_tree_classifier,
    "kNN": create_knn_classifier,
    "SVM": create_svm_classifier,
}


def escape_latex(text):
    """Escape text for LaTeX output."""
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
    """Format one dataframe cell for LaTeX output."""
    if isinstance(value, (float, np.floating)):
        return float_format % value
    return escape_latex(value)


def dataframe_to_latex(dataframe, index=False, float_format="%.4f"):
    """Convert a dataframe to a LaTeX tabular body."""
    latex_df = dataframe.copy()

    if index:
        index_name = latex_df.index.name or "class"
        latex_df = latex_df.copy()
        latex_df.insert(0, index_name, latex_df.index)

    columns = [escape_latex(column) for column in latex_df.columns]
    column_spec = "l" * len(columns)
    lines = [
        rf"\begin{{tabular}}{{{column_spec}}}",
        r"\hline",
        " & ".join(columns) + r" \\",
        r"\hline",
    ]

    for _, row in latex_df.iterrows():
        cells = [format_latex_cell(value, float_format=float_format) for value in row.tolist()]
        lines.append(" & ".join(cells) + r" \\")

    lines.extend([r"\hline", r"\end{tabular}"])
    return "\n".join(lines)


def wrap_latex_table(tabular_body, caption, label):
    """Wrap a LaTeX tabular body in a table environment."""
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


def dataset_report_to_latex(dataset_name, report_rows):
    """Build one weighted-avg classification report table per dataset."""
    report_df = pd.DataFrame(report_rows)
    return wrap_latex_table(
        dataframe_to_latex(report_df, index=False),
        f"Relatório de classificação (weighted avg) - {dataset_name}",
        f"tab:ex3-{dataset_name}-classification-report",
    )


def save_results_to_csv(all_results):
    """Save evaluation results as CSV and LaTeX tables."""
    output_dir = get_a3_root() / "output" / "ex3" / "tables"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Summary table: mean metrics for each (dataset, classifier) pair
    summary_rows = []
    for dataset_name in DATASETS:
        for clf_name in CLASSIFIERS.keys():
            results = all_results.get((dataset_name, clf_name))
            if results:
                summary_rows.append({
                    "dataset": dataset_name,
                    "classifier": clf_name,
                    "accuracy_mean": results["accuracy_mean"],
                    "accuracy_std": results["accuracy_std"],
                    "precision_mean": results["precision_mean"],
                    "precision_std": results["precision_std"],
                    "recall_mean": results["recall_mean"],
                    "recall_std": results["recall_std"],
                    "f1_mean": results["f1_mean"],
                    "f1_std": results["f1_std"],
                })

    summary_df = pd.DataFrame(summary_rows)
    summary_csv = output_dir / "evaluation_summary.csv"
    summary_df.to_csv(summary_csv, index=False)
    print(f"\nSummary saved to: {relative_to_project(summary_csv)}")

    summary_tex = output_dir / "evaluation_summary.tex"
    summary_tex.write_text(
        wrap_latex_table(
            dataframe_to_latex(summary_df, index=False),
            "Resumo dos resultados da validação cruzada (10-fold)",
            "tab:ex3-summary",
        ),
        encoding="utf-8",
    )

    best_rows = []
    for dataset_name in DATASETS:
        dataset_rows = summary_df[summary_df["dataset"] == dataset_name]
        if not dataset_rows.empty:
            best_row = dataset_rows.sort_values(by=["accuracy_mean", "f1_mean"], ascending=False).iloc[0]
            best_rows.append({
                "dataset": best_row["dataset"],
                "best_classifier": best_row["classifier"],
                "accuracy_mean": best_row["accuracy_mean"],
                "f1_mean": best_row["f1_mean"],
            })

    best_df = pd.DataFrame(best_rows)
    best_csv = output_dir / "best_classifiers.csv"
    best_df.to_csv(best_csv, index=False)
    best_tex = output_dir / "best_classifiers.tex"
    best_tex.write_text(
        wrap_latex_table(
            dataframe_to_latex(best_df, index=False),
            "Melhor classificador por conjunto de dados",
            "tab:ex3-best-classifiers",
        ),
        encoding="utf-8",
    )

    # Detailed results: confusion matrices and one report per dataset
    dataset_report_rows = {dataset_name: [] for dataset_name in DATASETS}

    for (dataset_name, clf_name), results in all_results.items():
        cm_df = pd.DataFrame(results["confusion_matrix"], index=results["labels"], columns=results["labels"])
        cm_csv = output_dir / f"{dataset_name}_{clf_name.replace(' ', '_')}_confusion_matrix.csv"
        cm_df.to_csv(cm_csv, index=False, header=False)

        cm_tex = output_dir / f"{dataset_name}_{clf_name.replace(' ', '_')}_confusion_matrix.tex"
        cm_tex.write_text(
            wrap_latex_table(
                dataframe_to_latex(cm_df, index=True),
                f"Matriz de confusão - {dataset_name} / {clf_name}",
                f"tab:ex3-{dataset_name}-{clf_name.replace(' ', '-').lower()}-cm",
            ),
            encoding="utf-8",
        )

        weighted_avg = results["classification_report_dict"]["weighted avg"]
        dataset_report_rows[dataset_name].append(
            {
                "classifier": clf_name,
                "accuracy": results["classification_report_dict"]["accuracy"],
                "precision": weighted_avg["precision"],
                "recall": weighted_avg["recall"],
                "f1-score": weighted_avg["f1-score"],
                "support": weighted_avg["support"],
            }
        )

    for dataset_name, rows in dataset_report_rows.items():
        report_df = pd.DataFrame(rows)
        report_csv = output_dir / f"{dataset_name}_classification_report.csv"
        report_df.to_csv(report_csv, index=False)

        report_tex = output_dir / f"{dataset_name}_classification_report.tex"
        report_tex.write_text(
            dataset_report_to_latex(dataset_name, rows),
            encoding="utf-8",
        )


def main():
    """Run the Ex.3 classification workflow."""
    all_results = {}

    print("=" * 80)
    print("10-Fold Cross-Validation Classification Evaluation")
    print("=" * 80)

    for dataset_name in DATASETS:
        print(f"\n{'='*80}")
        print(f"Dataset: {dataset_name.upper()}")
        print(f"{'='*80}")

        X, y, feature_names, class_names = load_dataset_for_classification(dataset_name)
        print(f"Features: {len(feature_names)}, Samples: {len(X)}, Classes: {len(class_names)}")
        print(f"Class distribution: {dict(y.value_counts())}")

        for clf_name, create_classifier in CLASSIFIERS.items():
            print(f"\n  {clf_name}:")
            clf = create_classifier()
            results = evaluate_classifier_cv(clf, X, y)
            all_results[(dataset_name, clf_name)] = results

            print(f"    Accuracy:  {results['accuracy_mean']:.4f} ± {results['accuracy_std']:.4f}")
            print(f"    Precision: {results['precision_mean']:.4f} ± {results['precision_std']:.4f}")
            print(f"    Recall:    {results['recall_mean']:.4f} ± {results['recall_std']:.4f}")
            print(f"    F1-Score:  {results['f1_mean']:.4f} ± {results['f1_std']:.4f}")
            print(f"    Confusion Matrix:\n{results['confusion_matrix']}")

    # Save all results to files
    save_results_to_csv(all_results)

    # Train and plot final DT model on full diabetes dataset
    print(f"\n{'='*80}")
    print("Training final Decision Tree on full Diabetes dataset for visualization")
    print(f"{'='*80}")
    X_diabetes, y_diabetes, _, _ = load_dataset_for_classification("diabetes")
    dt_final = create_decision_tree_classifier()
    dt_final.fit(X_diabetes, y_diabetes)
    plot_decision_tree_classifier(dt_final)


if __name__ == "__main__":
    main()
