from random import randint

# CLASSE FUNCIONARIO
class Funcionario:
    def __init__(self, re,nome):
        self.re = re
        self.nome = nome
        senha = 0
        maquina = 0
        monitor = ""

    # FUNÇOES PARA GERAR SENHA
    
    #   FACEBOOK 
    def gera_senha(self, operacao):
        if operacao == "FACEBOOK":
            random = randint(1000,9999)
            self.senha = "F@ceb00k" + str(random)

    #   MERCADO LIVRE
        elif operacao == "MP":
            random = randint(1000,9999)
            self.senha = "M&rc4do" + str(random)

    #   FLEURY
        elif operacao == "FLEURY":
            random = randint(10000,99999)
            self.senha = "F!&ury" + str(random)

    #   CIELO    
        elif operacao == "CIELO":
            random = randint(1000000,999999)
            self.senha = "C!el0" + str(random)

        else:
            print("Operação invalida")

    def set_maquina(self,maquina):
        self.maquina = maquina

    def set_monitor(self,monitor):
        self.monitor = monitor    
