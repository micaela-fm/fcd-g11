# FCD - Fundamentos de Ciência de Dados - A.3

## 1. Datasets

Datasets usados no Projeto A.3:

* [Pima Indians Diabetes](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
* [Iris](https://archive.ics.uci.edu/dataset/53/iris)
* [Wine Quality - White](https://archive.ics.uci.edu/dataset/186/wine+quality)
* [Forest Fires](https://archive.ics.uci.edu/dataset/162/forest+fires)
* [Zoo](https://archive.ics.uci.edu/dataset/111/zoo)

Seleção final por exercício:

* Exercício 2(a): Diabetes, Iris e Forest Fires.
* Exercício 2(b): Iris.
* Exercício 3: Diabetes, Iris, Wine Quality - White e Zoo.

## 2. Estrutura do projeto

* `data/raw` contém os dados originais.
* `data/processed` contém versões preparadas em CSV dos datasets usados no Exercício 3.
* `src/ex1` contém o script de verificação do ambiente.
* `src/ex2/a` contém os scripts de caracterização e conversão dos datasets.
* `src/ex2/b` contém o script de visualização do Iris.
* `src/ex2/utils` contém código comum aos scripts do Exercício 2.
* `src/ex3` contém os scripts de classificação e avaliação.
* `src/utils` contém utilitários comuns de paths e tabelas.
* `output` contém os resultados gerados pelos scripts.
* `report` será usado para o relatório.
* `_local_references` contém anexos locais ignorados pelo Git e não faz parte da entrega.

## 3. Preparação do ambiente

A partir da raiz do repositório:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r A3/requirements.txt
```

Dependências principais:

* numpy
* pandas
* matplotlib
* seaborn
* scikit-learn

## 4. Execução

Com o ambiente virtual ativo, o projeto pode ser executado de duas formas:

### Opção A — executar pela raiz do repositório

```bash
python -m A3.src.menu
```

### Opção B — executar a partir da pasta `A3`

Criar primeiro a configuração local:

```bash
cp A3/config/local.properties.example A3/config/local.properties
```

Editar `A3/config/local.properties`:

```text
repo_root=<caminho-para-o-repositorio>
venv_path=<caminho-para-o-virtualenv>
```

Depois executar:

```bash
cd A3
bash scripts/run_menu.sh
```

O menu permite:

* correr cada exercício individualmente;
* correr todos os exercícios;
* verificar se os outputs esperados existem.

## 5. Exercício 1 - Ambiente

Script principal:

```bash
python -m A3.src.ex1.environment_check
```

Objetivo:

* verificar a versão do Python;
* verificar as bibliotecas principais;
* gerar tabela de versões do ambiente.

Outputs principais:

* `output/ex1/tables/environment_versions.csv`
* `output/ex1/tables/environment_versions.tex`

## 6. Exercício 2(a) - Caracterização e conversão

Scripts principais:

```bash
python -m A3.src.ex2.a.dataset_inventory
python -m A3.src.ex2.a.dataset_summary
python -m A3.src.ex2.a.dataset_conversion
```

Datasets usados:

* Diabetes
* Iris
* Forest Fires

Objetivo:

* caracterizar os datasets;
* identificar número de instâncias, colunas e features;
* distinguir features numéricas e categóricas;
* calcular valores omissos;
* identificar o tipo de problema;
* converter os datasets para outro formato.

Outputs principais:

* `output/ex2/a/tables/ex2a_dataset_summary.csv`
* `output/ex2/a/tables/ex2a_dataset_summary.tex`
* `output/ex2/a/tables/ex2a_converted_files.csv`
* `output/ex2/a/tables/ex2a_converted_files.tex`
* `output/ex2/a/converted/`

## 7. Exercício 2(b) - Visualização do Iris

Script principal:

```bash
python -m A3.src.ex2.b.iris_visualization
```

Dataset usado:

* Iris

Objetivo:

* gerar três scatter plots entre pares de variáveis;
* gerar um gráfico de barras com o número de instâncias por classe;
* gerar tabelas objetivas para apoiar o relatório.

Outputs principais:

* `output/ex2/b/figures/2b_Iris_PetalLength_PetalWidth.png`
* `output/ex2/b/figures/2b_Iris_SepalLength_SepalWidth.png`
* `output/ex2/b/figures/2b_Iris_SepalLength_PetalLength.png`
* `output/ex2/b/figures/2b_Iris_ClassDistribution.png`
* `output/ex2/b/tables/2b_iris_class_distribution.csv`
* `output/ex2/b/tables/2b_iris_class_distribution.tex`
* `output/ex2/b/tables/2b_iris_scatter_plot_index.csv`
* `output/ex2/b/tables/2b_iris_scatter_plot_index.tex`

A interpretação dos gráficos deve ser feita no relatório.

## 8. Exercício 3 - Classificação e avaliação

Script principal:

```bash
python -m A3.src.ex3.main
```

Datasets usados:

* Diabetes
* Iris
* Wine Quality - White
* Zoo

Classificadores avaliados:

* Decision Tree
* kNN
* SVM

Metodologia:

* validação cruzada estratificada 10-fold;
* matriz de confusão;
* accuracy;
* precision;
* recall;
* F1-score.

Decisões principais:

* kNN usa distância euclidiana.
* kNN usa standardização porque depende de distâncias entre instâncias.
* SVM usa a configuração padrão da biblioteca.
* Decision Tree usa `entropy` como critério de divisão.
* A standardização é aplicada dentro de um `Pipeline`, para que em cada fold seja aprendida apenas com os dados de treino e aplicada depois aos dados de teste.

Outputs principais:

* `output/ex3/tables/evaluation_summary.csv`
* `output/ex3/tables/evaluation_summary.tex`
* `output/ex3/tables/best_classifiers.csv`
* `output/ex3/tables/best_classifiers.tex`
* `output/ex3/tables/*_classification_report.csv`
* `output/ex3/tables/*_classification_report.tex`
* `output/ex3/tables/*_confusion_matrix.csv`
* `output/ex3/tables/*_confusion_matrix.tex`
* `output/ex3/figures/decision_tree.svg`

Melhores classificadores obtidos:

* Diabetes: SVM.
* Iris: SVM.
* Wine Quality - White: Decision Tree.
* Zoo: Decision Tree.

Nota: no Wine Quality - White e no Zoo podem surgir avisos quando uma classe tem menos exemplos do que os 10 folds usados na validação cruzada.
