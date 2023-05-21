
"""
En Python, puedes escribir en un archivo de texto utilizando la función open() junto con los métodos de archivo adecuados. 
"""
import time



def write_txt(path):
    with open('archivo.txt', 'w') as archivo:
        archivo.write('Hola, mundo!\n')
        archivo.write('Estoy escribiendo en un archivo de texto.\n')




"""
Ten en cuenta que el modo 'w' sobrescribirá el contenido existente en el archivo. 
Si deseas agregar contenido al final del archivo sin eliminar el contenido existente, 
puedes utilizar el modo 'a' en lugar del modo 'w' al abrir el archivo:
"""

def write_append(path):
    for n in range(1,15):
        time.sleep(1.5)
        with open(path, 'a') as archivo:
            archivo.write(f'{n} Esta línea será agregada al final del archivo.\n')


def main():
    write_txt('archivo.txt')
    write_append('archivo.txt')


# Verificar si se está ejecutando directamente este archivo
if __name__ == "__main__":
    # Llamar a la función main()
    main()
