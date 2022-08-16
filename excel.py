from openpyxl import load_workbook

def importa_excel(planilha):
    base = load_workbook(f"{planilha}")
    planilha = base.active
    return planilha

# FUNÇAO PARA RETORNAR UMA CELULA
def retorna_dado_celula(planilha, linha, coluna):
     celula  = planilha.cell(roll = linha, column = coluna)
     return celula.value

# FUNCAO PARA PREENCHER UMA CELULA
def preencher_celula(planilha,celula_valor,linha, coluna):
    planilha.cell(row=linha, column= coluna, value = celula_valor)


# FUNCAO PARA CRIAR UMA LISTA DE RE's
def retorna_lista_re(planilha):
    lista_re =list()
    for celula in planilha["A"]:
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
            continue
        else:
            lista_nome.append(celula.value)
            
    return lista_nome