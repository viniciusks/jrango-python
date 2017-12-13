from cartao import *
from restaurante import *

class Operadora:
    def __init__(self):
        self.__cartoes = []
        self.__restaurantes = []
        self.__name = ""
        self.__code = ""
        self.__saldo = ""
        self.__nomeR = ""
        self.__codeR = ""
    
    def cadastroCartao(self):
        self.__name = input("Digite o nome do cartão: ")
        self.__code = input("Digite o código do cartão: ")
        self.__saldo = int(input("Digite o saldo: "))

        c = Cartao(self.__name,self.__code,self.__saldo)

        print("\nNome: " + c.getName())
        print("Código: " + c.getCodigo())
        print("Saldo: R$" + str(c.getSaldo()) + ",00")

        cTarget = c.getCodigo()
        permission = True
        for cartao in self.__cartoes:
            if cTarget == cartao.getCodigo():
                print("Cartão com este código ("+ cartao.getCodigo() +") já foi cadastrado em nosso sistema. Cadastre com outro código por gentileza.")
                permission = False
        if permission == True:
            self.__cartoes.append(c)

    def cadastroRestaurante(self):
        self.__nameR = input("Digite o nome do restaurante: ")
        self.__codeR = input("Digite o código do restaurante: ")

        r = Restaurante(self.__nameR,self.__codeR)

        rTarget = r.getCode()
        permission = True
        for restaurante in self.__restaurantes:
            if rTarget == restaurante.getCode():
                print("Restaurante com este código ("+ restaurante.getCode() +") já foi cadastrado em nosso sistema. Cadastre com outro código por gentileza.")
                permission = False
        if permission == True:
            self.__restaurantes.append(r)

    def acrescentarCredito(self):
        # Primeiro encontrar o cartão
        cTarget = input("Digite o número do cartão: ")
        saldo = int(input("Digite a quantidade de créditos que deseja inserir: "))
        for cartao in self.__cartoes:
            if cTarget == cartao.getCodigo():
                cartao.addSaldo(saldo)
    
    def listarCartoes(self):
        if self.__cartoes == []:
            print("Não temos cartões cadastrados ainda.")
        else:
            print("\nLista de cartões:")
            for cartao in self.__cartoes:
                print(" - " + cartao.getName() + " / " + "Saldo: R$" + str(cartao.getSaldo()) + ",00")
    
    def listarRestaurantes(self):
        if self.__restaurantes == []:
            print("Não temos restaurantes cadastrados ainda.")
        else:
            print("\nLista de restaurantes:")
            for restaurante in self.__restaurantes:
                print(" - " + restaurante.getName() + " / " + "Frequência: " + str(restaurante.getFrequencia()))

    def opPgto(self):
        # Primeiro procura o cartão
        cTarget = input("Digite o número do cartão: ")
        error = 0
        for cartao in self.__cartoes:
            if cTarget == cartao.getCodigo():
                # Segundo procura o restaurante
                rTarget = input("Digite o número do restaurante: ")
                for restaurante in self.__restaurantes:
                    if rTarget == restaurante.getCode():
                        # terceiro realiza o pagamento
                        vlrPago = int(input("Digite o valor a ser pago: "))
                        vlrInicial = int(cartao.getSaldo())
                        vlrTotal = vlrInicial - vlrPago
                        cartao.setSaldo(str(vlrTotal))
                        restaurante.setFrequencia()
                        print("Seu saldo: " + cartao.getSaldo())
                        print("Pagamento realizado com sucesso!")
                        error = 0
                        return
                    else:
                        error = 1
            else:
                error = 1
        if error == 1:
            print("Não foi possível realizar o pagamento, verifique por favor o seu saldo!")
    
    def maisFrequentado(self):
        nomeFreq = ""
        freq = ""
        for restaurante in self.__restaurantes:
            aux = restaurante.getFrequencia()
            for restaurante2 in self.__restaurantes:
                if aux <= restaurante2.getFrequencia():
                    aux = restaurante2.getFrequencia()
                    freq = str(aux)
                    nomeFreq = restaurante2.getName()
        if nomeFreq == "" or freq == "0":
            print("Ainda não temos consumos.")
        else:
            print("\nRestaurante mais frequentado: " + nomeFreq + " / Frequência: " + freq)