import sqlite3

def databaseConnector(pathDataBase, query):
    # Conectar ao banco de dados SQLite
    conexao = sqlite3.connect(pathDataBase)
    cursor = conexao.cursor()

    # Executar consulta SQL para recuperar todos os usuários
    cursor.execute(query)
    cliente = cursor.fetchall()

    # Fechar a conexão com o banco de dados
    conexao.close()

    return cliente