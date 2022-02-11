"""
Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
    - def nombre_funcion(): -> Definición
    - nombre_funcion() -> Implementación
"""
def saludar():
    print("¡Hola amiga!")

saludar()

"""
Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
"""
def saludar_2 (nombre):
    print(f"¡Hola {nombre}!")

saludar_2("Ezequiel")


"""
Escribir una función que reciba una lista de enteros positivos y devuelva su sumatoria.
"""
def sumatoria(lista):
    suma = 0
    for elemento in lista:
        suma += elemento

    return suma

resultado = sumatoria([1,2,3,4])
print(resultado)

# Versión sencilla
print(sum([1,2,3,4,5]))