"""
El entry point en Python es el punto de entrada principal de un programa. 
Es el punto desde el cual se inicia la ejecución del código. El entry point generalmente se define en el archivo 
principal de Python y se utiliza para iniciar la aplicación o el script.

El entry point se define comúnmente utilizando una función llamada main(). 
Esta función es el punto de entrada del programa y se ejecuta cuando se inicia el script. 
Puedes definir esta función main() en tu archivo principal y luego llamarla en el entry point.

"""

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]


def myfuncion():
    pass



def myfuncion2():
    return "Juan"



def myfuncion3(respuesta):
    print(respuesta)




def myfuncion4():
    print("BYE!!!")



def myfuncion5():
    pass


# TODO: Calcular la suma de todas las compras

"""
En este desafío, se te presenta una lista de objetos que representan órdenes de compra con los siguientes atributos:

customer_name: string
total: number
delivered: boolean
Tu reto es utilizar el concepto de módulos de Python para retornar la suma total de todas las órdenes de compra. Para resolver el ejercicio, 
debes trabajar en el archivo main.py, donde se encuentra la función get_total. Esta función recibe como parámetro la lista de órdenes de compra.

Debes retornar la suma total de todas las órdenes haciendo uso de las funciones definidas en el archivo my_functions.py.my_functions.py.

Ejemplo: 
Ouput:
240
"""

def get_total(orders):
    total = 0
    for order in orders:
        total += order["total"]
    return total




def main():
    print("iniciando APP....!!")
    # myfuncion()
    # respuesta = myfuncion2()
    # myfuncion3(respuesta)
    # myfuncion4()
    total = get_total(orders)
    print(total)


# Verificar si se está ejecutando directamente este archivo
if __name__ == "__main__":
    # Llamar a la función main()
    main()


"""
La verificación if __name__ == "__main__": 
es útil para asegurarse de que el código dentro de ese bloque solo se ejecute 
cuando el archivo es el punto de entrada principal y no cuando es importado como un módulo en otro archivo.

De esta manera, al ejecutar el archivo principal de Python, se llamará a la función main() 
y se ejecutará el código principal de tu programa.
"""