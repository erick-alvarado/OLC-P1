from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
from tkinter.ttk import LabelFrame

root = Tk()
root.title("Proyecto 1")
archivo = ""

def new():
    global archivo
    editor.delete(1.0, END)
    archivo = ""

def openFile():
    global archivo
    try:

        archivo = filedialog.askopenfilename(title = "Abrir Archivo", initialdir = "C:/")

        entrada = open(archivo)
        content = entrada.read()

        editor.delete(1.0, END)
        editor.insert(INSERT, content)
        entrada.close()
    except:
        print("-Ha ocurrido un error en abrir")

def logout():
    value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
    if value :
        root.destroy()

def saveFile():
    global archivo
    try:
        if archivo == "":
            saveAs()
        else:
            guardarc = open(archivo, "w")
            guardarc.write(editor.get(1.0, END))
            guardarc.close()
    except:
        print("-Ha ocurrido un error en abrir")
    
def saveAs():
    global archivo
    try:

        guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = "C:/")
        fguardar = open(guardar, "w+")
        fguardar.write(editor.get(1.0, END))
        fguardar.close()
        archivo = guardar
    except:
        print("-Ha ocurrido un error en guardar como")


barraMenu = Menu(root)
root.config(menu = barraMenu, width = 1000, height = 600)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label = "Nuevo", command = new)
archivoMenu.add_command(label = "Abrir", command = openFile)
archivoMenu.add_command(label = "Guardar", command = saveFile)
archivoMenu.add_command(label = "Guardar Como...", command = saveAs)
archivoMenu.add_separator()
archivoMenu.add_command(label = "Salir", command = logout)

barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
barraMenu.add_command(label = "Salir",  command = logout)

lbl = Label(root, text="Analizador lexico", font=("Arial", 20))
lbl.pack(side="top",pady = 20)

frame = LabelFrame(root, text = 'Texto de entrada')
frame.pack(side = "left",pady = 20, padx = 20)

frame2 = LabelFrame(root, text = 'Consola')
frame2.pack(side = "right",pady = 20,padx = 20)

editor = scrolledtext.ScrolledText(frame,width=50,height=25)
editor.pack(side = "left")
consola = scrolledtext.ScrolledText(frame2,width=50,height=25)
consola.pack(side = "right")

btn = Button(root, text="Analizar")
btn.pack(side = "top",pady = 200)

root.mainloop()