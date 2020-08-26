from enum import Enum
from Token import Token
from Error import Error

class lexicoHtml:
   
   fila = 1
   columna = 0
   cadena = ""
   contador =-1
   char = ''
   texto = ""
   lista_token = []
   lista_errores =[]

   lenguaje = {
      "color":"PROPIEDAD_COLOR",
      "background-color":"PROPIEDAD_BACKGROUND_COLOR",
      "background-image":"PROPIEDAD_BACKGROUND_IMAGE",
      "border":"PROPIEDAD_BORDER"  ,
      "opacity":"PROPIEDAD_OPACITY"  ,
      "background":"PROPIEDAD_BACKGROUND",
      "text-align":"PROPIEDAD_TEXT_ALIGN" ,
      "font-weight": "PROPIEDAD_FONT_WEIGHT" ,
      "font-family": "PROPIEDAD_FONT_FAMILY" ,
      "font-style": "PROPIEDAD_FONT_STYLE" ,
      "font-size": "PROPIEDAD_FONT_SIZE" ,
      "font": "PROPIEDAD_FONT" ,
      "padding": "PROPIEDAD_PADDING" ,
      "padding-left": "PROPIEDAD_PADDING_LEFT" ,
      "padding-right": "PROPIEDAD_PADDING_RIGHT" ,
      "padding-bottom": "PROPIEDAD_PADDING_BOTTOM" ,
      "padding-top": "PROPIEDAD_PADDING_TOP" ,
      "display": "PROPIEDAD_DISPLAY" ,
      "line-height": "PROPIEDAD_LINE_HEIGHT" ,
      "width": "PROPIEDAD_WIDTH" ,
      "height": "PROPIEDAD_HEIGHT" ,
      "margin": "PROPIEDAD_MARGIN" ,
      "margin-top": "PROPIEDAD_MARGIN_TOP" ,
      "margin-right": "PROPIEDAD_MARGIN_RIGHT" ,
      "margin-bottom": "PROPIEDAD_MARGIN_BOTTOM" ,
      "margin-left": "PROPIEDAD_MARGIN_LEFT" ,
      "border-style": "PROPIEDAD_BODER_STYLE" ,
      "display": "PROPIEDAD_DISPLAY" ,
      "position": "PROPIEDAD_POSITION" ,
      "bottom": "PROPIEDAD_BOTTOM" ,

      "h1": "PR_H1",
      "h2": "PR_H2",
      "h3": "PR_H3" ,
      "h4": "PR_H4" ,
      "h5": "PR_H5",
      "h6": "PR_H6" ,

      "p": "PR_P",
      "br": "PR_BR" ,
      "img": "PR_IMG" ,
      "src": "PR_SRC" ,
      "a": "PR_A" ,
      "href": "PR_HREF" ,

      "ul": "PR_UL"  ,
      "li": "PR_LI",

      "style": "PR_STYLE" ,

      "table": "PR_TABLE" ,
      "th": "PR_TH"   ,
      "tr": "PR_TR" ,
      "td": "PR_TD" ,

      "caption": "PR_CAPTION" ,
      "colgroup": "PR_COLGROUP",
      "col": "PR_COL" ,

      "thead": "PR_THEAD" ,
      "tbody": "PR_TBODY" ,
      "tfoot": "PR_TFOOT",

      "color": "PR_COLOR",
      "font": "PR_FONT",
      "size" : "PR_SIZE",
      "px" : "PR_PX",
      "border" : "PR_BORDER",

      "<": "SIM_ABRE_GUION" ,
      ">": "SIM_CIERRA_GUION",
      "/": "SIM_BARRA" ,
      "\'": "SIM_COMILLA",
      "\"": "SIM_COMILLA_DOBLE" ,
      "=": "SIM_IGUAL" ,
   }
   #"CADENA_TEXTO"
   #"NUMERO"
   

 

   def analizarHTML(self,txt):
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
         
         elif not self.lenguaje.get(self.char) == None:
            self.cadena+=self.char
            nombre = self.lenguaje.get(self.cadena)
            self.guardar(nombre,self.cadena)
            self.cadena=""

         elif self.char.isalpha():
            self.cadena+=self.char
            self.contador+=1
            self.estadoLetra()
         elif self.char.isnumeric():
            self.cadena+=self.char
            self.estadoNumero()
         else:
            self.cadena+=self.char
            self.errorLexico(self.cadena,self.columna,self.fila)






   def estadoLetra(self):

      if(self.texto[self.contador-2]=="\""or self.texto[self.contador-2]=="\'" or self.texto[self.contador-2]==">"):
         self.estadoCaracter()

      else:
            
         self.char  = self.texto[self.contador]
         if(self.char.isnumeric() and self.texto[self.contador-1]=='h'):
            self.cadena+=self.char
         else:
            while(self.char.isalpha()):
               self.cadena+=self.char
               self.contador+=1
               self.char  = self.texto[self.contador]
               
            self.contador-=1
         
         nombre = self.lenguaje.get(self.cadena)
         if(not nombre==None):
            self.guardar(nombre,self.cadena)
         else:
            self.errorLexico(self.cadena,self.columna,self.fila)

      self.cadena=""
      
      
   def estadoNumero(self):
      self.contador+=1
      self.char  = self.texto[self.contador]
      while(self.char.isnumeric()):
         self.cadena+=self.char
         self.contador+=1
         self.char  = self.texto[self.contador]
         
      
      self.guardar("NUMERO",self.cadena)
      self.cadena=""
      self.contador-=1

   def estadoCaracter(self):
      self.char  = self.texto[self.contador]
      while(not self.char=="<" and not self.char=="\""and not self.char=="\'"):
         self.cadena+=self.char
         self.contador+=1
         self.char  = self.texto[self.contador]
         
      
      self.guardar("CADENA_TEXTO",self.cadena)
      self.cadena=""
      self.contador-=1


   def guardar(self, texto,val):
      print (texto +" : "+val)
      self.lista_token.append(Token(texto,val))

   def errorLexico(self,texto,x,y):
      print ("ERROR LEXICO" +" : "+texto)
      self.cadena = ""
      self.lista_errores.append(Error(x,y,"Cadena no reconocida: "+texto))

   


      