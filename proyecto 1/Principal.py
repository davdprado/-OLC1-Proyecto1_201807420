from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext


def abrir_archivo():
    archivo_abierto=filedialog.askopenfilename( title='Abrir Archivo', initialdir='/home/roberto/',filetypes=(("css files",".css"),("all filse",".")))
    ruta=archivo_abierto
    if ruta !="":
        arch=open(ruta,'r')
        lectura=arch.read()
        text1.insert("1.0",lectura)
        arch.close()
    
    


Ventana_principal=Tk()
Ventana_principal.title("[OLC1]Proyecto1")

#-------------------------Barra de navegacion
menu=Menu(Ventana_principal)
new_item=Menu(menu)
new_item.add_command(label='Nuevo')
new_item.add_command(label='Abrir',command=abrir_archivo)
new_item.add_command(label='Guardar')
new_item.add_command(label='Guardar Como...')
new_item.add_command(label='Analizar')
new_item.add_separator()
new_item.add_command(label='Salir')
menu.add_cascade(label='Archivo',menu=new_item)
menu.add_cascade(label='Ayuda')
Ventana_principal.config(menu=menu)
#-------------------------------------Panel donde estara todo
frame = LabelFrame(Ventana_principal, text = 'Analizador Lexico')
frame.grid(row=0,column=0,columnspan=8,pady=20)

text1 = Text(frame,width=70,height=30)
text1.grid(column=0,row=0)
        
        
        
        
  
        



Ventana_principal.mainloop()



