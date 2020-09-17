from enum import Enum
from Token import Token
from Error import Error

class lexicoOperacion:
   
   

   lenguaje = {

      "*": "SIM" ,
      "/": "SIM" ,
      "+": "SIM",
      "-": "SIM",
      "(": "SIM_ABRIR_PARENTESIS" ,
      ")": "SIM_CERRAR_PARENTESIS"
   }
   #"CADENA_TEXTO"
   #"NUMERO"
   def resetear(self):
      self.fila = 1
      self.columna = 0
      self.cadena = ""
      self.contador =-1
      self.char = ''
      self.texto = ""
      self.lista_token = []
      self.lista_errores =[]
      self.lista_pos_error=[]
   def analizarOp(self,txt):
      self.resetear()
      self.texto =txt
      while(self.contador<len(self.texto)-1):
         
         self.contador+=1
         self.columna+=1
         self.char  = self.texto[self.contador]
         if self.char=='\t' or  self.char==" " or  self.char=="\r" :
            a = 0
         elif self.char=='\n' :
            self.columna=0
            self.fila+=1
         
         elif not self.lenguaje.get(self.char) == None:
            self.cadena+=self.char
            nombre = self.lenguaje.get(self.cadena)
            self.guardar(nombre,self.cadena)
            self.cadena=""

         elif self.char.isalpha():
            self.cadena+=self.char
            self.contador+=1
            self.columna+=1
            self.estadoLetra()
         elif self.char.isnumeric():
            self.cadena+=self.char
            self.estadoNumero()
         else:
            self.cadena+=self.char
            self.errorLexico(self.cadena,self.columna,self.fila)

   def estadoLetra(self):
      try:

         self.char  = self.texto[self.contador]
         while(self.char.isalpha() or self.texto[self.contador]=="-"):
            self.cadena+=self.char
            self.contador+=1
            self.columna+=1
            self.char  = self.texto[self.contador]

         if self.texto[self.contador].isdigit():
            self.contador-=1
            self.columna-=1
            self.estadoNumero()

         else:
            self.contador-=1
            nombre = self.lenguaje.get(self.cadena)
            if(not nombre==None):
               self.guardar(nombre,self.cadena)
            else:
               self.guardar("VAL",self.cadena)
         self.cadena=""
      except:
         self.contador-=1
         nombre = self.lenguaje.get(self.cadena)
         if(not nombre==None):
            self.guardar(nombre,self.cadena)
         else:
            self.guardar("VAL",self.cadena)
         self.cadena="" 
   def estadoNumero(self):
      try:
         self.q7 = True
         self.contador+=1
         self.columna+=1
         self.char  = self.texto[self.contador]
         while(self.char.isnumeric()):
            self.cadena+=self.char
            self.contador+=1
            self.columna+=1
            self.char  = self.texto[self.contador]
            
         self.contador-=1
         a=self.cadena.isdigit()
         if(a):
            self.guardar("VAL",self.cadena)
            self.cadena=""

         else:
            self.guardar("VAL",self.cadena)
            self.cadena=""
      except:
         self.contador-=1
         a=self.cadena.isdigit()
         if(a):
            self.guardar("VAL",self.cadena)
            self.cadena=""
         else:
            self.guardar("VAL",self.cadena)
            self.cadena=""
   def guardar(self, texto,val):
      print (texto +" : "+val)
      self.lista_token.append(Token(texto,val))

   def errorLexico(self,texto,x,y):
      print ("ERROR LEXICO" +" : "+texto)
      self.lista_pos_error.append(self.contador)
      self.cadena = ""
      self.lista_errores.append(Error(x,y,"Cadena no reconocida: "+texto))

   


      
