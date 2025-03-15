import os
import sqlite3
import pandas as pd
from extract_and_clean_csv import clean_data

extract_data = os.getcwd()
folder_setup = os.path.join(os.path.dirname(extract_data), 'setup')

def load_data():
    from extract_and_clean_csv import df_sales
    # Executa a funcao que limpa os dados
    return clean_data(df_sales)

def connect_in_db():
    # Definindo o caminho do banco de dados dentro da pasta 'setup'
    db_path = os.path.join(os.path.dirname(__file__), folder_setup, 'choco_sales.db')
    
    # Verifique o caminho do banco
    print(f"Caminho para o banco de dados: {db_path}")
    
    # Conecta ao banco
    conn = sqlite3.connect(db_path)

    return conn

def load_into_table(conn, df_sales_clean):
    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Definir a consulta SQL de inserção
    query = '''
    INSERT INTO choco_sales (sales_person, country, product, date, amount, boxes_shipped)
    VALUES (?, ?, ?, ?, ?, ?)
    '''
    
    # Iterar sobre as linhas do DataFrame e inserir os dados na tabela
    for _, row in df_sales_clean.iterrows():
        cursor.execute(query, (
            row['sales_person'], 
            row['country'], 
            row['product'], 
            row['date'], 
            row['amount'], 
            row['boxes_shipped']
        ))

    # Confirmar as alterações
    conn.commit()

    return 'Dados inseridos na tabela!'

# executar a carga de dados
def main():
    # Carregar os dados
    df_sales_clean = load_data()

    # Conectar ao banco de dados
    conn = connect_in_db()

    # Inserir os dados na tabela
    message = load_into_table(conn, df_sales_clean)
    print(message)

    # Fecha a conexão
    conn.close()

if __name__ == "__main__":
    main()