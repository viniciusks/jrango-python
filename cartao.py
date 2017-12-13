class Cartao:
    def __init__(self,name,codigo,saldo=0):
        self.__name = name
        self.__codigo = codigo
        self.__saldo = saldo
    
    def setName(self,name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def setCodigo(self,codigo):
        self.__codigo = codigo
    
    def getCodigo(self):
        return self.__codigo

    def addSaldo(self,saldo):
        if self.__saldo == 0:
            if saldo > 0:
                self.__saldo = saldo
                return
            else:
                print("Valor inserido menor que 0, insira um valor maior.")
                return
        else:
            self.__saldo += saldo
    
    def setSaldo(self,saldo):
        self.__saldo = saldo
        return

    def getSaldo(self):
        return self.__saldo