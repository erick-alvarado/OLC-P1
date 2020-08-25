class Token:

   nombre= ""
   valor = ""

   def __init__(self,nomb, val):
        self.nombre = nomb
        self.valor = val
    
   def getNombre(self):
        return self.nombre
    
   def getValor(self):
        return self.valor
