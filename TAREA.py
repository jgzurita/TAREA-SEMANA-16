### UEA ###

# Primero creamos o abrimos el archivo my_notes.txt  con tres lineas como se pide en las indicaciones
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("UNIVERSIDAD ESTATAL AMAZÓNICA\n")
    file.write("LA UNIVERSIDAD MAS GRANDE DE LA AMAZONIA ECUATORIANA.\n")
    file.write("LA UNIVERSIDAD PIENSA EN EL FUTURO DE TODOS.\n")

# realizamos la lectura de Archivo de Texto
# Abrimos el archivo
with open('my_notes.txt', 'r') as file:
    # mostramos cada línea del archivo
    for line in file:
        print(line.strip())