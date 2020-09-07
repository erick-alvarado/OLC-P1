from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
from tkinter.ttk import LabelFrame
from LexicoHtml import lexicoHtml
from LexicoCss import lexicoCss
from LexicoJs import lexicoJs

class GUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Proyecto 1")
        self.archivo = ""

        self.lexHTML = lexicoHtml()
        self.lexCSS = lexicoCss()
        self.lexJs = lexicoJs()

        self.barraMenu = Menu(self.root)
        self.root.config(menu=self.barraMenu, width=1000, height=600)

        self.archivoMenu = Menu(self.barraMenu, tearoff=0)
        self.archivoMenu.add_command(label="Nuevo", command=self.new)
        self.archivoMenu.add_command(label="Abrir", command=self.openFile)
        self.archivoMenu.add_command(label="Guardar", command=self.saveFile)
        self.archivoMenu.add_command(label="Guardar Como...", command=self.saveAs)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Salir", command=self.logout)

        self.barraMenu.add_cascade(label="Archivo", menu=self.archivoMenu)
        self.barraMenu.add_command(label="Salir",  command=self.logout)

        self.lbl = Label(self.root, text="Analizador lexico", font=("Arial", 20))
        self.lbl.pack(side="top", pady=20)

        self.frame = LabelFrame(self.root, text='Texto de entrada')
        self.frame.pack(side="left", pady=20, padx=20)

        self.frame2 = LabelFrame(self.root, text='Consola')
        self.frame2.pack(side="right", pady=20, padx=20)

        self.editor = scrolledtext.ScrolledText(self.frame, width=90, height=25)
        self.editor.pack(side="left")
        self.consola = scrolledtext.ScrolledText(self.frame2, width=50, height=25)
        self.consola.pack(side="right")

        self.btn = Button(self.root, text="Analizar", command=self.iniciarAnalisis)
        self.btn.pack(side="top", pady=200)

        self.root.mainloop()

    def new(self):
        self.archivo
        self.editor.delete(1.0, END)
        self.archivo = ""

    def iniciarAnalisis(self):
        if(self.tipoArchivo=="html"):
            self.lexHTML.analizarHTML(self.editor.get('1.0', 'end-1c'))
            self.editor.delete(1.0, END)
            self.editor.insert(INSERT, self.lexHTML.textoFinal())
            
        if(self.tipoArchivo=="css"):
            self.lexCSS.analizarCss(self.editor.get('1.0', 'end-1c'))
            self.editor.delete(1.0, END)
            self.editor.insert(INSERT, self.lexCSS.textoFinal())
            
        if(self.tipoArchivo=="js"):
            self.lexJs.analizarJs(self.editor.get('1.0', 'end-1c'))
            self.editor.delete(1.0, END)
            self.editor.insert(INSERT, self.lexJs.textoFinal())
        self.generateTable()
            


    def openFile(self):
        self.archivo
        try:
            self.archivo = filedialog.askopenfilename(
                title="Abrir Archivo", initialdir="C:/")

            a = self.archivo.split(".")
            for x in a :
                self.tipoArchivo = x 
            
            self.entrada = open(self.archivo)
            self.content = self.entrada.read()

            self.editor.delete(1.0, END)
            self.editor.insert(INSERT, self.content)
            self.entrada.close()
        except:
            print("-Ha ocurrido un error en abrir")

    def logout(self):
        value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
        if value:
            self.root.destroy()

    def saveFile(self):
        self.archivo
        try:
            if self.archivo == "":
                self.saveAs()
            else:
                guardarc = open(archivo, "w")
                guardarc.write(self.editor.get(1.0, END))
                guardarc.close()
        except:
            print("-Ha ocurrido un error en abrir")
            
    def saveAs(self):
        self.archivo
        try:

            guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = "C:/")
            fguardar = open(guardar, "w+")
            fguardar.write(self.editor.get(1.0, END))
            fguardar.close()
            archivo = guardar
        except:
            print("-Ha ocurrido un error en guardar como")    

    def generateTable(self):
        l = None
        if(self.tipoArchivo=="html"):
            l = self.lexHTML.lista_errores
        if(self.tipoArchivo=="css"):
            l = self.lexCSS.lista_errores
        if(self.tipoArchivo=="js"):
            l = self.lexJs.lista_errores
        
        html  = "<!DOCTYPE html> <html> <head> <title>Errores lexicos</title> </head> <body> REPLACE </body> </html>"
        
        table = "<table> <tr> <th> Nombre</th> <th>Fila</th><th>Columna</th></tr>REPLACE</table>"
        var = ""
        for x in l:
            pos1 = str(x.posicion_y)
            pos2= str(x.posicion_x)
            var+= "<tr> <th>"+x.texto+"</th> <th>"+pos1+"</th><th>"+pos2+"</th></tr>"

        table = table.replace("REPLACE",var)
        html = html.replace("REPLACE",table)

        if(not l == None):
            self.archivo
            try:

                guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = "C:/")
                fguardar = open(guardar, "w+")
                fguardar.write(html)
                fguardar.close()
                archivo = guardar
            except:
                print("-Ha ocurrido un error en guardar como")  


start = GUI()