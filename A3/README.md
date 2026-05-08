# fcd-g11

## Datasets

* [Pima Indians Diabetes](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
* [Iris](https://archive.ics.uci.edu/dataset/53/iris)
* [Wine quality - red](https://archive.ics.uci.edu/dataset/186/wine+quality)
* [Wine quality - white](https://archive.ics.uci.edu/dataset/186/wine+quality)
* [Forest fires](https://archive.ics.uci.edu/dataset/162/forest+fires)

## Estrutura do A.3

* `data/raw` contém os dados originais.
* `src/ex2/a` contém os scripts do Exercício 2(a).
* `src/ex2/b` contém os scripts do Exercício 2(b).
* `src/ex2/utils` contém código comum aos scripts do Exercício 2.
* `output/ex2/a` contém tabelas e ficheiros convertidos do Exercício 2(a).
* `output/ex2/b` contém figuras do Exercício 2(b).
* `report` será usado para o relatório.
* `_local_references` contém anexos locais ignorados pelo Git e não faz parte da entrega.

## Exercício 2(a) - Caracterização dos datasets

Executar:

```bash
python3 -m A3.src.ex2.a.dataset_inventory
python3 -m A3.src.ex2.a.dataset_summary
```

Ficheiros gerados:

* `A3/output/ex2/a/tables/ex2a_dataset_summary.csv`
* `A3/output/ex2/a/tables/ex2a_dataset_summary.md`
 
