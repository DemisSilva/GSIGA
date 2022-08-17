
from funcionario import Funcionario
def gera_funcionario(lista_re,lista_nome,max_linha,operacao):
    lista = list()
    for i in range(max_linha -1):
        re = lista_re[i]
        nome = lista_nome[i]
        func = Funcionario(re,nome)
        func.gera_senha(operacao)
        lista.append(func)
        
        return lista
