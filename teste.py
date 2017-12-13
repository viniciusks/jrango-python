class Veiculo(object):
    def __init__(self):
        self.__velocidade = 0
    
    def setVelocidade(self,velo):
        self.__velocidade = velo
        return

    def getVelocidade(self):
        return self.__velocidade

class Bicicleta(Veiculo):
    def __init__(self):
        super(Bicicleta,self).__init__()
        self.__marcha = 0

    def setMarcha(self,marcha):
        self.__marcha = marcha
        return

    def getMarcha(self):
        return self.__marcha