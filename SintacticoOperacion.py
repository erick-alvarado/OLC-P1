from enum import Enum
from Token import Token
from Error import Error

class sintacticoOperacion:
   
   def resetear(self):
      self.texto = "Valido"
      self.i=0
      self.lista = []
   def analizarSintactico(self, tokens):
      self.resetear()
      self.lista = tokens
      
      while self.i < len(tokens):
         
         self.inicio()

   def inicio(self):
      nombre = self.lista[self.i].nombre
      valor = self.lista[self.i].valor
      if self.checkAbrir("("):
         self.inicio()
         if self.checkCerrar(")"):
            print("ahuevos")
         else:
            self.errorSintactico()
      else:
         self.eps()

   def eps (self):
      if(self.checkVal("VAL")):
         a=0
      elif self.checkSim("SIM"):
         if(self.checkVal("VAL")):
            a=0
         else:
            self.errorSintactico()
      else:
         self.i-=1

 

   def errorSintactico(self):
      print ("Invalido")
      self.texto="Invalido"

   def checkSim(self,token):
      try:   
         if(self.lista[self.i].nombre == "SIM"):
            self.i+=1
            return True
         return False
      except:
         print("Fin de cadena")
   def checkVal(self,token):
      try:
         if(self.lista[self.i].nombre == "VAL"):
            self.i+=1
            return True
         return False
      except:
         print("Fin de cadena")
   def checkAbrir(self,token):
      try:
         if(self.lista[self.i].valor == "("):
            self.i+=1
            return True
         return False
      except:
         print("Fin de cadena")
   def checkCerrar(self,token):
      try:

         if(self.lista[self.i].valor == ")"):
            self.i+=1
            return True
         return False
      except:
         print("Fin de cadena")
