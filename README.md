# Case NPS Preditivo — Análise Exploratória e Predição da Satisfação do Cliente

**FIAP | Pós-graduação em AI Scientist**

## Sobre o projeto

O projeto está organizado em duas etapas principais:

- **Análise Exploratória de Dados (EDA):** investigação dos dados para compreender o comportamento do NPS e identificar fatores relacionados à satisfação dos clientes.
- **Modelo Preditivo:** desenvolvimento de um modelo de Machine Learning para estimar a nota individual de NPS com base no perfil do cliente e em indicadores operacionais.

## O que é NPS?

O **Net Promoter Score (NPS)** é um indicador utilizado para avaliar a satisfação e a disposição dos clientes em recomendar uma empresa.

Na escala tradicional de 0 a 10, os clientes são classificados em:

![Classificação NPS](./NOME_DA_IMAGEM.png)

- **Detratores:** notas de 0 a 6.
- **Neutros:** notas de 7 a 8.
- **Promotores:** notas de 9 a 10.

O NPS agregado é calculado pela diferença entre o percentual de promotores e o percentual de detratores.

**Observação:** como a base utilizada neste projeto apresenta notas decimais, a classificação individual foi adaptada para manter os mesmos limites: detratores com notas inferiores a 7, neutros com notas de 7 até valores inferiores a 9 e promotores com notas de 9 a 10.

## Objetivos e perguntas norteadoras

### 1. Análise Exploratória de Dados

**Pergunta norteadora: Quais fatores operacionais estão mais associados à satisfação dos clientes de um e-commerce?**

A análise exploratória busca compreender a distribuição das notas de NPS, identificar padrões de insatisfação e investigar as relações entre o perfil dos clientes, a experiência de compra e os indicadores operacionais.

### 2. Modelo Preditivo

**Pergunta norteadora: Qual nota de NPS podemos estimar para um cliente com base em seu perfil e nos indicadores operacionais da sua experiência de compra?**

A modelagem busca desenvolver uma Regressão Linear Múltipla capaz de estimar a nota individual de NPS utilizando informações relacionadas ao cliente, pedido, entrega e atendimento.

## Base de dados

O projeto utiliza o arquivo `desafio_nps_fase_1.csv`, contendo **2.500 registros e 19 variáveis**.

As informações abrangem:

- **Perfil do cliente:** idade, região e tempo de relacionamento.
- **Pedido:** valor da compra, quantidade de itens, descontos e condições de pagamento.
- **Logística:** prazo de entrega, atrasos, frete e tentativas de entrega.
- **Atendimento:** contatos, reclamações e tempo de resolução.
- **Satisfação e comportamento:** nota de NPS, satisfação interna e recompra.

A variável principal do estudo é `nps_score`, que representa a nota individual de satisfação do cliente.

## Estrutura do projeto

```text
analise-nps/
│
├── data/
│   └── raw/
│       └── desafio_nps_fase_1.csv
│
├── notebooks/
│   ├── 01_analise_exploratoria.ipynb
│   └── 02_modelo_regressao_linear.ipynb
│
├── models/
│   └── modelo_nps.joblib
│
├── src/
│   ├── __init__.py
│   └── prever_nps.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Como navegar pelo projeto

O desenvolvimento principal está documentado na pasta `notebooks/`.

Para acompanhar o raciocínio e reproduzir o estudo, recomenda-se executar os notebooks na ordem numérica.

### 1. Análise Exploratória — `notebooks/01_analise_exploratoria.ipynb`

Este notebook representa a primeira etapa do projeto e deve ser o ponto de partida para compreender os dados e o problema de negócio.

Nele são realizadas:

1. Importação e conhecimento da base de dados.
2. Identificação e classificação das variáveis.
3. Verificação da qualidade e consistência dos dados.
4. Análise estatística e distribuição das notas de NPS.
5. Investigação das relações entre variáveis operacionais e satisfação.
6. Visualizações, interpretação dos resultados e recomendações para o negócio.

A análise contempla aspectos relacionados ao perfil dos clientes, logística e atendimento, utilizando gráficos e medidas estatísticas para identificar padrões associados à satisfação.

As interpretações e conclusões estão documentadas ao longo do próprio notebook.

### 2. Modelo Preditivo — `notebooks/02_modelo_regressao_linear.ipynb`

O segundo notebook utiliza os dados do projeto para desenvolver um modelo de **Regressão Linear Múltipla**, com a biblioteca Scikit-learn.

O desenvolvimento está organizado nas seguintes etapas:

1. Definição do problema preditivo e da variável alvo `nps_score`.
2. Seleção das variáveis preditoras.
3. Separação dos dados em treinamento e teste.
4. Pré-processamento das variáveis categóricas com One-Hot Encoding.
5. Treinamento do modelo de Regressão Linear.
6. Avaliação utilizando MAE, RMSE, R² e análise dos resíduos.
7. Avaliação complementar das classificações de NPS derivadas das previsões.
8. Criação e salvamento de um Pipeline para reutilização do modelo.

O notebook contém os códigos, gráficos, métricas e interpretações necessários para compreender as decisões tomadas durante a modelagem.

### 3. Base de dados — `data/raw/`

Contém o arquivo CSV original utilizado nas análises e no treinamento do modelo.

### 4. Modelo treinado — `models/modelo_nps.joblib`

Armazena o Pipeline treinado, incluindo o pré-processamento das variáveis e o modelo de Regressão Linear.

Esse arquivo permite realizar novas previsões sem precisar executar novamente o treinamento.

### 5. Programa de previsão — `src/prever_nps.py`

Programa Python responsável por carregar o modelo salvo, solicitar as informações de um cliente e apresentar a nota de NPS estimada.

### 6. Dependências — `requirements.txt`

Contém as bibliotecas necessárias para executar os notebooks e o programa de previsão, permitindo a configuração do ambiente de desenvolvimento.

## Como executar o projeto

### 1. Instalar as dependências

Com Python instalado e o ambiente virtual ativado, abra o terminal na pasta raiz do projeto e execute:

```bash
pip install -r requirements.txt
```

Esse comando instalará as bibliotecas utilizadas no desenvolvimento, conforme especificadas no arquivo `requirements.txt`.

### 2. Executar os notebooks

Abra o projeto no VS Code, utilizando as extensões Python e Jupyter, e selecione o ambiente Python que contém as dependências instaladas.

Em seguida, acesse a pasta `notebooks/` e execute os arquivos nesta ordem:

**Primeiro:** `01_analise_exploratoria.ipynb`

Permite acompanhar a investigação dos dados, os gráficos, as análises estatísticas e as conclusões sobre a satisfação dos clientes.

**Segundo:** `02_modelo_regressao_linear.ipynb`

Permite acompanhar a seleção das variáveis, o treinamento, a avaliação e o salvamento do modelo preditivo.

As células devem ser executadas sequencialmente. Os caminhos relativos dos arquivos consideram que os notebooks são executados a partir da pasta `notebooks/`.

### 3. Executar o programa de previsão

Para utilizar o modelo treinado sem precisar executar os notebooks, abra o terminal na pasta raiz do projeto e execute:

```bash
python -m src.prever_nps
```

O programa solicitará as **14 variáveis preditoras** utilizadas no treinamento, relacionadas ao perfil do cliente, pedido, entrega e atendimento.

Ao finalizar o preenchimento, serão apresentados:

- A nota de NPS prevista pelo modelo.
- A classificação correspondente: Detrator, Neutro ou Promotor.