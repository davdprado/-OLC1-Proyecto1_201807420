from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from Error import Error
from Token import Token

PLRCS=['px','pc','pt','em','vh','vw','in','cm','mm','color','background-color','background','image','border','opacity','background','text','align','font','family','font','size','font','weight','font','style','font','padding','left','padding','right','padding','bottom','padding','padding','top','display','line','height','width','height','margin','top','margin','border','style','position','bottom','top','left','right','float','clear','max','width','min','width','max','height','min','height']


listaErrorC=list()
listaToken=list()

def es_Reservada(lexema):
    for pl in PLRCS:
        if lexema==pl:
            return True

def Estados_iniciales(caract,fil,col,consola,idError):
    if caract.isdigit():
        return 2
    elif caract.isalnum():
        return 1
    elif caract=='#':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract=='.':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract==';':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract==':':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract=='{':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract=='}':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract=='(':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract==')':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract==',':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract=='*':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract=='-':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract=='%':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract=='"':
        return 12
    elif caract=='/':
        return 5
    elif caract=="'":
        return 15
    elif (caract=='\n' or caract==' ' or caract=='\t'):
        return 0
    else:
        consola.insert(END,caract+" No pertenece \n")
        NuevoError=Error(idError,fil,col,"El Caracter "+caract+" no pertenece al lenguaje")
        idError=idError+1
        listaErrorC.append(NuevoError)
        return 0

def AnalizadorLexicoCss(txtcont,consola):
    lexema=""
    columna=0
    fila=1
    cerrar=False
    continuar=False
    conta=0
    idError=0
    estado=0
    contadorcito=0
    rutita=""
    lex=""
    contenido= txtcont.get("1.0","end-1c")
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
        elif estado==2:
            if caracter.isdigit():
                lexema=lexema+caracter
                estado=2
            else:
                if caracter!='.':
                    consola.insert(END,lexema+" numero \n")
                    lexema=""
                    estado=Estados_iniciales(caracter,fila,columna,consola,idError)
                    lexema=lexema+caracter
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
                consola.insert(END,lexema+" es decimal \n")
                lexema=""
                estado=Estados_iniciales(caracter,fila,columna,consola,idError)
        elif estado==5:
            lexema=lexema+caracter
            estado=6
        elif estado==6:
            if caracter=='/' or caracter=='*':
                if caracter=='*':
                    lexema=lexema+caracter
                    estado=8
            else:
                consola.insert(END,caracter+" No pertenece \n")
                NuevoError=Error(idError,fila,columna,"El Caracter "+caracter+" no pertenece al lenguaje")
                idError=idError+1
                listaErrorC.append(NuevoError)
                estado=Estados_iniciales(caracter,fila,columna,consola,idError)
        elif estado==8:
            if caracter!='*':
                lexema=lexema+caracter
            else:
                lexema=lexema+caracter
                estado=9
        elif estado==9:
            if caracter!='/':
                lexema=lexema+caracter
                estado=8
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