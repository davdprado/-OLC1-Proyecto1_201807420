from tkinter import *

class Interfaz:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("[OLC1]Proyecto1")
        
        self.menu=Menu()

Ventana_principal=Tk()
Principal=Interfaz(Ventana_principal)
Ventana_principal.mainloop()



'''
raiz=Tk() #inicia la ventana
#-------------------------------Ventana
raiz.title("Principal")
#--------------------------------Menu de navegacion------------------------
menu=Menu(raiz)
new_item = Menu(menu)
new_item.add_command(label='Nuevo')
new_item.add_command(label='Abrir')
new_item.add_command(label='Guardar como...')
new_item.add_command(label='Analizar')
new_item.add_separator()
new_item.add_command(label='Salir')
menu.add_cascade(label='Archivo',menu=new_item)
menu.add_cascade(label='Ayuda')

raiz.config(menu=menu)

#-------------------------------Contenedor Principal-------------------
contenedor1=Frame()
contenedor1.pack()    #empaquetar(meterlo dentro de la ventana)
contenedor1.config(width="900", height="600")



raiz.mainloop() #bucle infinito para que la ventana este en ejecucion continua

##'''