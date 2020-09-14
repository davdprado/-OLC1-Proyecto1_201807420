from Error import Error


listaError=list()

continuar=False
cerrar=False
fila=0

PalResJs =['int','var','string','char','boolean','if','for','while','do','continue','break','return','function','this','class','Math','pow']

def es_Reservada(lexema):
    for pl in PalResJs:
        if lexema==pl:
            return True
    


def EstadosIniciales(caracter):
    if caracter.isdigit():
        print("["+caracter+"] es digito")
        return 2
    elif caracter.isalnum():
        print("["+caracter+"] es letra")
        return 1
    elif
    elif (caracter=='\n' or caracter==' ' or caracter=='\t'):
        if caracter=='\n':
            fila=fila+1
        print("espacio")
        return 0
    else:
        print(caracter+" no pertenece al lenguaje")
        return 0



def AnalizadorLexicoJS(txtcont):
    columna=0
    estado=0
    lexema=""
    contenido= txtcont.get("1.0","end-1c")
    contenido = contenido.lower()
    for caracter in contenido:
        columna=columna+1
        if estado==0:
            estado=EstadosIniciales(caracter)
            print(lexema)

        if estado==1:
            if caracter.isalnum() or caracter=='_':
                lexema=lexema+caracter
                estado=1
            else:
                if es_Reservada(lexema):
                    lexema=""
                else:
                    lexema=""
                estado=0

        elif estado==2:
            if caracter.isdigit():
                lexema=lexema+caracter
                estado=2
            elif caracter=='.':
                lexema=lexema+caracter
                estado=3
            else:
                print("Error "+caracter)
                estado=0
                lexema=""
        elif estado==3:
            if caracter.isdigit():
                lexema=lexema+caracter
                estado=4
            else:
                print("Error "+caracter)
                estado=0
                lexema=""
        elif estado==4:
            if caracter.isdigit():
                lexema=lexema+caracter
                estado=4
            else:
                print("Error "+caracter)
                estado=0
                lexema=""
                



            






