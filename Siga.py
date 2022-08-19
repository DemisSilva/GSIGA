# CLASSE SIGA
class Siga:
    def __init__(self,numero,operacao,data, funcioanrios):
        self.numero = numero
        self.operacao = operacao
        self.data = data
        self.funcionarios = funcioanrios

    def insere_funcionario(self, funcionario):
        self.funcionarios["RE"] = funcionario.re
        self.funcionarios["Nome"] = funcionario.nome
        self.funcionarios["Senha"] = funcionario.senha

        