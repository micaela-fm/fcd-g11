from A3.src.ex1 import environment_check
from A3.src.ex2.a import dataset_conversion, dataset_inventory, dataset_summary
from A3.src.ex2.b import iris_visualization
from A3.src.ex2.utils.datasets import get_a3_root, relative_to_project


EXPECTED_OUTPUTS = [
    "output/ex1/tables/environment_versions.csv",
    "output/ex1/tables/environment_versions.md",
    "output/ex2/a/tables/ex2a_dataset_summary.csv",
    "output/ex2/a/tables/ex2a_dataset_summary.md",
    "output/ex2/a/tables/ex2a_converted_files.csv",
    "output/ex2/a/tables/ex2a_converted_files.md",
    "output/ex2/a/converted/diabetes/diabetes.json",
    "output/ex2/a/converted/iris/iris.json",
    "output/ex2/a/converted/iris/iris.csv",
    "output/ex2/a/converted/forest_fires/forest_fires.json",
    "output/ex2/b/figures/2b_Iris_PetalLength_PetalWidth.png",
    "output/ex2/b/figures/2b_Iris_SepalLength_SepalWidth.png",
    "output/ex2/b/figures/2b_Iris_SepalLength_PetalLength.png",
    "output/ex2/b/figures/2b_Iris_ClassDistribution.png",
    "output/ex2/b/tables/2b_iris_class_distribution.csv",
    "output/ex2/b/tables/2b_iris_class_distribution.md",
]


def print_menu():
    print()
    print("FCD A.3 - Menu de execução")
    print()
    print("1 - Verificar ambiente Python")
    print("2 - Exercício 2(a): inventário dos datasets")
    print("3 - Exercício 2(a): tabela de caracterização")
    print("4 - Exercício 2(a): conversão entre formatos")
    print("5 - Exercício 2(b): visualização do Iris")
    print("6 - Correr tudo")
    print("7 - Verificar ficheiros de output esperados")
    print("0 - Sair")


def run_task(task_name, task_function):
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
    tasks = [
        ("Verificar ambiente Python", environment_check.main),
        ("Exercício 2(a): inventário dos datasets", dataset_inventory.main),
        ("Exercício 2(a): tabela de caracterização", dataset_summary.main),
        ("Exercício 2(a): conversão entre formatos", dataset_conversion.main),
        ("Exercício 2(b): visualização do Iris", iris_visualization.main),
    ]

    for task_name, task_function in tasks:
        if not run_task(task_name, task_function):
            print("Execução interrompida devido a erro.")
            return


def check_expected_outputs():
    print()
    print("=== Verificação dos outputs esperados ===")
    a3_root = get_a3_root()

    for relative_path in EXPECTED_OUTPUTS:
        output_path = a3_root / relative_path
        status = "[OK]" if output_path.exists() else "[FALTA]"
        print(f"{status} {relative_to_project(output_path)}")


def handle_option(option):
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
        run_all()
    elif option == "7":
        check_expected_outputs()
    elif option == "0":
        return False
    else:
        print("Opção inválida.")

    return True


def main():
    keep_running = True

    while keep_running:
        print_menu()
        option = input("Escolha uma opção: ").strip()
        keep_running = handle_option(option)

    print("A sair.")


if __name__ == "__main__":
    main()
