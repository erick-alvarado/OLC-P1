from enum import Enum
from Token import Token
from Error import Error

class lexicoJs:
   
   fila = 1
   columna = 0
   cadena = ""
   contador =-1
   char = ''
   texto = ""
   lista_token = []
   lista_errores =[]
   lista_pos_error=[]

   lenguaje = {
      "var":"TIPO_VARIABLE",

      "true":"VALOR_TRUE",
      "false":"VALOR_FALSE",

      "if":"SENTENCIA_IF",
      "else":"SENTENCIA_ELSE",
      "for":"SENTENCIA_FOR",
      "do":"SENTENCIA_DO",
      "while":"SENTENCIA_WHILE",

      "continue":"SENTENCIA_ESCAPE_CONTINUE",
      "break":"SENTENCIA_ESCAPE_BREAK",
      "return":"SENTENCIA_ESCAPE_RETURN",


      "class":"PROPIEDAD_CLASE",
      "function":"PROPIEDAD_FUNCTION",
      "console":"PROPIEDAD_CONSOLE"  ,
      "log":"PROPIEDAD_LOG"  ,
      "this":"PROPIEDAD_THIS"  ,
      "Math":"PROPIEDAD_MATH"  ,
      "pow":"PROPIEDAD_POW"  ,

      "=": "SIM_IGUAL" ,
      "\"": "SIM_COMILLA" ,
      "\'": "SIM_COMILLA_SIMPLE" ,
      ";": "SIM_PUNTO_COMA" ,
      "{": "SIM_ABRIR_CORCHETES" ,
      "}": "SIM_CERRAR_CORCHETES" ,
      ">": "SIM_MAYOR" ,
      "<": "SIM_MENOR" ,
      ".": "SIM_PUNTO" ,
      ",": "SIM_COMA" ,
      "-": "SIM_MENOS" ,
      "+": "SIM_MAS" ,
      "!": "SIM_EXCLAMACION" ,
      "&": "SIM_INCLUSION" ,
      "|": "SIM_BARRA_VERTICAL" ,
      "(": "SIM_ABRIR_PARENTESIS" ,
      ")": "SIM_CERRAR_PARENTESIS" ,
      "/": "SIM_BARRA" ,
       "*": "SIM_ASTERISCO" 

   }
   #"CADENA_TEXTO"
   #"NUMERO"
   #"VARIABLE"
   #"COMENTARIO"

 

   def analizarJs(self,txt):
      self.lista_errores=[]
      self.texto=txt
      self.contador = -1
      self.fila=1
      self.columna=0
      fila = 1
      while(self.contador<len(self.texto)-1):
         
         self.contador+=1
         self.columna+=1
         self.char  = self.texto[self.contador]
         if self.char=='\t' or  self.char==" " or  self.char=="\r" :
            a = 0
         elif self.char=='\n' :
            self.columna=0
            self.fila+=1
         elif self.char=='\"' :
            self.cadena+=self.char
            nombre = self.lenguaje.get(self.cadena)
            self.guardar(nombre,self.cadena)
            self.cadena=""
            self.contador+=1
            self.estadoCaracter2()
         elif self.char=='\'' :
            self.cadena+=self.char
            nombre = self.lenguaje.get(self.cadena)
            self.guardar(nombre,self.cadena)
            self.cadena=""
            self.contador+=1
            self.estadoCaracter4()
         elif self.char=='/' :
            self.cadena+=self.char
            nombre = self.lenguaje.get(self.cadena)
            self.guardar(nombre,self.cadena)
            self.cadena=""

            try:
               self.contador+=1
               self.char  = self.texto[self.contador]
               if(self.char == '*'):
                  self.cadena+=self.char
                  nombre = self.lenguaje.get(self.cadena)
                  self.guardar(nombre,self.cadena)
                  self.cadena=""
                  self.contador+=1
                  self.estadoCaracter()
               elif self.char == '/':
                  self.cadena+=self.char
                  nombre = self.lenguaje.get(self.cadena)
                  self.guardar(nombre,self.cadena)
                  self.cadena=""
                  self.contador+=1
                  self.estadoCaracter3()
               else:
                  self.contador-=1
            except:
               a = 0

         elif not self.lenguaje.get(self.char) == None:

            self.cadena+=self.char
            nombre = self.lenguaje.get(self.cadena)
            self.guardar(nombre,self.cadena)
            self.cadena=""

         elif self.char.isalpha() or self.char=="-":
            self.cadena+=self.char
            self.contador+=1
            self.estadoLetra()
         elif self.char.isnumeric():
            self.cadena+=self.char
            self.estadoNumero()
         else:
            self.cadena+=self.char
            self.errorLexico(self.cadena,self.columna,self.fila)


   def textoFinal(self):
      s = list(self.texto)
      
      for x in self.lista_pos_error:
         s[x]=" "

      str1 = ''.join(s)
          
      return str1


   def estadoLetra(self):

      self.char  = self.texto[self.contador]
      while(self.char.isalpha() or self.texto[self.contador]=="-"):
         self.cadena+=self.char
         self.contador+=1
         self.char  = self.texto[self.contador]

      if self.texto[self.contador].isdigit():
         self.contador-=1
         self.estadoNumero()

      else:
         self.contador-=1
         nombre = self.lenguaje.get(self.cadena)
         if(not nombre==None):
            self.guardar(nombre,self.cadena)
         else:
            self.guardar("ID",self.cadena)
      self.cadena=""
      
      
   def estadoNumero(self):
      self.contador+=1
      self.char  = self.texto[self.contador]
      while(self.char.isnumeric()):
         self.cadena+=self.char
         self.contador+=1
         self.char  = self.texto[self.contador]
         
      self.contador-=1
      a=self.cadena.isdigit()
      if(a):
         self.guardar("NUMERO",self.cadena)
         self.cadena=""

      else:
         self.guardar("ID",self.cadena)
         self.cadena=""
      

   def estadoCaracter(self):
      self.char  = self.texto[self.contador]
      while(not self.char=="*" and not self.texto[self.contador+1]=="/"):
         self.cadena+=self.char
         self.contador+=1
         self.char  = self.texto[self.contador]
      
      self.guardar("COMENTARIO",self.cadena)
      self.cadena=""
      self.contador-=1
   
   def estadoCaracter2(self):
      self.char  = self.texto[self.contador]
      while(not self.char=='\"'):
         self.cadena+=self.char
         self.contador+=1
         self.char  = self.texto[self.contador]
      
      self.guardar("CADENA",self.cadena)
      self.guardar("SIM_COMILLA",self.char)
      self.cadena=""

   def estadoCaracter3(self):
      self.char  = self.texto[self.contador]
      try:

         while(not self.char=='\n'):
            self.cadena+=self.char
            self.contador+=1
            self.char  = self.texto[self.contador]
      except:
         print("Falto el \\n")
      self.guardar("COMENTARIO",self.cadena)
      self.cadena=""
      
   def estadoCaracter4(self):
      self.char  = self.texto[self.contador]
      while(not self.char=='\''):
         self.cadena+=self.char
         self.contador+=1
         self.char  = self.texto[self.contador]
      
      self.guardar("CADENA",self.cadena)
      self.guardar("SIM_COMILLA_SIMPLE",self.char)
      self.cadena=""

   def guardar(self, texto,val):
      print (texto +" : "+val)
      self.lista_token.append(Token(texto,val))

   def errorLexico(self,texto,x,y):
      print ("ERROR LEXICO" +" : "+texto)
      self.lista_pos_error.append(self.contador)
      self.cadena = ""
      self.lista_errores.append(Error(x,y,"Cadena no reconocida: "+texto))

   


      