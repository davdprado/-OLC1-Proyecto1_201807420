from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from Analizadorjs import AnalizadorLexicoJS
from Analizadorjs import listaError
from Analizadorjs import listaToken
from Analizadorhtml import AnalisisHTML
import os.path

extension=""


def abrir_archivo():
    archivo_abierto=filedialog.askopenfilename( title='Abrir Archivo', initialdir='/home/roberto/Escritorio/Entradas',filetypes=(("all files",".*"),("css files",".css")))
    ruta=archivo_abierto
    if ruta !="":
        arch=open(ruta,'r')
        lectura=arch.read()
        text1.insert("1.0",lectura)
        arch.close()
    global extension
    extension=os.path.splitext(ruta)[1]

        

def Nuevo_archivo():
    #aqui va el algoritmo para eso
    print("")

def Guardar_archivo():
    #aqui va el algoritmo para eso
    print("algo")

    
def Analizar():
    listaError=list()
    listaToken=list()
    if(extension=='.js'):
        AnalizadorLexicoJS(text1,text2)
    elif(extension=='.css'):
        print("analizar css")
    elif (extension=='.html'):
        AnalisisHTML(text1,text2)
    else:
        print("Estension desconocida")

    



Ventana_principal=Tk()
Ventana_principal.title("[OLC1]Proyecto1")

#-------------------------Barra de navegacion
menu=Menu(Ventana_principal)
new_item=Menu(menu)
new_item.add_command(label='Nuevo')
new_item.add_command(label='Abrir',command=abrir_archivo)
new_item.add_command(label='Guardar',command=Guardar_archivo)
new_item.add_command(label='Guardar Como...')
new_item.add_command(label='Analizar',command=Analizar)
new_item.add_separator()
new_item.add_command(label='Salir')
menu.add_cascade(label='Archivo',menu=new_item)
menu.add_cascade(label='Ayuda')
Ventana_principal.config(menu=menu)
#-------------------------------------Panel donde estara todo
frame = LabelFrame(Ventana_principal, text = 'Analizador Lexico')
frame.grid(row=0,column=0,columnspan=8,pady=20)

text1 = Text(frame,width=80,height=30)
text1.grid(column=0,row=0) 

text2 =Text(frame,width=60,height=20,bg="black",fg="white")
text2.grid(column=80,row=0)
        
        



Ventana_principal.mainloop()



