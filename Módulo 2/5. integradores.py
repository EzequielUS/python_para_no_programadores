# Ejercicios para practicar
"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, las almacene en otra lista, y después las muestre por pantalla con el mensaje “En <asignatura> has sacado <nota>” donde <asignatura> es cada una de las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""



"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""


"""
Pida un número entero por teclado. Luego, determine si ese número ingresado es múltiplo de 3 y de 5. Avisar al usuario que el numero ingresado es múltiplo o no. 
"""


"""
Realizar un programa que, ingresando la edad de una persona, determine si es menor, mayor con edad laboral o jubilado (contemplando jubilado para ambos sexos a los 65 años). 
"""
edad = input("Ingrese edad:  ")
edad = int(edad)

if edad < 18:
    print("Menor de edad")
else:
    if edad < 65:
        print("Edad laboral")
    else:
        print("Jubilado")

"""
En un sistema de agencia de viajes se tiene un sistema de información para paquetes turísticos. Se quiere hacer un programa que al ingresar el paquete (solo la letra) te de una descripción de lo que contiene cada “combo”. a. Paquete A: “Cancún 7 noches + Aéreos u$s 1200 por persona” b. Paquete B: “Miami 8 noches + Aéreos + Alquiler de Auto u$s 1500 por persona” c. Paquete C: “Bariloche 10 noches + Aéreos + excursiones u$s 1300 por persona” d. Paquete D: “Rio de Janeiro 10 noches + Aéreos + excursiones u$s 1400 por persona
"""
paquete = input("Ingrese el paquete: ")

if paquete =="A" or paquete == "a":
    print("Cancún 7 noches + Aéreos u$s 1200 por persona")
elif paquete == "B" or paquete == "b":
    print("Miami 8 noches + Aéreos + Alquiler de Auto u$s 1500 por persona")
elif paquete == "C" or paquete =="c":
    print("Bariloche 10 noches + Aéreos + excursiones u$s 1300 por persona")
elif paquete == "D" or paquete == "d":
    print("Rio de Janeiro 10 noches + Aéreos + excursiones u$s 1400 por persona")
else:
    print("Error de opción")

"""
Se tiene la “matriz” (una lista de listas): m = [ [10,50,5], [20,30,70], [15,45,80] ] . Recorrerla con 2 sentencias ‘for’ para mostrar cada uno de los elementos que la componen.  
"""

"""
A nuestro desafío de juego de casino vamos a agregarle las siguientes funcionalidades:
Permitir que el usuario elija la dificultad de juego con la que quiere jugar. La dificultad varía entre, “Fácil”, “Medio” y “Difícil”. Si no se seleccionará alguna de estas opciones, deberán por defecto seleccionar la modalidad “Fácil”. La dificultad se medirá según la cantidad de valores entre los que se generará el número aleatorio.
“Facil”: Los valores aleatorios se encuentran definidos entre 0 y 10. El jugador contará con 3 intentos.
“Medio”: Los valores aleatorios se encuentran definidos entre 0 y 100. El jugador contará con 6 intentos.
“Difícil”: Los valores aleatorios se encuentran definidos entre 0 y 1000. El jugador contará con 12 intentos.

Se deberá modificar la lógica del código para poder realizar los juegos utilizando una estructura iterativa (no repetir código). También, se deberá definir la cantidad de juegos según la modalidad que haya seleccionado el usuario.
"""


import random

while True:
    print("Defina la dificultad del juego:")
    print("- Facil")
    print("- Medio")
    print("- Dificil")
    dificultad = input("Opción: ")

    if dificultad == "Facil":
        elementos = 10
        juegos = 3
        break
    elif dificultad == "Medio":
        elementos = 100
        juegos = 6
        break
    elif dificultad == "Dificil":
        elementos = 1000
        juegos = 12
        break
    else:
        print("Opción incorrecta, intente nuevamente.")

valor_random = random.randint(0, elementos)

contador = 1
while contador <= juegos:
    valor_ingresado = int(input("Adivine el valor generado: "))
    if valor_ingresado > valor_random:
        print("Te pasaste, intenta con un valor mas bajo.\n")
    elif valor_ingresado < valor_random:
        print("Te falto, intenta con un valor mas alto.\n")
    elif valor_ingresado == valor_random:
        print("Felicitaciones, ganaste!")
        print(f"Valor Random: {valor_random}\nValor Ingresado: {valor_ingresado}")
        break

    contador = contador + 1

if contador > juegos:
    print("Mejor suerte la próxima!")