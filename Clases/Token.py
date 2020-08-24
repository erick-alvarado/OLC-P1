from enum import Enum, auto
class Token:
    def __init__(self,nombre, valor):
        self.nombre = nombre
        self.valor = valor
    
    def getNombre(self):
        return self.__nombre
    
    def getValor(self):
        return self.__valor
        

    