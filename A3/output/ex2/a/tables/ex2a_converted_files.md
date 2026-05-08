# Ficheiros convertidos - Exercício 2(a)

| dataset_name | source_file | original_format | converted_file | converted_format | n_instances | n_columns |
| --- | --- | --- | --- | --- | --- | --- |
| Diabetes | A3/data/raw/diabetes/diabetes.csv | csv | A3/output/ex2/a/converted/diabetes/diabetes.json | json | 768 | 9 |
| Iris | A3/data/raw/iris/iris.data | data | A3/output/ex2/a/converted/iris/iris.json | json | 150 | 5 |
| Iris | A3/data/raw/iris/iris.data | data | A3/output/ex2/a/converted/iris/iris.csv | csv | 150 | 5 |
| Forest Fires | A3/data/raw/forest+fires/forestfires.csv | csv | A3/output/ex2/a/converted/forest_fires/forest_fires.json | json | 517 | 13 |

## Nota metodológica

* Os datasets foram carregados com pandas a partir dos ficheiros originais em A3/data/raw.
* A conversão principal foi feita para JSON.
* O dataset Iris foi também exportado para CSV porque o ficheiro original `.data` não contém cabeçalho explícito.
* Os ficheiros originais não foram alterados.
