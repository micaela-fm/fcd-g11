from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import matplotlib.pyplot as plt

from A3.src.utils.paths import get_a3_root


def create_decision_tree_classifier():
    """Create a decision tree classifier."""
    return DecisionTreeClassifier(criterion="entropy", random_state=0)


def create_knn_classifier():
    """Create a kNN classifier pipeline with feature scaling."""
    return Pipeline(
        [
            ("scaler", StandardScaler()),
            ("classifier", KNeighborsClassifier(n_neighbors=5, metric="euclidean")),
        ]
    )


def create_svm_classifier():
    """Create an SVM classifier pipeline with feature scaling."""
    return Pipeline(
        [
            ("scaler", StandardScaler()),
            ("classifier", SVC()),
        ]
    )


def plot_decision_tree_classifier(decision_tree):
    """Save the trained decision tree as an SVG figure."""
    depth = decision_tree.tree_.max_depth
    leaves = decision_tree.tree_.n_leaves
    figure_width = max(24, min(2.5 * leaves, 220))
    figure_height = max(10, min(2.2 * depth, 90))
    font_size = max(4, min(9, 18 / (depth + 1)))

    figure, axis = plt.subplots(figsize=(figure_width, figure_height), dpi=120)
    tree.plot_tree(
        decision_tree,
        ax=axis,
        filled=True,
        rounded=True,
        fontsize=font_size,
        impurity=False,
        proportion=True,
        precision=2,
    )
    figure.tight_layout()

    output_dir = get_a3_root() / "output" / "ex3" / "figures"
    output_dir.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_dir / "decision_tree.svg", bbox_inches="tight")
    plt.close(figure)
