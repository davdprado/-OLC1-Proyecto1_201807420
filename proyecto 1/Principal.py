from tkinter import *

raiz=Tk() #inicia la ventana
#-------------------------------Ventana
raiz.title("Principal")
raiz.iconbitmap("image\icono.ico")
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