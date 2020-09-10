
from enum import Enum
from Token import Token
from Error import Error


class lexicoCss:
   

   lenguaje = {
      "color":"PROPIEDAD_COLOR",
      "content":"PROPIEDAD_CONTENT",
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
      "center": "VAL_ID_CENTER" ,
      "absolute": "VAL_ID_ABSOLUTE" ,
      "inline-bloack": "VAL_ID_INLINE_BLOCK" ,
      "solid": "VAL_ID_SOLID" ,

      "red": "VAL_COLOR_RED" ,
      "purple": "VAL_COLOR_PURPLE" ,
      "yellow": "VAL_COLOR_YELLOW" ,
      "gray": "VAL_COLOR_GRAY" ,
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
      "{": "SIM_ABRIR_CORCHETES" ,
      "}": "SIM_CERRAR_CORCHETES" ,
      "#": "SIM_HASHTAG" ,


   }
   #"CADENA_TEXTO"
   #"NUMERO"
   #"ID"
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


   def analizarCss(self,txt):
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
            print("S0->S5")
            self.cadena+=self.char
            nombre = self.lenguaje.get(self.cadena)
            self.guardar(nombre,self.cadena)
            self.cadena=""
            self.contador+=1
            self.columna+=1
            self.estadoCaracter2()
         elif self.char=='/' :
            print("S0->S8")
            try:   
               self.contador+=1
               self.columna+=1
               self.char  = self.texto[self.contador]
               if(self.char == '*'):
                  print("S8->S3")
                  self.contador+=1
                  self.columna+=1
                  self.estadoCaracter()
               else:
                  self.errorLexico("/",self.columna,self.fila)
                  self.contador-=1
            except:
               self.errorLexico("/",self.columna,self.fila)
               a = 0

         elif not self.lenguaje.get(self.char) == None:
            print("S0->S1")
            self.cadena+=self.char
            nombre = self.lenguaje.get(self.cadena)
            self.guardar(nombre,self.cadena)
            self.cadena=""

         elif self.char.isalpha() or self.char=="-":
            print("S0->S2")
            self.cadena+=self.char
            self.contador+=1
            self.columna+=1
            self.estadoLetra()
         elif self.char.isnumeric():
            print("S0->S4")
            self.cadena+=self.char
            self.estadoNumero()
         else:
            self.cadena+=self.char
            self.errorLexico(self.cadena,self.columna,self.fila)


   def estadoLetra(self):

      self.char  = self.texto[self.contador]
      while(self.char.isalpha() or self.texto[self.contador]=="-"):
         self.cadena+=self.char
         self.contador+=1
         self.columna+=1
         self.char  = self.texto[self.contador]

      if self.texto[self.contador].isdigit():
         print("S2->S4")
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
      self.columna+=1
      self.char  = self.texto[self.contador]
      while(self.char.isnumeric()):
         self.cadena+=self.char
         self.contador+=1
         self.columna+=1
         self.char  = self.texto[self.contador]
         
      self.contador-=1
      a =self.cadena.isdigit()
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
         self.guardar("SIM_BARRA","/")
         self.guardar("SIM_ASTERISCO","*")
         self.guardar("COMENTARIO",self.cadena)
         print("S3->S9")
         self.guardar("SIM_ASTERISCO","*")
         print("S9->S7")
         self.guardar("SIM_BARRA","/")
         self.cadena=""

         self.contador+=1
      except:
         self.errorLexico("/",self.columna,self.fila)
         self.errorLexico("*",self.columna,self.fila)
         self.contador=num
         self.cadena=""
      
      
   
   def estadoCaracter2(self):
      self.char  = self.texto[self.contador]
      while(not self.char=='\"'):
         self.cadena+=self.char
         self.contador+=1
         self.columna+=1
         self.char  = self.texto[self.contador]
      print("S5->S6")
      self.guardar("CADENA",self.cadena)
      self.guardar("SIM_COMILLA",self.char)
      self.cadena=""


   def guardar(self, texto,val):
      print (texto +" : "+val)
      self.lista_token.append(Token(texto,val))

   def errorLexico(self,texto,x,y):
      print ("ERROR LEXICO" +" : "+texto)
      self.lista_pos_error.append(self.contador)
      self.cadena = ""
      self.lista_errores.append(Error(x,y,"Cadena no reconocida: "+texto))
   
   
   


      