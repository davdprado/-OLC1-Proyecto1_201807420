class Token():
    def __init__(self,id,fila,columna,lexema):
        self.Id=id
        self.Fila=fila
        self.Columna=columna
        self.Lexema=lexema

class Transiciones():
    def __init__(self,tr,Eo,Ef):
        self.Trans=tr
        self.EstadoInicial=Eo
        self.EstadoFinal=Ef