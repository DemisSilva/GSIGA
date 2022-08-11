from re import A
import pyodbc
from openpyxl import workbook,load_workbook
from random import randint

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
        
    def gera_senha(self,operacao):
        random = randint(1000,9999)
        if operacao == "FACEBOOK":
            self.senha = "F@ceb00k" + str(random)

    def set_maquina(self,maquina):
        self.maquina = maquina

    def set_monitor(self,monitor):
        self.monitor = monitor    

            
# IMPORTANDO PLANILHA COM OS DADOS
base = load_workbook("Base.xlsx")
planilha = base.active

# CONEXÃO COM O BANCO DE DADOS
def Conecta_BD():

    dados_conexao = (
        "Driver={SQL Server};"
        "Server=DESKTOP-8DLMQSI;"
        "Database=Saidas_SIGA;"
    )
    conexao = pyodbc.connect(dados_conexao)
    print("Conexão bem sucedida")

# FUNÇAO PARA RETORNAR UMA CELULA
# def retorna_dado_celula(planilha, linha, coluna):
#     celula  = planilha.cell(roll = linha, column = coluna)
#     return celula.value

# FUNCAO PARA PREENCHER UMA CELULA
def preencher_celula(planilha,celula_valor,linha, coluna):
    planilha.cell(row=linha, column= coluna, value = celula_valor)


# FUNCAO PARA CRIAR UMA LISTA DE RE's
def retorna_lista_re(planilha):
    lista_re =list()
    for celula in planilha["A"]:
        print(celula.value)
        if celula.value == "RE":
            continue
        else:
            lista_re.append(int(celula.value))

    return lista_re

# FUNÇAO PARA RETORNAR OS NOMES
def retorna_lista_nome(planilha):
    lista_nome = list()
    for celula in planilha["B"]:
        if celula.value == "Nome":
            print("Nome")
        else:
            lista_nome.append(celula.value)
            
    return lista_nome

# FUNCAO PARA ALIMENTAR O BANCO DE DADOS
def alimenta_siga_br(numer_siga,operacao,data):
    numero_siga = input("Numero do siga:")
    operacao = input("Operacao:").upper()
    data = input("Data:")
    
def alimenta_funcionario_br(re, nome, max_linha):
    i=0
    while(i <= max_linha):

        i =+1 


# PROGRAMA PRINCIPAL
# Conecta_BD()


max_linha = planilha.max_row
lista_re = retorna_lista_re(planilha)
lista_nome = retorna_lista_nome(planilha)



    