import pyodbc

def conecta_bd():

    dados_conexao = (
        "Driver={SQL Server};"
        "Server=DESKTOP-8DLMQSI;"
        "Database=Saidas_SIGA;"
    )
    conexao = pyodbc.connect(dados_conexao)
    print("Conexão bem sucedida")
    return conexao
    