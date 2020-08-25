class Error:
    posicion_x = 0
    posicion_y = 0
    texto =""
    def __init__(self,x,y,txt):
        self.posicion_x=x
        self.posicion_y=y
        self.texto=txt