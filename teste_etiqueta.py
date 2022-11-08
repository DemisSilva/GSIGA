from openpyxl import Workbook,load_workbook
from excel import preencher_celula

ws = Workbook()
etiqueta = ws.active

for linha in range(1,15):
    if linha % 3 == 0:
            etiqueta.insert_rows(idx=linha, amount= 2 )
    elif linha
    else:    
        preencher_celula(etiqueta,"senha",linha,1)
        preencher_celula(etiqueta,"data",linha + 1,1)

ws.save('Etiqueta.xlsx')