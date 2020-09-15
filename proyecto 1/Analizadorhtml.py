from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext

listaEH=list()
listaTH=list()

Palhtml=['html','head','title','body','h1','h2','h3','h4','h5','h6','p','br','src','a','href','ul','ol','li','style','table','th','tr','td','caption','colgroup','col','thead','tbody','tfoot']

def AnalisisHTML(txt1,consola):
    fila=1
    columna=0
    contenido=txt1.get("1.0","end-1c")
    contenido = contenido.lower()
        
 

