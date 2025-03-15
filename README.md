# Simple ETL Pipeline - Carregando Dados de Vendas de Chocolate
Este projeto é um pipeline ETL simples em Python que extrai, limpa e carrega dados de vendas de chocolate em um banco de dados SQLite.

## Funcionalidades
Extrair dados: O código lê um arquivo CSV contendo dados de vendas de chocolate.
Limpeza de dados: O código limpa os dados, tratando valores ausentes e renomeando colunas para um formato mais amigável.
Carregar dados: Os dados limpos são carregados em uma tabela no banco de dados SQLite.

### Dependências
Este projeto requer as seguintes bibliotecas Python:

- pandas para manipulação de dados.
- sqlite3 para interação com o banco de dados SQLite.
- os para manipulação de caminhos de arquivos.

#### Preparar o ambiente
Para preparar o ambiente basta executar os arquivos .py get_data.py ( esses arquivo gera o csv com os dados) e create_table.py(este arquivo criar o banco sqlite3 e a tabela).