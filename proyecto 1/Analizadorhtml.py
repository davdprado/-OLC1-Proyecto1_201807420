from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from Error import Error
from Token import Token

listaToken=list()

listaErrorH=list()
conta=0
Palhtml=['html','head','title','body','h1','h2','h3','h4','h5','h6','p','br','src','a','href','ul','ol','li','style','table','th','tr','td','caption','colgroup','col','thead','tbody','tfoot']
Palhtml = set(Palhtml)
def es_Reservada(lexema):
    for pl in Palhtml:
        if lexema==pl:
            return True

def Estados_iniciales(caract,fil,col,consola,idError):
    if caract.isalnum():
        return 1
    elif caract.isdigit():
        return 2
    elif caract=='<':
        return 5
    elif caract=='>':
        consola.insert(END,caract+" simbolo \n")
        return 0
    elif caract=='=':
        consola.insert(END,caract+" simbolo \n")
        return 0
    elif caract=='"':
        return 12
    elif caract=="'":
        return 15
    elif caract=='.':
        consola.insert(END,caract+" simbolo \n")
        return 0
    elif caract=='/':
        consola.insert(END,caract+" simbolo \n")
        return 0
    elif (caract=='\n' or caract==' ' or caract=='\t'):
        return 0
    else:
        consola.insert(END,caract+" No pertenece \n")
        NuevoError=Error(idError,fil,col,"El Caracter "+caract+" no pertenece al lenguaje")
        idError=idError+1
        listaErrorH.append(NuevoError)
        estado=0



def AnalisisHTML(txt1,consola):
    fila=1
    columna=0
    idError=0
    estado=0
    ruta=False
    lexema=""
    conta=0
    continuar=False
    cerrar=False
    contenido=txt1.get("1.0","end-1c")
    contenido = contenido.lower()
    for caracter in contenido:
        columna=columna+1
        if caracter=='\n':
            fila=fila+1
            columna=0
        if estado==0:
            estado=Estados_iniciales(caracter,fila,columna,consola,idError)
        if estado==1:
            if caracter.isalnum():
                lexema=lexema+caracter
                estado=1
            else:
                if es_Reservada(lexema):
                    consola.insert(END,lexema + " Es una palabra reservada\n")
                    lexema=""
                else:
                    consola.insert(END,lexema + " Es una identificador\n")
                    lexema=""
                estado=Estados_iniciales(caracter,fila,columna,consola,idError)
                lexema=lexema+caracter
        elif estado==2:
            if caracter.isdigit():
                lexema=lexema+caracter
                estado=2
            else:
                if caracter!='.':
                    consola.insert(END,lexema + " Entero\n")
                    lexema=""
                    estado=Estados_iniciales(caracter,fila,columna,consola,idError)
                else:
                    lexema=lexema+caracter
                    estado=3
        elif estado==3:
            lexema=lexema+caracter
            estado=4

        elif estado==4:
            if caracter.isdigit():
                lexema=lexema+caracter
                estado=4
            else:
                consola.insert(END,lexema + " Decimal\n")
                lexema=""
                estado=Estados_iniciales(caracter,fila,columna,consola,idError)
        
        elif estado==5:
            lexema=lexema+caracter
            estado=6
        elif estado==6:
            if caracter=='!':
                lexema=lexema+caracter
                estado=7
            else:
                NuevoToken=Token(conta,fila,columna,lexema)
                conta=conta+1
                listaToken.append(NuevoToken)
                consola.insert(END,lexema+" signo < solo \n")
                lexema=""
                estado=Estados_iniciales(caracter,fila,columna,consola,idError)
                lexema=lexema+caracter
        elif estado==7:
            if caracter=='-':
                lexema=lexema+caracter
                estado=8
            else:
                NuevoToken=Token(conta,fila,columna,lexema)
                conta=conta+1
                listaToken.append(NuevoToken)
                consola.insert(END,caracter+" simbolo \n")
                lexema=""
                estado=Estados_iniciales(caracter,fila,columna,consola,idError)
        elif estado==8:
            if caracter=='-':
                lexema=lexema+caracter
                estado=9
            else:
                NuevoToken=Token(conta,fila,columna,lexema)
                conta=conta+1
                listaToken.append(NuevoToken)
                consola.insert(END,caracter+" algo \n")
                lexema=""
                estado=Estados_iniciales(caracter,fila,columna,consola,idError)
        elif estado==9:
            if caracter!='-':
                lexema=lexema+caracter
            else:
                if lexema[-2]=='-' and lexema[-1]=='-':
                    lexema=lexema+caracter
                    estado=10
        elif estado==10:
            if caracter!='>':
                lexema=lexema+caracter
                estado=9
            else:
                lexema=lexema+caracter
                NuevoToken=Token(conta,fila,columna,lexema)
                conta=conta+1
                listaToken.append(NuevoToken)
                consola.insert(END,lexema+" comentario largo \n")
                print(lexema)
                lexema=""
                estado=0
        elif estado==12:
            if(caracter=='"' and cerrar==True):
                lexema=lexema+caracter
                estado=13
                continuar=False
                cerrar=False
            else:
                lexema=lexema+caracter
                estado=12
                continuar=True
                cerrar=True
        elif estado==13:
            NuevoToken=Token(conta,fila,columna,lexema)
            conta=conta+1
            listaToken.append(NuevoToken)
            consola.insert(END,lexema+" cadena \n")
            lexema=""
            estado=Estados_iniciales(caracter,fila,columna,consola,idError)
            lexema=lexema+caracter
        
        elif estado==15:
            if(caracter=="'" and cerrar==True):
                lexema=lexema+caracter
                estado=16
                continuar=False
                cerrar=False
            else:
                lexema=lexema+caracter
                estado=15
                continuar=True
                cerrar=True
        elif estado==16:
            NuevoToken=Token(conta,fila,columna,lexema)
            conta=conta+1
            listaToken.append(NuevoToken)
            consola.insert(END,lexema+" cadena \n")
            lexema=""
            estado=Estados_iniciales(caracter,fila,columna,consola,idError)
            lexema=lexema+caracter

                
        
        
 

