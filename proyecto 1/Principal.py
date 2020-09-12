from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext

def abrir_archivo():
    archivo_abierto=filedialog.askopenfilename( title='Abrir Archivo',filetypes=(("css files",".css"),("all filse",".")))
    print(archivo_abierto)
class Interfaz:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("[OLC1]Proyecto1")
        #-------------------------Barra de navegacion
        self.menu=Menu(self.ventana)
        new_item=Menu(self.menu)
        new_item.add_command(label='Nuevo')
        new_item.add_command(label='Abrir',command=abrir_archivo)
        new_item.add_command(label='Guardar')
        new_item.add_command(label='Guardar Como...')
        new_item.add_command(label='Analizar')
        new_item.add_separator()
        new_item.add_command(label='Salir')
        self.menu.add_cascade(label='Archivo',menu=new_item)
        self.menu.add_cascade(label='Ayuda')
        self.ventana.config(menu=self.menu)
        #-------------------------------------Panel donde estara todo
        frame = LabelFrame(self.ventana, text = 'Analizador Lexico')
        frame.grid(row=0,column=0,columnspan=8,pady=20)

        txt = Text(frame,width=70,height=30)
        txt.grid(column=0,row=0)
        
        


Ventana_principal=Tk()
Principal=Interfaz(Ventana_principal)
Ventana_principal.mainloop()



