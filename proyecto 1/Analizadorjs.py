from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from Error import Error
from Token import Token
from Token import Transiciones
import os


listaToken=list()
listaError=list()
listaTransicion=list()
columna=0
estado=0
fila=0
continuar=False
cerrar=False
idError=0
conta=0

PalResJs =['int','var','string','char','boolean','if','for','while','do','continue','break','return','function','this','class','Math','pow']

def existeT(listat,tr,e,ee):
    for ta in listat:
        if ta.Trans==tr and ta.EstadoInicial==e and ta.EstadoFinal==ee:
            return False
    return True

def es_Reservada(lexema):
    for pl in PalResJs:
        if lexema==pl:
            return True
    

def EstadosIniciales(est,caracter,idError,fila,columna,consola):
    if caracter.isdigit():
        if existeT(listaTransicion,"D",est,2):
            NuevaT=Transiciones("D",est,2)
            listaTransicion.append(NuevaT)
        return 2
    elif caracter.isalnum():
        if existeT(listaTransicion,"L",est,1):
            NuevaT=Transiciones("L",est,1)
            listaTransicion.append(NuevaT)
        return 1
    elif caracter=='"':
        if existeT(listaTransicion,'cs',0,12):
            NuevaT=Transiciones('cs',0,12)
            listaTransicion.append(NuevaT)
        return 12
    elif caracter=="'":
        if existeT(listaTransicion,"'",0,15):
            NuevaT=Transiciones("'",0,15)
            listaTransicion.append(NuevaT)
        return 15
    elif caracter=='(':
        consola.insert(END,caracter+" simbolo \n")
        if existeT(listaTransicion,'(',0,11):
            NuevaT=Transiciones("(",0,11)
            listaTransicion.append(NuevaT)
        return 0
    elif caracter==')':
        if existeT(listaTransicion,')',0,14):
            NuevaT=Transiciones(")",0,14)
            listaTransicion.append(NuevaT)
        consola.insert(END,caracter+" simbolo \n")
        return 0
    elif caracter=='&':
        NuevaT=Transiciones("&",0,22)
        listaTransicion.append(NuevaT)
        return 22
    elif caracter=='{':
        consola.insert(END,caracter+" simbolo \n")
        if existeT(listaTransicion,'{',0,25):
            NuevaT=Transiciones("{",0,25)
            listaTransicion.append(NuevaT)
        return 0
    elif caracter=='}':
        consola.insert(END,caracter+" simbolo \n")
        if existeT(listaTransicion,'}',0,26):
            NuevaT=Transiciones("}",0,26)
            listaTransicion.append(NuevaT)
        return 0
    elif caracter==':':
        consola.insert(END,caracter+" simbolo \n")
        if existeT(listaTransicion,':',0,27):
            NuevaT=Transiciones(":",0,27)
            listaTransicion.append(NuevaT)
        return 0
    elif caracter=='|':
        NuevaT=Transiciones("|",0,20)
        listaTransicion.append(NuevaT)
        return 20
    elif caracter=='=':
        consola.insert(END,caracter+" simbolo \n")
        if existeT(listaTransicion,'=',0,28):
            NuevaT=Transiciones("=",0,28)
            listaTransicion.append(NuevaT)
        return 0
    elif caracter=='<':
        consola.insert(END,caracter+" simbolo \n")
        if existeT(listaTransicion,'<',0,29):
            NuevaT=Transiciones("<",0,29)
            listaTransicion.append(NuevaT)
        return 0
    elif caracter=='>':
        consola.insert(END,caracter+" simbolo \n")
        if existeT(listaTransicion,'>',0,30):
            NuevaT=Transiciones(">",0,30)
            listaTransicion.append(NuevaT)
        return 0
    elif caracter=='+':
        consola.insert(END,caracter+" simbolo \n")
        if existeT(listaTransicion,'+',0,31):
            NuevaT=Transiciones("+",0,31)
            listaTransicion.append(NuevaT)
        return 0
    elif caracter=='*':
        if existeT(listaTransicion,'*',0,32):
            NuevaT=Transiciones("*",0,32)
            listaTransicion.append(NuevaT)
        consola.insert(END,caracter+" simbolo \n")
        return 0
    elif caracter==';':
        if existeT(listaTransicion,';',0,33):
            NuevaT=Transiciones(";",0,33)
            listaTransicion.append(NuevaT)
        consola.insert(END,caracter+" simbolo \n")
        return 0
    elif caracter=='-':
        if existeT(listaTransicion,'-',0,34):
            NuevaT=Transiciones("-",0,34)
            listaTransicion.append(NuevaT)
        consola.insert(END,caracter+" simbolo \n")
        return 0
    elif caracter=='/':
        if existeT(listaTransicion,"/",0,6):
            NuevaT=Transiciones("/",0,6)
            listaTransicion.append(NuevaT)
        return 5
    elif caracter=='!':
        consola.insert(END,caracter+" simbolo \n")
        if existeT(listaTransicion,'!',0,35):
            NuevaT=Transiciones("!",0,35)
            listaTransicion.append(NuevaT)
        return 0
    elif caracter==',':
        consola.insert(END,caracter+" simbolo \n")
        if existeT(listaTransicion,',',0,36):
            NuevaT=Transiciones(",",0,36)
            listaTransicion.append(NuevaT)
        return 0
    elif caracter=='.':
        consola.insert(END,caracter+" simbolo \n")
        if existeT(listaTransicion,'.',0,37):
            NuevaT=Transiciones(".",0,37)
            listaTransicion.append(NuevaT)
        return 0
    elif (caracter=='\n' or caracter==' ' or caracter=='\t'):
        return 0
    else:
        consola.insert(END,caracter+" No pertenece \n")
        NuevoError=Error(idError,fila,columna,"El Caracter "+caracter+" no pertenece al lenguaje")
        idError=idError+1
        listaError.append(NuevoError)
        return 0



