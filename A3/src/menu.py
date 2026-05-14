from A3.src.ex1 import environment_check
from A3.src.ex2.a import dataset_conversion, dataset_inventory, dataset_summary
from A3.src.ex2.b import iris_visualization
from A3.src.ex3 import main as ex3_main
from A3.src.utils.paths import get_a3_root, relative_to_project


EX3_DATASETS = ["diabetes", "iris", "winequality", "zoo"]
EX3_CLASSIFIERS = ["Decision_Tree", "kNN", "SVM"]

BASE_EXPECTED_OUTPUTS = [
    "output/ex1/tables/environment_versions.csv",
    "output/ex1/tables/environment_versions.tex",
    "output/ex2/a/tables/ex2a_dataset_summary.csv",
    "output/ex2/a/tables/ex2a_dataset_summary.tex",
    "output/ex2/a/tables/ex2a_converted_files.csv",
    "output/ex2/a/tables/ex2a_converted_files.tex",
    "output/ex2/a/converted/diabetes/diabetes.json",
    "output/ex2/a/converted/iris/iris.json",
    "output/ex2/a/converted/iris/iris.csv",
    "output/ex2/a/converted/forest_fires/forest_fires.json",
    "output/ex2/b/figures/2b_Iris_PetalLength_PetalWidth.png",
    "output/ex2/b/figures/2b_Iris_SepalLength_SepalWidth.png",
    "output/ex2/b/figures/2b_Iris_SepalLength_PetalLength.png",
    "output/ex2/b/figures/2b_Iris_ClassDistribution.png",
    "output/ex2/b/tables/2b_iris_class_distribution.csv",
    "output/ex2/b/tables/2b_iris_class_distribution.tex",
    "output/ex2/b/tables/2b_iris_scatter_plot_index.csv",
    "output/ex2/b/tables/2b_iris_scatter_plot_index.tex",
    "output/ex3/figures/decision_tree.svg",
    "output/ex3/tables/evaluation_summary.csv",
    "output/ex3/tables/evaluation_summary.tex",
    "output/ex3/tables/best_classifiers.csv",
    "output/ex3/tables/best_classifiers.tex",
    "output/ex3/tables/diabetes_classification_report.csv",
    "output/ex3/tables/diabetes_classification_report.tex",
    "output/ex3/tables/iris_classification_report.csv",
    "output/ex3/tables/iris_classification_report.tex",
    "output/ex3/tables/winequality_classification_report.csv",
    "output/ex3/tables/winequality_classification_report.tex",
    "output/ex3/tables/zoo_classification_report.csv",
    "output/ex3/tables/zoo_classification_report.tex",
]


def get_expected_outputs():
    """Return the list of expected A.3 output files."""
    expected_outputs = list(BASE_EXPECTED_OUTPUTS)

    for dataset_name in EX3_DATASETS:
        for classifier_name in EX3_CLASSIFIERS:
            expected_outputs.append(
                f"output/ex3/tables/{dataset_name}_{classifier_name}_confusion_matrix.csv"
            )
            expected_outputs.append(
                f"output/ex3/tables/{dataset_name}_{classifier_name}_confusion_matrix.tex"
            )

    return expected_outputs


def print_menu():
    """Print the interactive execution menu."""
    print()
    print("FCD A.3 - Menu de execução")
    print()
    print("1 - Verificar ambiente Python")
    print("2 - Exercício 2(a): inventário dos datasets")
    print("3 - Exercício 2(a): tabela de caracterização")
    print("4 - Exercício 2(a): conversão entre formatos")
    print("5 - Exercício 2(b): visualização do Iris")
    print("6 - Exercício 3: classificação e avaliação")
    print("7 - Correr tudo")
    print("8 - Verificar ficheiros de output esperados")
    print("0 - Sair")


def run_task(task_name, task_function):
    """Run one menu task and report its status."""
    print()
    print(f"=== {task_name} ===")
    try:
        task_function()
    except Exception as error:
        print(f"Erro ao executar '{task_name}': {error}")
        return False

    print("Tarefa concluída.")
    return True


def run_all():
    """Run all A.3 tasks in sequence."""
    tasks = [
        ("Verificar ambiente Python", environment_check.main),
        ("Exercício 2(a): inventário dos datasets", dataset_inventory.main),
        ("Exercício 2(a): tabela de caracterização", dataset_summary.main),
        ("Exercício 2(a): conversão entre formatos", dataset_conversion.main),
        ("Exercício 2(b): visualização do Iris", iris_visualization.main),
        ("Exercício 3: classificação e avaliação", ex3_main.main),
    ]

    for task_name, task_function in tasks:
        if not run_task(task_name, task_function):
            print("Execução interrompida devido a erro.")
            return


def check_expected_outputs():
    """Check whether the expected output files exist."""
    print()
    print("=== Verificação dos outputs esperados ===")
    a3_root = get_a3_root()

    for relative_path in get_expected_outputs():
        output_path = a3_root / relative_path
        status = "[OK]" if output_path.exists() else "[FALTA]"
        print(f"{status} {relative_to_project(output_path)}")


def handle_option(option):
    """Handle one user menu option."""
    if option == "1":
        run_task("Verificar ambiente Python", environment_check.main)
    elif option == "2":
        run_task("Exercício 2(a): inventário dos datasets", dataset_inventory.main)
    elif option == "3":
        run_task("Exercício 2(a): tabela de caracterização", dataset_summary.main)
    elif option == "4":
        run_task("Exercício 2(a): conversão entre formatos", dataset_conversion.main)
    elif option == "5":
        run_task("Exercício 2(b): visualização do Iris", iris_visualization.main)
    elif option == "6":
        run_task("Exercício 3: classificação e avaliação", ex3_main.main)
    elif option == "7":
        run_all()
    elif option == "8":
        check_expected_outputs()
    elif option == "0":
        return False
    else:
        print("Opção inválida.")

    return True


def main():
    """Run the interactive A.3 menu."""
    keep_running = True

    while keep_running:
        print_menu()
        option = input("Escolha uma opção: ").strip()
        keep_running = handle_option(option)

    print("A sair.")


if __name__ == "__main__":
    main()
