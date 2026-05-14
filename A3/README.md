# FCD - Fundamentos de Ciências de Dados - A.3

## Datasets

* [Pima Indians Diabetes](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
* [Iris](https://archive.ics.uci.edu/dataset/53/iris)
* [Wine quality - white](https://archive.ics.uci.edu/dataset/186/wine+quality)
* [Forest fires](https://archive.ics.uci.edu/dataset/162/forest+fires)
* [Zoo](https://archive.ics.uci.edu/dataset/111/zoo)

Seleção final por exercício:

* Exercício 2(a): Diabetes, Iris e Forest Fires.
* Exercício 2(b): Iris.
* Exercício 3: Diabetes, Iris, Wine Quality - White e Zoo.

## Estrutura do A.3

* `data/raw` contém os dados originais.
* `src/ex1` contém o script de verificação do ambiente do Exercício 1.
* `src/ex2/a` contém os scripts do Exercício 2(a).
* `src/ex2/b` contém os scripts do Exercício 2(b).
* `src/ex2/utils` contém código comum aos scripts do Exercício 2.
* `output/ex1` contém as tabelas geradas no Exercício 1.
* `output/ex2/a` contém tabelas e ficheiros convertidos do Exercício 2(a).
* `output/ex2/b` contém figuras e tabelas geradas no Exercício 2(b).
* `output/ex3` contém métricas, matrizes de confusão, tabelas LaTeX e figuras do Exercício 3.
* `report` será usado para o relatório.
* `_local_references` contém anexos locais ignorados pelo Git e não faz parte da entrega.

## Execução dos scripts

Todos os comandos devem ser executados a partir da raiz do repositório, não dentro da pasta `A3/`.

Nos exemplos abaixo:

* `<repo-root>` representa a pasta raiz do projeto `fcd-g11`;
* `<path-to-venv>` representa o caminho para o ambiente virtual Python;
* depois de ativar o ambiente, executar sempre os scripts com `python -m ...`.

Os outputs principais atuais são tabelas CSV e LaTeX `.tex`. Alguns ficheiros Markdown podem existir como legado técnico, mas não são o formato principal para o relatório.

No ambiente local usado neste projeto, o `python3` do sistema não tem `scikit-learn`. Para correr o Exercício 3 foi usado o virtualenv:

```bash
/home/tiago-nevoa/.virtualenvs/fcd-g11/bin/python
```

## Preparação do ambiente Python

Criar e ativar um ambiente virtual, depois instalar as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r A3/requirements.txt
```

## Menu de execução

Executar a partir da raiz do repositório, com o ambiente virtual ativado:

```bash
cd <repo-root>
source <path-to-venv>/bin/activate
python -m A3.src.menu
```

O menu permite correr scripts individuais, correr o Exercício 3, correr todos os scripts e verificar se os outputs esperados existem.

Também pode ser usado diretamente com o Python do virtualenv validado:

```bash
cd <repo-root>
/home/tiago-nevoa/.virtualenvs/fcd-g11/bin/python -m A3.src.menu
```

## Configuração local opcional

O ficheiro `A3/config/local.properties.example` é o template de configuração local.
Cada utilizador pode criar `A3/config/local.properties`, que é local e não deve ir para Git.

Criar a configuração local:

```bash
cp A3/config/local.properties.example A3/config/local.properties
```

Depois editar `A3/config/local.properties` e preencher:

```text
repo_root=<repo-root>
venv_path=<path-to-venv>
```

Com essa configuração, é possível abrir o menu com:

```bash
bash A3/scripts/run_menu.sh
```

Também é possível continuar a usar o comando genérico:

```bash
cd <repo-root>
source <path-to-venv>/bin/activate
python -m A3.src.menu
```

## Exercício 1 - Ambiente

Executar:

```bash
cd <repo-root>
source <path-to-venv>/bin/activate
python -m A3.src.ex1.environment_check
```

Ficheiros gerados:

* `A3/output/ex1/tables/environment_versions.csv`
* `A3/output/ex1/tables/environment_versions.tex`

## Exercício 2(a) - Caracterização dos datasets

A tabela do Exercício 2(a) caracteriza apenas Diabetes, Iris e Forest Fires. O dataset Wine Quality - White é usado posteriormente no Exercício 3.

Executar:

```bash
cd <repo-root>
source <path-to-venv>/bin/activate
python -m A3.src.ex2.a.dataset_inventory
python -m A3.src.ex2.a.dataset_summary
python -m A3.src.ex2.a.dataset_conversion
```

Ficheiros gerados:

* `A3/output/ex2/a/tables/ex2a_dataset_summary.csv`
* `A3/output/ex2/a/tables/ex2a_dataset_summary.tex`
* `A3/output/ex2/a/tables/ex2a_converted_files.csv`
* `A3/output/ex2/a/tables/ex2a_converted_files.tex`
* `A3/output/ex2/a/converted/`

## Exercício 2(b) - Visualização do Iris

Este exercício gera três scatter-plots individuais, um gráfico de barras, uma tabela com a distribuição das classes e uma tabela neutra com o índice dos scatter-plots.

Executar:

```bash
cd <repo-root>
source <path-to-venv>/bin/activate
python -m A3.src.ex2.b.iris_visualization
```

Ficheiros gerados:

* `A3/output/ex2/b/figures/2b_Iris_PetalLength_PetalWidth.png`
* `A3/output/ex2/b/figures/2b_Iris_SepalLength_SepalWidth.png`
* `A3/output/ex2/b/figures/2b_Iris_SepalLength_PetalLength.png`
* `A3/output/ex2/b/figures/2b_Iris_ClassDistribution.png`
* `A3/output/ex2/b/tables/2b_iris_class_distribution.csv`
* `A3/output/ex2/b/tables/2b_iris_class_distribution.tex`
* `A3/output/ex2/b/tables/2b_iris_scatter_plot_index.csv`
* `A3/output/ex2/b/tables/2b_iris_scatter_plot_index.tex`

Para adaptar este script a outro dataset, configurar no início de `iris_visualization.py` os valores `DATASET_ID`, `SCATTER_PAIRS` e `OUTPUT_PREFIX`. O dataset também deve estar registado em `A3/src/ex2/utils/datasets.py`.

## Exercício 3 - Classificação e avaliação

O Exercício 3 usa Diabetes, Iris, Wine Quality - White e Zoo. O dataset Zoo foi escolhido como dataset adicional de classificação multiclasse. O dataset Forest Fires não é usado no Exercício 3; fica apenas no Exercício 2(a), onde é caracterizado como problema de regressão.

O script avalia Decision Tree, kNN e SVM com validação cruzada estratificada 10-fold. Para kNN e SVM, a normalização com `StandardScaler` é feita dentro do pipeline avaliado na validação cruzada, evitando data leakage. O `random_state=0` é usado apenas para reprodutibilidade. Wine Quality e Zoo têm classes raras, pelo que o scikit-learn pode emitir avisos sobre classes com poucos exemplos; mantemos 10 folds porque é o procedimento pedido.

Executar pelo menu ou diretamente:

```bash
cd <repo-root>
source <path-to-venv>/bin/activate
python -m A3.src.ex3.main
```

No ambiente local validado, também pode ser executado diretamente com:

```bash
cd <repo-root>
/home/tiago-nevoa/.virtualenvs/fcd-g11/bin/python -m A3.src.ex3.main
```

Ficheiros principais gerados:

* `A3/output/ex3/tables/evaluation_summary.csv`
* `A3/output/ex3/tables/evaluation_summary.tex`
* `A3/output/ex3/tables/best_classifiers.csv`
* `A3/output/ex3/tables/best_classifiers.tex`
* `A3/output/ex3/tables/*_classification_report.csv`
* `A3/output/ex3/tables/*_classification_report.tex`
* `A3/output/ex3/tables/*_confusion_matrix.csv`
* `A3/output/ex3/tables/*_confusion_matrix.tex`
* `A3/output/ex3/figures/decision_tree.svg`

As tabelas LaTeX do Exercício 3 são geradas automaticamente pelo script de avaliação, usando funções auxiliares em `A3/src/ex3/main.py`.

Melhores classificadores validados:

* Diabetes: SVM.
* Iris: SVM.
* Wine Quality - White: Decision Tree.
* Zoo: Decision Tree.

O código gera outputs técnicos objetivos. A interpretação qualitativa dos resultados deve ser feita no relatório.

## Como adaptar scripts a outro dataset

Para reutilizar os scripts com outro dataset:

* adicionar a configuração do dataset em `A3/src/ex2/utils/datasets.py`;
* definir um `dataset_id` simples e único;
* definir a `target_column`;
* definir `read_options` quando o ficheiro precisar de separador, cabeçalho ou nomes de colunas específicos;
* garantir que o ficheiro existe em `A3/data/raw`;
* no script de visualização, ajustar `DATASET_ID`, `SCATTER_PAIRS` e `OUTPUT_PREFIX`.

## Notas para o relatório

No relatório PDF, as tabelas devem privilegiar nomes de ficheiros simples para manter a leitura clara.
Nos outputs técnicos e neste README, podem ser usados paths relativos completos para facilitar a validação dos ficheiros.

## Exportação limpa do projeto

A entrega/zip final não deve incluir ficheiros locais ou gerados automaticamente, como:

* `.git/`
* `.idea/`
* `A3/_local_references/`
* `A3/config/local.properties`
* `__pycache__/`
* `build/`
* `tmp/`

Comando recomendado para criar um zip limpo a partir do Git:

```bash
git archive --format=zip --output ../fcd-g11-a3.zip HEAD
```