def AnalizadorLexicoJS(txtcont,consola):
    lexema=""
    columna=0
    fila=1
    cerrar=False
    continuar=False
    primera=False
    conta=0
    idError=0
    estado=0
    contadorcito=0
    lex=""
    consu=0
    bus=""
    rutita=""
    esWin=False
    contenido= txtcont.get("1.0","end-1c")
    contenido = contenido.lower()
    for caracter in contenido:
        columna=columna+1
        if caracter=='\n':
            fila=fila+1
            columna=0
        if estado==0:
            estado=EstadosIniciales(estado,caracter,idError,fila,columna, consola)
        if estado==1:
            if caracter.isalpha() or caracter=='_':
                lexema=lexema+caracter
                if caracter=='_':
                    if existeT(listaTransicion,'_',1,1):
                        NuevaT=Transiciones("_",1,1)
                        listaTransicion.append(NuevaT)
                else:
                    if existeT(listaTransicion,'L',1,1):
                        NuevaT=Transiciones("L",1,1)
                        listaTransicion.append(NuevaT)
                estado=1
            else:
                if es_Reservada(lexema):
                    consola.insert(END,lexema+" Reservada \n")
                    NuevoToken=Token(conta,fila,columna,lexema)
                    conta=conta+1
                    lexema=""
                    listaToken.append(NuevoToken)
                else: #aqui puedo poner para que solo sean las conjunciones como . + - = ! / *
                    NuevoToken=Token(conta,fila,columna,lexema)
                    consola.insert(END,lexema+" Identificador \n")
                    conta=conta+1
                    lexema=""
                    listaToken.append(NuevoToken)
                estado=EstadosIniciales(estado,caracter,idError,fila,columna, consola)

        elif estado==2:
            if caracter.isdigit():
                lexema=lexema+caracter
                if existeT(listaTransicion,"D",2,2):
                    NuevaT=Transiciones("D",2,2)
                    listaTransicion.append(NuevaT)
                estado=2
            else:
                if caracter!='.':
                    consola.insert(END,lexema+" numero \n")
                    lexema=""
                    estado=EstadosIniciales(estado,caracter,idError,fila,columna, consola)
                else:
                    lexema=lexema+caracter
                    if existeT(listaTransicion,'.',2,3):
                        NuevaT=Transiciones(".",2,3)
                        listaTransicion.append(NuevaT)
                    estado=3

        elif estado==3:
            lexema=lexema+caracter
            if existeT(listaTransicion,"D",3,4):
                NuevaT=Transiciones("D",3,4)
                listaTransicion.append(NuevaT)
            estado=4

        elif estado==4:
            if caracter.isdigit():
                lexema=lexema+caracter
                if existeT(listaTransicion,"D",4,4):
                    NuevaT=Transiciones("D",4,4)
                    listaTransicion.append(NuevaT)
                estado=4
            else:
                consola.insert(END,lexema+" decimal \n")
                lexema=""
                estado=EstadosIniciales(estado,caracter,idError,fila,columna, consola)
                NuevoToken=Token(conta,fila,columna,lexema)
                conta=conta+1
                listaToken.append(NuevoToken)
        
        elif estado==5:
            lexema=lexema+caracter
            estado=6
        elif estado==6:
            if caracter=='/' or caracter=='*':
                if caracter=='/':
                    lexema=lexema+caracter
                    if existeT(listaTransicion,"/",6,7):
                        NuevaT=Transiciones("/",6,7)
                        listaTransicion.append(NuevaT)
                    estado=7
                elif caracter=='*':
                    lexema=lexema+caracter
                    if existeT(listaTransicion,"*",6,8):
                        NuevaT=Transiciones("*",6,8)
                        listaTransicion.append(NuevaT)
                    estado=8
            else:
                NuevoToken=Token(conta,fila,columna,lexema)
                conta=conta+1
                listaToken.append(NuevoToken)
                consola.insert(END,lexema+" signo / solo \n")
                lexema=""
                estado=EstadosIniciales(estado,caracter,idError,fila,columna, consola)
        elif estado==7:
            if caracter!='\n':
                lexema=lexema+caracter
                if existeT(listaTransicion,"Ca",7,7):
                    NuevaT=Transiciones("Ca",7,7)
                    listaTransicion.append(NuevaT)
            else:
                NuevoToken=Token(conta,fila,columna,lexema)
                conta=conta+1
                listaToken.append(NuevoToken)
                consola.insert(END,lexema+" comentario de linea \n")
                lexema=""
                estado=0
        elif estado==8:
            if caracter!='*':
                lexema=lexema+caracter
                if existeT(listaTransicion,"Ca",8,8):
                    NuevaT=Transiciones("Ca",8,8)
                    listaTransicion.append(NuevaT)
            else:
                lexema=lexema+caracter
                if existeT(listaTransicion,"*",8,9):
                    NuevaT=Transiciones("*",8,9)
                    listaTransicion.append(NuevaT)
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
                if existeT(listaTransicion,"/",9,10):
                    NuevaT=Transiciones("/",9,10)
                    listaTransicion.append(NuevaT)
                consola.insert(END,lexema+" comentario largo \n")
                print(lexema)
                lexema=""
                estado=0
        elif estado==12:
            if(caracter=='"' and cerrar==True):
                lexema=lexema+caracter
                estado=13
                if existeT(listaTransicion,'cs',12,13):
                    NuevaT=Transiciones('cs',12,13)
                    listaTransicion.append(NuevaT)
                continuar=False
                cerrar=False
            else:
                lexema=lexema+caracter
                estado=12
                if existeT(listaTransicion,"Ca",12,12):
                    NuevaT=Transiciones("Ca",12,12)
                    listaTransicion.append(NuevaT)
                continuar=True
                cerrar=True
        elif estado==13:
            NuevoToken=Token(conta,fila,columna,lexema)
            conta=conta+1
            listaToken.append(NuevoToken)
            consola.insert(END,lexema+" cadena \n")
            lexema=""
            estado=EstadosIniciales(estado,caracter,idError,fila,columna, consola)
        
        elif estado==15:
            if(caracter=="'" and cerrar==True):
                lexema=lexema+caracter
                if existeT(listaTransicion,"'",15,16):
                    NuevaT=Transiciones("'",15,16)
                    listaTransicion.append(NuevaT)
                estado=16
                continuar=False
                cerrar=False
            else:
                lexema=lexema+caracter
                if existeT(listaTransicion,"Ca",15,15):
                    NuevaT=Transiciones("Ca",15,15)
                    listaTransicion.append(NuevaT)
                estado=15
                continuar=True
                cerrar=True
        elif estado==16:
            NuevoToken=Token(conta,fila,columna,lexema)
            conta=conta+1
            listaToken.append(NuevoToken)
            consola.insert(END,lexema+" cadena \n")
            lexema=""
            estado=EstadosIniciales(estado,caracter,idError,fila,columna, consola)
        elif estado==20:
            if caracter=='|':
                lexema=lexema+caracter
                if lexema=='||':
                    NuevoToken=Token(conta,fila,columna,lexema)
                    conta=conta+1
                    listaToken.append(NuevoToken)
                    if existeT(listaTransicion,"||",20,21):
                        NuevaT=Transiciones("||",20,21)
                        listaTransicion.append(NuevaT)
                    consola.insert(END,lexema+" doble | \n")
                    lexema=""
                    estado=0
            else:
                if caracter!=' ' or caracter!='\n':
                    consola.insert(END,caracter+" No pertenece \n")
                    NuevoError=Error(idError,fila,columna,"El Caracter "+lexema+" no pertenece al lenguaje")
                    idError=idError+1
                    listaError.append(NuevoError)
                    lexema=""
                    estado=EstadosIniciales(estado,caracter,idError,fila,columna, consola)
                else:
                    lexema=""
                    estado=EstadosIniciales(estado,caracter,idError,fila,columna, consola)
        elif estado==22:
            if caracter=='&':
                lexema=lexema+caracter
                if lexema=='&&':
                    NuevoToken=Token(conta,fila,columna,lexema)
                    conta=conta+1
                    listaToken.append(NuevoToken)
                    if existeT(listaTransicion,"&&",22,23):
                        NuevaT=Transiciones("&&",22,23)
                        listaTransicion.append(NuevaT)
                    consola.insert(END,lexema+" doble & \n")
                    lexema=""
                    estado=0
            else:
                if caracter!=' ' or caracter!='\n':
                    consola.insert(END,caracter+" No pertenece \n")
                    NuevoError=Error(idError,fila,columna,"El Caracter "+lexema+" no pertenece al lenguaje")
                    idError=idError+1
                    listaError.append(NuevoError)
                    lexema=""
                    estado=EstadosIniciales(estado,caracter,idError,fila,columna, consola)
                else:
                    lexema=""
                    estado=EstadosIniciales(estado,caracter,idError,fila,columna, consola)
    print(len(listaTransicion))
    


            
            
                

            
        




            






