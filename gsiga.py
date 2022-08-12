import pyodbc
from random import randint
import excel


# CONEXÃO COM O BANCO DE DADOS
def conecta_bd():

    dados_conexao = (
        "Driver={SQL Server};"
        "Server=DESKTOP-8DLMQSI;"
        "Database=Saidas_SIGA;"
    )
    conexao = pyodbc.connect(dados_conexao)
    print("Conexão bem sucedida")
    return conexao


# CLASSE SIGA
class Siga:
    def __init__(self,numero,operacao,data,funcionario):
        self.numero = numero
        self.operacao = operacao
        self.data = data
        self.funcionario = dict()

# CLASSE FUNCIONARIO
class Funcionario:
    def __init__(self, re,nome,senha,maquina,monitor):
        self.re = re
        self.nome = nome
    # FUNCÇOES GERADORAS DE SENHA 
    #  FACEBOOK  
    def gera_senha_facebook(self,operacao):
        random = randint(1000,9999)
        if operacao == "FACEBOOK":
            self.senha = "F@ceb00k" + str(random)

    #  MERCADO LIVRE
    def gera_senha_mp(self,operacao):
        random = randint(10000,99999)
        if operacao == "MP":
            self.senha = "M&rc4do" + str(random)
    
    #  FLERY
    def gera_senha_fleury(self,operacao):
        random = randint(10000,99999)
        if operacao == "FLEURY":
            self.senha = "F!&ury" + str(random)
    #  CIELO
    def gera_senha_cielo(self,operacao):
        random = randint(1000000,9999999)
        if operacao == "CIELO":
            self.senha = "C!el0" + str(random)
    
    def set_maquina(self,maquina):
        self.maquina = maquina

    def set_monitor(self,monitor):
        self.monitor = monitor    

# PROGRAMA PRINCIPAL --------------------------------------------------------------------------------------------------------------------

#CONECTANDO NO BANCO DE DADOS
conexao = conecta_bd()

# IMPORTANDO PLANILHA
planilha = excel.importa_planilha_excel("Base.xlsx")



