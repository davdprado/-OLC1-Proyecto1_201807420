def crearRH(listax):
    archivo=open("errores.html",'w')
    archivo.writelines("<style>TABLE{border: 1px solid #64ffda;font-family:Century Gothic;} TH{color:black;} h1{font-family:Century Gothic;}</style> \n")
    archivo.writelines("<Center><h1>Listado de Errores</h1></Center>\n ")
    archivo.writelines("<Center><TABLE border = 2></Center>\n ")
    archivo.writelines("<TR bgcolor=" + "'#00b248'" + ";>\n ")
    archivo.writelines("<TH> No. </TH>\n ")
    archivo.writelines("<TH> Fila </TH>\n ")
    archivo.writelines("<TH> Columna </TH>\n ")
    archivo.writelines("<TH> Descripcion </TH>\n ")
    archivo.writelines("</TR>\n ")
    contadorcito=0
    for error in listax:
        contadorcito=contadorcito+1
        archivo.writelines("<TR>")
        archivo.writelines("<TH bgcolor=" + "'#00e676'" + ";>" + str(contadorcito) + "</TH>\n ")
        archivo.writelines("<TH bgcolor=" + "'#00e676'" + ";>" + str(error.Fila) + "</TH>\n ")
        archivo.writelines("<TH>" + str(error.Columna) + "</TH>\n ")
        archivo.writelines("<TH bgcolor=" + "'#00e676'" + ";>" + error.Descripcion + "</TH>\n ")
        archivo.writelines("</TR>\n ")
    archivo.close()
    