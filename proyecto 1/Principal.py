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
import os.path
import os

extension=""
RutaP=""



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


def abrir_archivo():
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
    #aqui va el algoritmo para eso
    print("")

def Guardar_archivo():
    guardar_archivo=filedialog.asksaveasfile(title='Guardar Archivo', initialdir=RutaP,defaultextension=".html",filetypes=(("html files",'.html'),("css files",".css")))
    if(extension=='.js'):
        crearRH(listaError,guardar_archivo)
        print(guardar_archivo)
    elif(extension=='.css'):
        crearRH(listaErrorC,guardar_archivo)
    elif (extension=='.html'):
        crearRH(listaErrorH,guardar_archivo)
    else:
        print("Estension desconocida")
    

    
def Analizar():
    listaError=list()
    listaToken=list()
    if(extension=='.js'):
        AnalizadorLexicoJS(text1,text2)
    elif(extension=='.css'):
        AnalizadorLexicoCss(text1,text2)
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



