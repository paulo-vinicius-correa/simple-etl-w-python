import sqlite3

def create_table(db_name):
    # Conectar ao banco de dados
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Criar a tabela de vendas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS choco_sales (
        id INTEGER PRIMARY KEY,
        sales_person TEXT,
        country TEXT,
        product TEXT,
        date DATE,
        amount REAL,
        boxes_shipped INTEGER
    )
    ''')
    # confirma as alteracoes
    conn.commit()
    # fecha a conexao
    conn.close()

db_name = 'choco_sales.db'

create = create_table(db_name)