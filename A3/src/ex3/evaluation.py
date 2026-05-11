from sklearn.model_selection import cross_validate, cross_val_predict, StratifiedKFold
from sklearn.metrics import confusion_matrix, classification_report, make_scorer, precision_score, recall_score, f1_score


def evaluate_classifier_cv(clf, X, y, n_splits=10, random_state=0):
    """Evaluate a classifier using 10-fold stratified CV.

    Returns: dict with metrics and confusion matrix
    """
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)

    scoring = {
        "accuracy": "accuracy",
        "precision": make_scorer(precision_score, average="weighted", zero_division=0),
        "recall": make_scorer(recall_score, average="weighted", zero_division=0),
        "f1": make_scorer(f1_score, average="weighted", zero_division=0),
    }

    cv_results = cross_validate(clf, X, y, cv=cv, scoring=scoring)
    y_pred = cross_val_predict(clf, X, y, cv=cv)
    labels = sorted(y.unique().tolist())
    cm = confusion_matrix(y, y_pred, labels=labels)

    return {
        "accuracy_scores": cv_results["test_accuracy"],
        "accuracy_mean": cv_results["test_accuracy"].mean(),
        "accuracy_std": cv_results["test_accuracy"].std(),
        "precision_scores": cv_results["test_precision"],
        "precision_mean": cv_results["test_precision"].mean(),
        "precision_std": cv_results["test_precision"].std(),
        "recall_scores": cv_results["test_recall"],
        "recall_mean": cv_results["test_recall"].mean(),
        "recall_std": cv_results["test_recall"].std(),
        "f1_scores": cv_results["test_f1"],
        "f1_mean": cv_results["test_f1"].mean(),
        "f1_std": cv_results["test_f1"].std(),
        "confusion_matrix": cm,
        "labels": labels,
        "classification_report": classification_report(y, y_pred, zero_division=0),
        "classification_report_dict": classification_report(y, y_pred, output_dict=True, zero_division=0),
    }
