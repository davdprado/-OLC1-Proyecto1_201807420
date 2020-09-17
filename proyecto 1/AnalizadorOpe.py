from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from Error import Error
from Token import Token
import os

listaErrorO=list()
OtraError=list()
listaExpr=list()

class FuncionA():
    def __init__(self,exp,est,fila):
        self.Fila=fila
        self.Expresion=exp
        self.Estado=est

def crearHt(listax):
    archivo=open("Sintactico.html",'w')
    archivo.writelines("<style>TABLE{border: 1px solid #64ffda;font-family:Century Gothic;} TH{color:black;} h1{font-family:Century Gothic;}</style> \n")
    archivo.writelines("<Center><h1>Listado Analisis</h1></Center>\n ")
    archivo.writelines("<Center><TABLE border = 2></Center>\n ")
    archivo.writelines("<TR bgcolor=" + "'#00b248'" + ";>\n ")
    archivo.writelines("<TH> No. </TH>\n ")
    archivo.writelines("<TH> Fila </TH>\n ")
    archivo.writelines("<TH> Expresion </TH>\n ")
    archivo.writelines("<TH> Analilsis </TH>\n ")
    archivo.writelines("</TR>\n ")
    contadorcito=0
    for ope in listax:
        contadorcito=contadorcito+1
        archivo.writelines("<TR>")
        archivo.writelines("<TH bgcolor=" + "'#00e676'" + ";>" + str(contadorcito) + "</TH>\n ")
        archivo.writelines("<TH bgcolor=" + "'#00e676'" + ";>" + str(ope.Fila) + "</TH>\n ")
        archivo.writelines("<TH>" + ope.Expresion + "</TH>\n ")
        archivo.writelines("<TH bgcolor=" + "'#00e676'" + ";>" + ope.Estado + "</TH>\n ")
        archivo.writelines("</TR>\n ")
    archivo.close()

def Estados_iniciales(caract,fil,col,consola,idError):
    if caract.isdigit():
        return 2
    elif caract.isalnum():
        return 1
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
    elif caract=='*':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract=='+':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract=='-':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif caract=='/':
        consola.insert(END,caract + " Simbolo\n")
        return 0
    elif (caract=='\n' or caract==' ' or caract=='\t'):
        return 0
    else:
        consola.insert(END,caract+" No pertenece \n")
        NuevoError=Error(idError,fil,col,"El Caracter "+caract+" no pertenece al lenguaje")
        idError=idError+1
        listaErrorO.append(NuevoError)
        OtraError.append(NuevoError)
        return 0



def AnalisisLexico(contenido,consola):
    contenido = contenido.split('\n')
    filita=0
    global OtraError
    for expresion in contenido:
        filita=filita+1
        lexema=""
        columna=0
        OtraError=[]
        fila=1
        cerrar=False
        continuar=False
        conta=0
        idError=0
        estado=0
        contadorcito=0
        rutita=""
        lex=""
        for caracter in expresion:
            columna=columna+1
            if caracter=='\n':
                fila=fila+1
                columna=0
            if estado==0:
                estado=Estados_iniciales(caracter,fila,columna,consola,idError)
            if estado==1:
                if caracter.isalnum() or caracter=='_':
                    lexema=lexema+caracter
                    estado=1
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
        if OtraError:
            NuevaExpre=FuncionA(expresion,"Incorrecta",filita)
            listaExpr.append(NuevaExpre)
        else:
            NuevaExpre=FuncionA(expresion,"Correcta",filita)
            listaExpr.append(NuevaExpre)



def Analisis_Sintactico(expres):
    pila=[]
    for c in expres:
        if c=='(':
            pila.append(c)
        else:
            if c==')' and pila:
                print(pila.pop())
    if pila:
        return True
    else:
        return False

def AnalizarOpe(txt1,txt2):
    contenido= txt1.get("1.0","end-1c")
    contenido = contenido.lower()
    AnalisisLexico(contenido,txt2)
    for func in listaExpr:
        if func.Estado=="Correcta":
            if Analisis_Sintactico(func.Expresion):
                func.Estado="Incorrecta"
    crearHt(listaExpr)
    comando="Sintactico.html"
    print(os.system(comando))


