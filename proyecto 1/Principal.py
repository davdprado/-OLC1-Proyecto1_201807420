from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from Analizadorjs import AnalizadorLexicoJS
from Analizadorjs import listaError
from Analizadorjs import listaToken
from Analizadorhtml import AnalisisHTML
from crearhtml import crearRH
from Analizadorhtml import listaErrorH
from Analizadorcss import AnalizadorLexicoCss
from Analizadorcss import listaErrorC
from Analizadorjs import listaTransicion
from AnalizadorOpe import AnalizarOpe
import os.path
import os

extension=""
RutaP=""
def cerrar():
    Ventana_principal.destroy()

def BorrarDatos():
    global listaError,listaToken,listaErrorH,listaErrorC,listaTransicion,extension
    listaError=[]
    listaErrorC=[]
    listaErrorH=[]
    listaToken=[]
    listaTransicion=[]
    extension=""
    text1.delete("1.0","end")
    text2.delete("1.0","end")

def Graficar():
    dot= open('imagen.dot','w')
    dot.writelines('digraph G{ \n')
    for tar in listaTransicion:
        dot.writelines(str(tar.EstadoInicial)+'->'+str(tar.EstadoFinal)+'[label="'+tar.Trans+'"];\n')
    dot.writelines('}')
    dot.close()
    print("probando")
    comando="dot -Tpng imagen.dot -o arbol.png"
    print(os.system(comando))
    comando2="arbol.png"
    print(os.system(comando2))


def abrir_archivo():
    BorrarDatos()
    global RutaP
    archivo_abierto=filedialog.askopenfilename( title='Abrir Archivo', initialdir='C:/Users/Roberto/Documents/entradas',filetypes=(("all files",".*"),("css files",".css"),("html files",".html"),("js files",".js")))
    ruta=archivo_abierto
    if ruta !="":
        arch=open(ruta,'r')
        lectura=arch.read()
        text1.insert("1.0",lectura)
        arch.close()
    global extension
    extension=os.path.splitext(ruta)[1]
    if (extension==".rmt"):
        print("ruta")
    else:
        texto=text1.get("1.0","end-1c")
        texto = texto.split('\n')
        consu=0
        bus=""
        rutita=""
        esWin=False
        for linea in texto:
            for c in linea:
                bus=bus+c
                if bus[-1]==":" and bus[-2]=="W":
                    esWin=True
                elif esWin==True:
                    rutita=rutita+c
            esWin=False
            bus=""
            consu=consu+1
            if consu==2:
                break
        rutita=rutita.replace(" '","")
        rutita=rutita.replace("'","")
        print("la ruta es: "+rutita)
        os.makedirs(rutita,exist_ok=True)
        RutaP=rutita

        

def Nuevo_archivo():
    BorrarDatos()

def Guardar_archivo():
    guardar_archivo=filedialog.asksaveasfile(title='Guardar Archivo', initialdir=RutaP,defaultextension=".html",filetypes=(("html files",'.html'),("css files",".css")))

    
def Analizar():
    if(extension=='.js'):
        AnalizadorLexicoJS(text1,text2)
        crearRH(listaError)
        comando2="errores.html"
        print(os.system(comando2))
        Graficar()
    elif(extension=='.css'):
        AnalizadorLexicoCss(text1,text2)
        crearRH(listaErrorC)
        comando2="errores.html"
        print(os.system(comando2))
    elif (extension=='.html'):
        AnalisisHTML(text1,text2)
        crearRH(listaErrorH)
        comando2="errores.html"
        print(os.system(comando2))
    else:
        AnalizarOpe(text1,text2)
        print("Estension desconocida")

    



Ventana_principal=Tk()
Ventana_principal.title("[OLC1]Proyecto1")

#-------------------------Barra de navegacion
menu=Menu(Ventana_principal)
new_item=Menu(menu)
new_item.add_command(label='Nuevo',command=Nuevo_archivo)
new_item.add_command(label='Abrir',command=abrir_archivo)
new_item.add_command(label='Guardar',command=Guardar_archivo)
new_item.add_command(label='Guardar Como...',comman=Graficar)
new_item.add_command(label='Analizar',command=Analizar)
new_item.add_separator()
new_item.add_command(label='Salir')
menu.add_cascade(label='Archivo',menu=new_item)
menu.add_cascade(label='Ayuda')
Ventana_principal.config(menu=menu)
#-------------------------------------Panel donde estara todo
frame = LabelFrame(Ventana_principal, text = 'Analizador Lexico')
frame.grid(row=0,column=0,columnspan=8,pady=20)

text1 = Text(frame,width=90,height=20)
text1.grid(column=0,row=0) 

text2 =Text(frame,width=80,height=10,bg="black",fg="white")
text2.grid(column=0,row=20)
        
        



Ventana_principal.mainloop()



