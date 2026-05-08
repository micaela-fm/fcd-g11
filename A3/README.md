# FCD Fundamentos de Ciência de Dados - A.3

## Datasets

* [Pima Indians Diabetes](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
* [Iris](https://archive.ics.uci.edu/dataset/53/iris)
* [Wine quality - white](https://archive.ics.uci.edu/dataset/186/wine+quality)
* [Forest fires](https://archive.ics.uci.edu/dataset/162/forest+fires)

Seleção final por exercício:

* Exercício 2(a): Diabetes, Iris e Forest Fires.
* Exercício 2(b): Iris.
* Exercício 3: Diabetes, Iris, Wine Quality - White e Forest Fires com alvo binário derivado de `area`.

## Estrutura do A.3

* `data/raw` contém os dados originais.
* `src/ex1` contém o script de verificação do ambiente do Exercício 1.
* `src/ex2/a` contém os scripts do Exercício 2(a).
* `src/ex2/b` contém os scripts do Exercício 2(b).
* `src/ex2/utils` contém código comum aos scripts do Exercício 2.
* `output/ex1` contém as tabelas geradas no Exercício 1.
* `output/ex2/a` contém tabelas e ficheiros convertidos do Exercício 2(a).
* `output/ex2/b` contém figuras do Exercício 2(b).
* `report` será usado para o relatório.
* `_local_references` contém anexos locais ignorados pelo Git e não faz parte da entrega.

## Exercício 1 - Ambiente

Executar:

```bash
source /home/tiago-nevoa/.virtualenvs/fcd-g11/bin/activate
python -m A3.src.ex1.environment_check
```

Ficheiros gerados:

* `A3/output/ex1/tables/environment_versions.csv`
* `A3/output/ex1/tables/environment_versions.md`

## Exercício 2(a) - Caracterização dos datasets

A tabela do Exercício 2(a) caracteriza apenas Diabetes, Iris e Forest Fires. O dataset Wine Quality - White fica reservado para reutilização posterior no Exercício 3.

Executar:

```bash
source /home/tiago-nevoa/.virtualenvs/fcd-g11/bin/activate
python -m A3.src.ex2.a.dataset_inventory
python -m A3.src.ex2.a.dataset_summary
python -m A3.src.ex2.a.dataset_conversion
```

Ficheiros gerados:

* `A3/output/ex2/a/tables/ex2a_dataset_summary.csv`
* `A3/output/ex2/a/tables/ex2a_dataset_summary.md`
* `A3/output/ex2/a/tables/ex2a_converted_files.csv`
* `A3/output/ex2/a/tables/ex2a_converted_files.md`
* `A3/output/ex2/a/converted/`

## Exercício 2(b) - Visualização do Iris

Este exercício gera três scatter-plots individuais, um gráfico de barras e uma tabela com a distribuição das classes.

Executar:

```bash
source /home/tiago-nevoa/.virtualenvs/fcd-g11/bin/activate
python -m A3.src.ex2.b.iris_visualization
```

Ficheiros gerados:

* `A3/output/ex2/b/figures/2b_Iris_PetalLength_PetalWidth.png`
* `A3/output/ex2/b/figures/2b_Iris_SepalLength_SepalWidth.png`
* `A3/output/ex2/b/figures/2b_Iris_SepalLength_PetalLength.png`
* `A3/output/ex2/b/figures/2b_Iris_ClassDistribution.png`
* `A3/output/ex2/b/tables/2b_iris_class_distribution.csv`
* `A3/output/ex2/b/tables/2b_iris_class_distribution.md`

Para adaptar este script a outro dataset, configurar no início de `iris_visualization.py` os valores `DATASET_ID`, `SCATTER_PAIRS` e `OUTPUT_PREFIX`. O dataset também deve estar registado em `A3/src/ex2/utils/datasets.py`.
