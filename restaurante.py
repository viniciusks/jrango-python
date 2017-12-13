class Restaurante:
    def __init__(self,name,code):
        self.__name = name
        self.__code = code
        self.__frequencia = 0

    def setName(self,name):
        self.__name = name
        return

    def getName(self):
        return self.__name

    def setCode(self,code):
        self.__code = code
        return

    def getCode(self):
        return self.__code

    def setFrequencia(self):
        self.__frequencia += 1
        return

    def getFrequencia(self):
        return self.__frequencia