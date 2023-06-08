def crearTabla(dataframe, nombreTabla): #nombre tabla es el nombre que le pondre en html
    archivoHTML=dataframe.to_html()  #con esto pasamos py a html (coje el dataframe y lo pasa a html)
    archivo=open(f"./tables/{nombreTabla}.html","w", encoding="utf-8") #(cojame un espacio para guardarlo en html dandole la ruta donde lo quiero guardar) aqui estamos abriendo un archivo y creandolo en la carpeta tables para llevarlo al html - w es que le permite al usuario escribir (un permiso)
    #para escribir etiquetas html dentro de python, para eso son las 3 comillas '''
    archivo.write('''  
    <!DOCTYPE html>  
    <html>
    <head>
    <title>TABLAS</title> 
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    </head>
    <body>
    ''')
    archivo.write(archivoHTML) #(lleveme el dataframe que ya es html y guardelo en ese espacio) para escribir el archivo html
    archivo.write('''
    </body>
    </html>            
    ''')
    archivo.close() #cerrando el proceso
    