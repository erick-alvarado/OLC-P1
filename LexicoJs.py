from graphviz import Digraph
from enum import Enum
from Token import Token
from Error import Error

class lexicoJs:
   
   
   
   
   
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
      ":": "SIM_DOS_PUNTOS" ,
      "{": "SIM_ABRIR_CORCHETES" ,
      "}": "SIM_CERRAR_CORCHETES" ,
      ">": "SIM_MAYOR" ,
      "<": "SIM_MENOR" ,
      ".": "SIM_PUNTO" ,
      ",": "SIM_COMA" ,
      "-": "SIM_MENOS" ,
      "+": "SIM_MAS" ,
      "!": "SIM_EXCLAMACION" ,
      "(": "SIM_ABRIR_PARENTESIS" ,
      ")": "SIM_CERRAR_PARENTESIS" ,
      "/": "SIM_BARRA" ,
       "*": "SIM_ASTERISCO",
        "&&": "SIM_AND",
         "||": "SIM_OR",

   }
   #"CADENA_TEXTO"
   #"NUMERO"
   #"VARIABLE"
   #"COMENTARIO"

 
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
      self.q1=False
      self.q17=False
      self.q15=False

      self.q9=False
      self.q8=False
      self.q5=False
      self.q10=False
      self.q6=False
      self.q7=False
      self.q12=False
      self.q13= False

   def analizarJs(self,txt):
      
      self.resetear()
      self.texto = txt
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
            self.columna+=1
            self.estadoCaracter2()
         elif self.char=='\'' :
            self.cadena+=self.char
            nombre = self.lenguaje.get(self.cadena)
            self.guardar(nombre,self.cadena)
            self.cadena=""
            self.contador+=1
            self.columna+=1
            self.estadoCaracter4()
         elif (self.char=='&' and self.texto[self.contador+1]=='&' ):
               self.columna+=1
               self.cadena= "&&"
               self.contador+=1
               nombre = self.lenguaje.get(self.cadena)
               self.guardar(nombre,self.cadena)
               self.cadena=""
               self.q15=True
         elif (self.char=='|' and self.texto[self.contador+1]=='|' ):
               self.columna+=1
               self.cadena= "||"
               self.contador+=1
               nombre = self.lenguaje.get(self.cadena)
               self.guardar(nombre,self.cadena)
               self.cadena=""
               self.q17=True
         elif self.char=='/' :
            self.cadena+=self.char
            nombre = self.lenguaje.get(self.cadena)
            self.guardar(nombre,self.cadena)
            self.cadena=""
            self.q8=True
            try:
               self.contador+=1
               self.columna+=1
               self.char  = self.texto[self.contador]
               if(self.char == '*'):
                  self.cadena+=self.char
                  nombre = self.lenguaje.get(self.cadena)
                  self.guardar(nombre,self.cadena)
                  self.cadena=""
                  self.contador+=1
                  self.columna+=1
                  self.estadoCaracter()
               elif self.char == '/':
                  self.q9=True
                  self.cadena+=self.char
                  nombre = self.lenguaje.get(self.cadena)
                  self.guardar(nombre,self.cadena)
                  self.cadena=""
                  self.contador+=1
                  self.columna+=1
                  self.estadoCaracter3()
               else:
                  self.contador-=1
            except:
               a = 0

         elif not self.lenguaje.get(self.char) == None:
            self.q1=True
            self.cadena+=self.char
            nombre = self.lenguaje.get(self.cadena)
            self.guardar(nombre,self.cadena)
            self.cadena=""

         elif self.char.isalpha() or self.char=="-":
            self.cadena+=self.char
            self.contador+=1
            self.columna+=1
            self.q6=True
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
         s[x]=""

      str1 = ''.join(s)
          
      return str1


   def estadoLetra(self):

      self.char  = self.texto[self.contador]
      while(self.char.isalpha() or self.texto[self.contador]=="-"):
         self.cadena+=self.char
         self.contador+=1
         self.columna+=1
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
      self.q7 = True
      self.contador+=1
      self.char  = self.texto[self.contador]
      while(self.char.isnumeric()):
         self.cadena+=self.char
         self.contador+=1
         self.columna+=1
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
      try:
         num = self.contador
         print(self.char)
         print(self.texto[self.contador+1])
         while(True):
            if(self.char=='*' and self.texto[self.contador+1]=='/'):
               break
            if(self.char == '\n'):
               self.fila+=1
               self.columna=0
            
            self.cadena+=self.char
            self.contador+=1
            self.columna+=1
            self.char  = self.texto[self.contador]
         
         self.guardar("COMENTARIO",self.cadena)
         self.guardar("SIM_ASTERISCO","*")
         self.guardar("SIM_BARRA","/")
         self.cadena=""
         self.contador+=1
         self.q5=True

      except:
         self.contador=num
         self.cadena=""
   
   def estadoCaracter2(self):
      self.char  = self.texto[self.contador]
      while(not self.char=='\"'):
         self.cadena+=self.char
         self.contador+=1
         self.columna+=1
         self.char  = self.texto[self.contador]
      self.q12=True
      self.guardar("CADENA",self.cadena)
      self.guardar("SIM_COMILLA",self.char)
      self.cadena=""

   def estadoCaracter3(self):
      self.char  = self.texto[self.contador]
      try:

         while(not self.char=='\n'):
            self.cadena+=self.char
            self.contador+=1
            self.columna+=1
            self.char  = self.texto[self.contador]
      except:
         print("Falto el \\n")
      self.guardar("COMENTARIO",self.cadena)
      self.cadena=""
      self.q10=True
      
   def estadoCaracter4(self):
      self.char  = self.texto[self.contador]
      while(not self.char=='\''):
         self.cadena+=self.char
         self.contador+=1
         self.columna+=1
         self.char  = self.texto[self.contador]
      self.q13=True
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

   def generarGrafica(self):
      self.dot = Digraph(comment='AutomataJs')
      self.dot.node('q0', 'q0')
      if(self.q1):
         self.dot.node('q1', 'q1')
         self.dot.edge('q0', 'q1', label='; \n{\n }\n <\n >\n =\n |\n +\n *\n -\n )\n (\n . \n')
      if(self.q17):
         self.dot.node('q16', 'q16')
         self.dot.node('q17', 'q17')
         self.dot.edge('q0', 'q16', label = '|')
         self.dot.edge('q16', 'q17', label = '|')
      if(self.q15):
         self.dot.node('q14', 'q14')
         self.dot.node('q15', 'q15')
         self.dot.edge('q0', 'q14', label = '&')
         self.dot.edge('q14', 'q15', label = '&')
      if(self.q8):
         self.dot.node('q8', 'q8')
         self.dot.edge('q0', 'q8', label = '/')
      if(self.q9):
         self.dot.node('q9', 'q9')
         self.dot.edge('q8', 'q9', label = '/')
      if(self.q10):
         self.dot.node('q10', 'q10')
         self.dot.edge('q9', 'q10', label = 'C')
         self.dot.edge('q10', 'q10', label = 'C') 
      if(self.q5):
         self.dot.node('q3', 'q3')
         self.dot.node('q4', 'q4')
         self.dot.node('q5', 'q5')
         self.dot.edge('q8', 'q3', label = '*')
         self.dot.edge('q3', 'q3', label = 'C')
         self.dot.edge('q3', 'q4', label = '*')
         self.dot.edge('q4', 'q5', label = '/')
      if(self.q6):
         self.dot.node('q6', 'q6')
         self.dot.edge('q0', 'q6', label = '- \n L')
         self.dot.edge('q6', 'q6', label = '- \n L')
      if(self.q7):
         self.dot.node('q7', 'q7')
         if(self.q6):
            self.dot.edge('q6', 'q7', label = 'D')
         
         self.dot.edge('q0', 'q7', label = 'D')
         self.dot.edge('q7', 'q7', label = 'D')
      if(self.q12):
         self.dot.node('q11', 'q11')
         self.dot.node('q12', 'q12')
         self.dot.edge('q0', 'q11', label = '\"')
         self.dot.edge('q11', 'q11', label = 'C')
         self.dot.edge('q11', 'q12', label = '\"')
      if(self.q13):
         self.dot.node('q2', 'q2')
         self.dot.node('q13', 'q13')
         self.dot.edge('q0', 'q2', label = '\'')
         self.dot.edge('q2', 'q2', label = 'C')
         self.dot.edge('q2', 'q13', label = '\'')
      
      self.dot.attr('node', shape='circle')      
      
      self.dot.view()







      









   