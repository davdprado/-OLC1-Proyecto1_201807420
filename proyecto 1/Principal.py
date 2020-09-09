from tkinter import *

class Interfaz:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("[OLC1]Proyecto1")
        #-------------------------Barra de navegacion
        self.menu=Menu(self.ventana)
        new_item=Menu(self.menu)
        new_item.add_command(label='Nuevo')
        new_item.add_command(label='Abrir')
        new_item.add_command(label='Guardar')
        new_item.add_command(label='Guardar Como...')
        new_item.add_command(label='Analizar')
        new_item.add_separator()
        new_item.add_command(label='Salir')
        self.menu.add_cascade(label='Archivo',menu=new_item)
        self.menu.add_cascade(label='Ayuda')
        self.ventana.config(menu=self.menu)
        #-------------------------------------Panel donde estara todo


Ventana_principal=Tk()
Principal=Interfaz(Ventana_principal)
Ventana_principal.mainloop()



