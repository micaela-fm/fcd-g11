# fcd-g11

Repositório de projetos da UC **Fundamentos de Ciências de Dados** (Verão 2025/2026) — ISEL, Licenciatura em Engenharia Informática e de Computadores.

## Módulos

### A.3 — Python para Machine Learning

Localização: [`A3/A3.ipynb`](A3/A3.ipynb)

Conteúdo:
- **Secção 2** — Visualização de dados e conversão entre formatos
  - Análise de três conjuntos de dados (Iris, Penguins, Titanic): características, valores omissos e tipo de problema
  - Conversão dos datasets para formato JSON
  - Scatter-plots e gráfico de barras sobre o dataset Iris
- **Secção 3** — Tarefas de classificação e avaliação de classificadores
  - Treino de Árvore de Decisão, kNN e SVM com 10-fold cross-validation
  - Matrizes de confusão, acurácia, precision, recall e F1-score
  - Datasets utilizados: Diabetes, Iris, Wine, Breast Cancer

## Dependências

```bash
pip install -r requirements.txt
```

Ou instalar individualmente:

```bash
pip install matplotlib numpy pandas scikit-learn seaborn
```