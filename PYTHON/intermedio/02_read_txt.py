"""
En Python, puedes leer archivos de texto utilizando la función open() junto con los métodos de archivo adecuados.
"""

"""
Abrir un archivo de texto en modo lectura:
Puedes utilizar la función open() para abrir un archivo en modo lectura. El modo de apertura debe ser especificado como 'r'
"""
import time


def read_txt(path):
    # Abrir un archivo de texto en modo lectura
    archivo = open(path, 'r')

    # Leer el contenido del archivo línea por línea
    for linea in archivo:
        print(linea)
        time.sleep(5)

    # Cerrar el archivo
    archivo.close()


"""
a partir de Python 3.6, se recomienda utilizar la construcción with para abrir archivos,
ya que se encargará automáticamente de cerrar el archivo después de finalizar su uso:
"""
def read_txt_with(path):
    with open(path, 'r') as file:
        for linea in file:
            time.sleep(2)
            print(linea)



def read_full_txt(path):
    # 2. Leer todo el contenido de un archivo en una cadena:
    # Puedes utilizar el método read() para leer todo el contenido de un archivo en una sola cadena.

    # Abrir un archivo de texto en modo lectura
    archivo = open(path, 'r')

    # Leer todo el contenido del archivo en una cadena
    contenido = archivo.read()

    # Imprimir el contenido del archivo
    print(contenido)

    # Cerrar el archivo
    archivo.close()




"""
El método más óptimo para leer archivos de texto en Python depende del tamaño del archivo y del tipo de lectura que deseas realizar:

1. Lectura línea por línea:
Si el archivo de texto es grande y solo necesitas procesar una línea a la vez, 
leer el archivo línea por línea utilizando un bucle for es eficiente en términos de consumo de memoria. 
Esto es especialmente útil si el archivo es demasiado grande para caber en la memoria disponible.

2. Lectura completa del archivo:
Si necesitas acceder a todo el contenido del archivo en una sola operación, el método read() es adecuado. 
Sin embargo, ten en cuenta que si el archivo es extremadamente grande, cargar todo su contenido en la memoria puede 
agotar los recursos disponibles.

3. Lectura por bloques:
Si el archivo es muy grande pero no necesitas acceder a todo su contenido al mismo tiempo, 
puedes leerlo en bloques utilizando el método read(size), donde size especifica la cantidad de bytes que deseas leer. 
Esto permite trabajar con secciones del archivo sin cargarlo completamente en memoria.
"""


def read_buffer(path):
    buffer_size = 1096  # Tamaño del bloque en bytes

    with open(path, 'r') as archivo:
        while True:
            bloque = archivo.read(buffer_size)
            if not bloque:
                break
            # Procesar el bloque leído
            time.sleep(2.5)
            print("---------" + bloque)
            print(bloque)


def main():
    path = 'peaches.txt'
    # read_txt(path)
    # read_txt_with(path)
    # read_full_txt(path)
    read_buffer(path)


# Verificar si se está ejecutando directamente este archivo
if __name__ == "__main__":
    # Llamar a la función main()
    main()
