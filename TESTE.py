from re import A
import pyodbc
from openpyxl import workbook,load_workbook
from random import randint

random = randint(1000,9999)

operacao = "FACEBOOK"
if operacao == "FACEBOOK":
    senha = "F@ceb00k" + str(random)  

print(senha)