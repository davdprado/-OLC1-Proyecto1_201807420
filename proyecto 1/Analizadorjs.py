from Error import Error
from Token import Token

listaToken=list()
listaError=list()
columna=0
estado=0
fila=0
continuar=False
cerrar=False
idError=0
conta=0

PalResJs =['int','var','string','char','boolean','if','for','while','do','continue','break','return','function','this','class','Math','pow']

def es_Reservada(lexema):
    for pl in PalResJs:
        if lexema==pl:
            return True
    

def EstadosIniciales(caracter):
    global idError
    global fila
    global columna
    if caracter.isdigit():
        print("["+caracter+"] es digito")
        return 2
    elif caracter.isalnum():
        print("["+caracter+"] es letra")
        return 1
    elif caracter=='"':
        return 12
    elif caracter=="'":
        return 15
    elif caracter=='(':
        return 0
    elif caracter==')':
        return 0
    elif caracter=='&':
        return 22
    elif caracter=='{':
        return 0
    elif caracter=='}':
        return 0
    elif caracter=='|':
        return 20
    elif caracter=='=':
        return 18
    elif caracter=='<':
        return 18
    elif caracter=='>':
        return 18
    elif caracter=='+':
        return 18
    elif caracter=='*':
        return 0
    elif caracter==';':
        return 0
    elif caracter=='-':
        return 18
    elif caracter=='/':
        return 5
    elif caracter=='!':
        return 18
    elif (caracter=='\n' or caracter==' ' or caracter=='\t'):
        if caracter=='\n':
            fila=fila+1
        return 0
    else:
        print("Error del caracter "+caracter)
        NuevoError=Error(idError,fila,columna,"El Caracter "+caracter+" no pertenece al lenguaje")
        idError=idError+1
        listaError.append(NuevoError)
        return 0



def AnalizadorLexicoJS(txtcont):
    lexema=""
    global columna
    global fila
    global cerrar
    global continuar
    global conta
    global idError
    estado=0
    contenido= txtcont.get("1.0","end-1c")
    contenido = contenido.lower()
    for caracter in contenido:
        columna=columna+1
        if estado==0:
            estado=EstadosIniciales(caracter)

        if estado==1:
            if caracter.isalnum() or caracter=='_':
                lexema=lexema+caracter
                estado=1
            else:
                if es_Reservada(lexema):
                    NuevoToken=Token(conta,fila,columna,lexema)
                    conta=conta+1
                    lexema=""
                    listaToken.append(NuevoToken)
                else: #aqui puedo poner para que solo sean las conjunciones como . + - = ! / *
                    NuevoToken=Token(conta,fila,columna,lexema)
                    conta=conta+1
                    lexema=""
                    listaToken.append(NuevoToken)
                estado=EstadosIniciales(caracter)

        elif estado==2:
            if caracter.isdigit():
                lexema=lexema+caracter
                estado=2
            else:
                if caracter!='.':
                    lexema=""
                    estado=EstadosIniciales(caracter)
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
                lexema=""
                estado=EstadosIniciales(caracter)
                NuevoToken=Token(conta,fila,columna,lexema)
                conta=conta+1
                listaToken.append(NuevoToken)
        
        elif estado==5:
            if caracter=='/':
                lexema=lexema+caracter
                if lexema=='//':
                    estado=6
                else:
                    NuevoToken=Token(conta,fila,columna,lexema)
                    conta=conta+1
                    listaToken.append(NuevoToken)
                    lexema=""
                    estado=0
            elif caracter=='*':
                lexema=lexema+caracter
                if lexema=='/*':
                    estado=7
            else:
                NuevoToken=Token(conta,fila,columna,lexema)
                conta=conta+1
                listaToken.append(NuevoToken)
                lexema=""
                estado=0
        elif estado==6:
            if caracter!='\n':
                lexema=lexema+caracter
            else:
                NuevoToken=Token(conta,fila,columna,lexema)
                conta=conta+1
                listaToken.append(NuevoToken)
                lexema=""
                estado=0
        elif estado==7:
            if caracter!='*':
                lexema=lexema+caracter
            else:
                lexema=lexema+caracter
                estado=8
        elif estado==8:
            if caracter!='/':
                lexema=lexema+caracter
                estado=7
            else:
                lexema=lexema+caracter
                NuevoToken=Token(conta,fila,columna,lexema)
                conta=conta+1
                listaToken.append(NuevoToken)
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
            lexema=""
            estado=EstadosIniciales(caracter)
        
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
            lexema=""
            estado=EstadosIniciales(caracter)
        elif estado==20:
            if caracter=='|':
                lexema=lexema+caracter
                if lexema=='||':
                    NuevoToken=Token(conta,fila,columna,lexema)
                    conta=conta+1
                    listaToken.append(NuevoToken)
                    lexema=""
                    estado=0
            else:
                NuevoError=Error(idError,fila,columna,"El Caracter "+caracter+" no pertenece al lenguaje")
                idError=idError+1
                listaError.append(NuevoError)
                lexema=""
                estado=0
        elif estado==22:
            if caracter=='&':
                lexema=lexema+caracter
                if lexema=='&&':
                    NuevoToken=Token(conta,fila,columna,lexema)
                    conta=conta+1
                    listaToken.append(NuevoToken)
                    lexema=""
                    estado=0
                elif lexema=='&':
                    continue
                elif lexema!='&&':
                    NuevoError=Error(idError,fila,columna,"El Caracter "+caracter+" no pertenece al lenguaje")
                    idError=idError+1
                    listaError.append(NuevoError)
                    lexema=""
                    estado=0
            
            
                

            
        




            






