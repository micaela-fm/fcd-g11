from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from pathlib import Path


def train_decision_tree_classifier(X, y):
    decision_tree = tree.DecisionTreeClassifier()
    return decision_tree.fit(X, y)


def train_knn_classifier(X, y):
    knn = KNeighborsClassifier(n_neighbors=5)
    return knn.fit(X, y)


def train_svm_classifier(X, y):
    svm = SVC(kernel="rbf", random_state=0)
    return svm.fit(X, y)


def plot_decision_tree_classifier(decision_tree):
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

    output_dir = Path("output") / "ex3" / "figures"
    output_dir.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_dir / "decision_tree.svg", bbox_inches="tight")


