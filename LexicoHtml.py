from enum import Enum
from Token import Token
from Error import Error

class lexicoHtml:
   
   

   lenguaje = {
      "html":"ETIQUETA_HTML",
      "head":"ETIQUETA_HEAD"  ,
      "title":"ETIQUETA_TITLE" ,
      "body": "ETIQUETA_BODY" ,

      "h1": "ETIQUETA_H1",
      "h2": "ETIQUETA_H2",
      "h3": "ETIQUETA_H3" ,
      "h4": "ETIQUETA_H4" ,
      "h5": "ETIQUETA_H5",
      "h6": "ETIQUETA_H6" ,

      "p": "ETIQUETA_P",
      "br": "ETIQUETA_BR" ,
      "img": "ETIQUETA_IMG" ,
      "src": "ATRIBUTO_SRC" ,
      "a": "ETIQUETA_A" ,
      "href": "ATRIBUTO_HREF" ,

      "ul": "ETIQUETA_UL"  ,
      "li": "ETIQUETA_LI",

      "style": "ATRIBUTO_STYLE" ,

      "table": "ETIQUETA_TABLE" ,
      "th": "ETIQUETA_TH"   ,
      "tr": "ETIQUETA_TR" ,
      "td": "ETIQUETA_TD" ,

      "caption": "ETIQUETA_CAPTION" ,
      "colgroup": "ETIQUETA_COLGROUP",
      "col": "ETIQUETA_COL" ,

      "thead": "ETIQUETA_THEAD" ,
      "tbody": "ETIQUETA_TBODY" ,
      "tfoot": "ETIQUETA_TFOOT",

      "color": "ESTILO_COLOR",
      "font": "ESTILO_FONT",
      "size" : "ESTILO_SIZE",
      "px" : "ESTILO_PX",
      "border" : "ESTILO_BORDER",

      "<": "SIM_MENOR" ,
      ">": "SIM_MAYOR",
      "/": "SIM_BARRA" ,
      "\'": "SIM_COMILLA",
      "\"": "SIM_COMILLA_DOBLE" ,
      "=": "SIM_IGUAL" ,
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
      self.ruta=""
   def analizarHTML(self,txt):
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
         elif self.char=='>' :    
            self.cadena+=self.char
            nombre = self.lenguaje.get(self.cadena)
            self.guardar(nombre,self.cadena)

            self.contador+=1
            self.columna+=1
            self.estadoCaracter2()
         elif self.char=='\"' :
            self.contador+=1
            self.columna+=1
            self.estadoCaracter()
         elif self.char=='\'' :
            self.contador+=1
            self.columna+=1
            self.estadoCaracter3()
         
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
      
   def textoFinal(self):
      s = list(self.texto)
      for x in self.lista_pos_error:
         s[x]=" "

      str1 = ''.join(s)
      
      print(str1)     
      return str1

   def estadoLetra(self):
      try:
         n = len(self.lista_token)
         self.char = self.texto[self.contador]
         if(self.char.isnumeric() and self.texto[self.contador-1] == 'h'):
            self.cadena += self.char
         else:
            while(self.char.isalpha()):
               self.cadena += self.char
               self.contador += 1
               self.char = self.texto[self.contador]

            self.contador -= 1

         nombre = self.lenguaje.get(self.cadena)
         if(not nombre == None):
            self.guardar(nombre, self.cadena)
         else:
            self.errorLexico(self.cadena, self.columna, self.fila)

         self.cadena = ""
      except:

         print("finalizo la cadena")
         nombre = self.lenguaje.get(self.cadena)
         if(not nombre == None):
            self.guardar(nombre, self.cadena)
         else:
            self.errorLexico(self.cadena, self.columna, self.fila)

         self.cadena = ""
      
   def estadoNumero(self):
      try:
         self.contador+=1
         self.columna+=1
         self.char  = self.texto[self.contador]
         while(self.char.isnumeric()):
            self.cadena+=self.char
            self.contador+=1
            self.columna+=1
            self.char  = self.texto[self.contador]
            
         
         self.guardar("NUMERO",self.cadena)
         self.cadena=""
         self.contador-=1
      except:
         print("Finalizo la cadena")
         self.guardar("NUMERO",self.cadena)
         self.cadena=""

   def estadoCaracter(self):
      try:
         num = self.contador-1
         colum = self.columna-1
         fil = self.fila
         self.char  = self.texto[self.contador]
         while(not self.char=='\"'):
            if(self.char == '\n'):
               self.fila+=1
               self.columna=0
            self.cadena+=self.char
            self.contador+=1
            self.columna+=1
            self.char  = self.texto[self.contador]
         self.q12=True
         self.guardar("SIM_COMILLA",self.char)
         self.guardar("CADENA",self.cadena)
         self.guardar("SIM_COMILLA",self.char)
         self.cadena=""
      except:
         self.contador=num
         self.columna= colum
         self.fila=fil
         self.cadena='\"'
         self.errorLexico(self.cadena,self.columna+1,self.fila)
   
   def estadoCaracter2(self):
      try:
         self.char  = self.texto[self.contador]
         while(not self.char=='<'):
            if(self.char == '\n'):
               self.fila+=1
               self.columna=0
            if(not self.char == '\n' and not self.char == '\t' and not self.char == '\r' ):
               self.cadena+=self.char
            self.contador+=1
            self.columna+=1
            self.char  = self.texto[self.contador]

         if len(self.cadena)>0:
            self.guardar("CADENA",self.cadena)
            self.guardar("SIM_MENOR",self.char)
            self.cadena=""
         else:
            self.contador-=1
            self.columna-=1
      except:
         self.contador-=1
         self.columna-=1
         print("fin de la cadena")
      
   def estadoCaracter3(self):
      try:
         num = self.contador-1
         colum = self.columna-1
         fil = self.fila
         self.char  = self.texto[self.contador]
         while(not self.char=='\''):
            self.cadena+=self.char
            self.contador+=1
            self.columna+=1
            self.char  = self.texto[self.contador]
         self.q13=True
         self.guardar("SIM_COMILLA",self.char)
         self.guardar("CADENA",self.cadena)
         self.guardar("SIM_COMILLA",self.char)
         self.cadena=""
      except:
         self.contador=num
         self.columna= colum
         self.fila=fil
         self.cadena='\''
         self.errorLexico(self.cadena,self.columna+1,self.fila)
   
   def guardar(self, texto,val):
      print (texto +" : "+val)
      self.lista_token.append(Token(texto,val))

   def errorLexico(self,texto,x,y):
      print ("ERROR LEXICO" +" : "+texto)
      self.lista_pos_error.append(self.contador)
      self.cadena = ""
      self.lista_errores.append(Error(x,y,"Cadena no reconocida: "+texto))

   


      
