from enum import Enum
from Token import Token
from Error import Error

class lexicoCss:
   
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
      "top": "PROPIEDAD_TOP" ,
      "right": "PROPIEDAD_RIGHT" ,
      "left": "PROPIEDAD_LEFT" ,
      "float": "PROPIEDAD_FLOAT" ,
      "clear": "PROPIEDAD_CLEAR" ,
      "max-width": "PROPIEDAD_MAX_WIDTH" ,
      "max-height": "PROPIEDAD_MAX_HEIGHT" ,
      "min-width": "PROPIEDAD_MIN_WIDTH" ,
      "min-height": "PROPIEDAD_MIN_HEIGHT" ,
      "px": "VAL_UNIDAD_PX" ,
      "em": "VAL_UNIDAD_EM" ,
      "vh": "VAL_UNIDAD_VH" ,
      "vw": "VAL_UNIDAD_VW" ,
      "in": "VAL_UNIDAD_IN" ,
      "cm": "VAL_UNIDAD_CM" ,
      "mm": "VAL_UNIDAD_MM" ,
      "pt": "VAL_UNIDAD_PT" ,
      "pc": "VAL_UNIDAD_PC" ,

      "relative": "VAL_ID_RELATIVE" ,
      "inline-bloack": "VAL_ID_INLINE_BLOCK" ,

      "red": "VAL_COLOR_RED" ,
      "rgba": "VAL_COLOR_RGBA" ,

      "%": "SIM_PORCENTAJE" ,
      "(": "SIM_ABRIR_PARENTESIS" ,
      ")": "SIM_CERRAR_PARENTESIS" ,
      ";": "SIM_PUNTO_COMA" ,
      ":": "SIM_DOS_PUNTOS" ,
      ",": "SIM_COMA" ,
      ".": "SIM_PUNTO" ,
      "-": "SIM_MENOS" ,
      "\"": "SIM_COMILLA" ,
      "/": "SIM_BARRA" ,
      "*": "SIM_ASTERISCO" ,
      "{": "SIM_ABRIR_CORCHETES" ,
      "}": "SIM_CERRAR_CORCHETES" ,
      "#": "SIM_HASHTAG" ,


   }
   #"CADENA_TEXTO"
   #"NUMERO"
   #"ID"
   #"COMENTARIO"

 

   def analizarCss(self,txt):
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
      
      print(str1)     
      return str1







   def estadoLetra(self):

      if(self.texto[self.contador-2]=="*"and self.texto[self.contador-3]=="/"):
         self.estadoCaracter()
      else:
            
         self.char  = self.texto[self.contador]
         while(self.char.isalpha() or self.texto[self.contador]=="-"):
            self.cadena+=self.char
            self.contador+=1
            self.char  = self.texto[self.contador]

         if self.texto[self.contador].isdigit():
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
      if(self.cadena.isdigit):
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


   def guardar(self, texto,val):
      print (texto +" : "+val)
      self.lista_token.append(Token(texto,val))

   def errorLexico(self,texto,x,y):
      print ("ERROR LEXICO" +" : "+texto)
      self.lista_pos_error.append(self.contador)
      self.cadena = ""
      self.lista_errores.append(Error(x,y,"Cadena no reconocida: "+texto))

   


      