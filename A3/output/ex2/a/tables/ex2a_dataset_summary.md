# Caracterização dos datasets - Exercício 2(a)

| dataset_name | source_file | source_url | n_instances | n_columns_total | target_column | n_predictive_features | n_numeric_features | n_categorical_features | missing_values_total | missing_values_percentage | task_type | target_unique_values |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Diabetes | A3/data/raw/diabetes/diabetes.csv | https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database | 768 | 9 | Outcome | 8 | 8 | 0 | 0 | 0.0 | classificação binária | 2 |
| Iris | A3/data/raw/iris/iris.data | https://archive.ics.uci.edu/dataset/53/iris | 150 | 5 | class | 4 | 4 | 0 | 0 | 0.0 | classificação multiclasse | 3 |
| Wine Quality - Red | A3/data/raw/wine+quality/winequality-red.csv | https://archive.ics.uci.edu/dataset/186/wine+quality | 1599 | 12 | quality | 11 | 11 | 0 | 0 | 0.0 | classificação ordinal/multiclasse | 6 |
| Wine Quality - White | A3/data/raw/wine+quality/winequality-white.csv | https://archive.ics.uci.edu/dataset/186/wine+quality | 4898 | 12 | quality | 11 | 11 | 0 | 0 | 0.0 | classificação ordinal/multiclasse | 7 |
| Forest Fires | A3/data/raw/forest+fires/forestfires.csv | https://archive.ics.uci.edu/dataset/162/forest+fires | 517 | 13 | area | 12 | 10 | 2 | 0 | 0.0 | regressão | 251 |

## Nota metodológica

* As características numéricas e categóricas foram contadas excluindo a variável alvo.
* A percentagem de valores omissos considera valores formalmente marcados como ausentes no ficheiro.
* No dataset Diabetes existem valores zero em atributos clínicos que podem ser interpretados como valores inválidos/suspeitos, mas não foram tratados como omissos nesta caracterização inicial.
* O dataset Forest Fires é identificado como regressão porque a variável alvo `area` é numérica contínua.
