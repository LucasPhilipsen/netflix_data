# Análise de Filmes da Netflix (Anos 90)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![DataCamp](https://img.shields.io/badge/DataCamp-05192D?style=for-the-badge&logo=datacamp&logoColor=03E860)

Este projeto realiza uma Análise Exploratória de Dados (EDA) sobre o catálogo da Netflix, com foco específico em filmes lançados durante a década de 1990. O objetivo é entender tendências de duração e frequência de gêneros específicos.

Este projeto foi desenvolvido como parte de uma prática do **DataCamp**.

## Objetivos da Análise

O script responde às seguintes perguntas sobre os dados:
1. **Qual foi a duração de filme mais frequente na década de 1990?**
2. **Quantos filmes de ação curtos (menos de 90 minutos) foram lançados nessa década?**
3. **Qual a distribuição geral da duração dos filmes?** (Visualização gráfica)

## Tecnologias Utilizadas

* **Python 3**
* **Pandas**: Manipulação e filtragem de dados.
* **Matplotlib**: Visualização de dados (Histograma).
* **NumPy**: Operações numéricas.

## Estrutura do Projeto

* `main.py`: Arquivo principal que orquestra a execução. Ele importa os módulos, exibe os resultados no console e gera o gráfico.
* `netflix.py`: Contém a lógica de processamento de dados. Carrega o CSV, aplica filtros (apenas filmes, anos 90) e realiza os cálculos estatísticos (moda, contagem).
* `graph.py`: Responsável pela geração do histograma de distribuição das durações.
* `netflix_data.csv`: Base de dados utilizada (necessário adicionar este arquivo à pasta do projeto).
