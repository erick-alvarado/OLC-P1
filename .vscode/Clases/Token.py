from enum import Enum, auto
class Token:
    def __init__(self,nombre, valor):
        self.nombre = nombre
        self.valor = valor
    
    @property
    def getNombre(self):
        return self.__nombre
    @property
    def getValor(self):
        return self.__valor
        

    