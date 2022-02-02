"""
Ejercicio Investigación
"""
# Primera medición
medicion_1 = float(input("Ingrese la primera medición: "))

# Segunda medición
medicion_2 = float(input("Ingrese la segunda medición: "))

# Tercera medición
medicion_3 = float(input("Ingrese la tercera medición: "))

# Cuarta medición
medicion_4 = float(input("Ingrese la cuarta medición: "))

# Quinta medición
medicion_5 = float(input("Ingrese la quinta medición: "))

# Calculo el promedio
promedio = (medicion_1 + medicion_2 + medicion_3 + medicion_4 + medicion_5) / 5

if promedio > 1800 and promedio < 2800:
    print(f"Medición válida. Valor obtenido: {round(promedio, 1)}")
elif promedio > 2800:
    print(f"Medición por encima del rango. Valor obtenido: {round(promedio, 2)}")
elif promedio >= 0 and promedio < 1800:
    print(f"Medición por debajo del rango. Valor obtenido: {promedio}")
elif promedio < 0:
    print(f"Medición Errónea. Valor: {int(promedio)}")



"""
Ejercicios Boliche
"""
print("Bienvenido al sistema de pedidos.")
dni = int(input("Introduzca su DNI: "))

es_mayor_de_edad = False
error_de_sistema = False

if dni >= 5000000 and dni <= 45000000:
    print("El DNI ingresado corresponde a un mayor de edad.")
    es_mayor_de_edad = True
elif dni < 5000000:
    print("El DNI ingresado no corresponde a un sujeto activo.")
    error_de_sistema = True
elif dni > 45000000 and dni <= 50000000:
    print("El DNI ingresado corresponde a un menor de edad.")
    es_mayor_de_edad = False
elif dni > 50000000:
    print("El DNI ingresado corresponde a un menor de 16 años.")
    error_de_sistemaror = True

if not error_de_sistema:
    if es_mayor_de_edad:
        print("Bebidas disponibles: ")
        print("0. Agua")
        print("1. Coca Cola")
        print("2. Sprite")
        print("3. Cuba Libre")
        print("4. Fernet")
        opcion = int(input("Opción: "))

        if opcion >= 0 and opcion <= 4:
            print("Pedido correcto, se ha generado el ticket.")
        else:
            print("Pedido incorrecto. Fin del programa.")

    else:
        print("Bebidas disponibles: ")
        print("0. Agua")
        print("1. Coca Cola")
        print("2. Sprite")
        opcion = int(input("Opción: "))

        if opcion >= 0 and opcion <= 2:
            print("Pedido correcto, se ha generado el ticket.")
        else:
            print("Pedido incorrecto. Fin del programa.")



"""
Desarrollar el juego Guess it.

El mismo consiste en generar un valor aleatorio, entre un rango de valores predefinido (lo modificamos con base a su dificultad), permitirle
al usuario 3 intentos para poder acertar el numero, guiandolo con base al valor que haya elegido.
"""

import random

gano = False
valor_random = random.randint(0, 3)
valor_ingresado = int(input("Adivine el valor generado: "))

if valor_ingresado > valor_random:
    print("Te pasaste, intenta con un valor mas bajo.")
elif valor_ingresado < valor_random:
    print("Te falto, intenta con un valor mas alto.")
elif valor_ingresado == valor_random:
    print("Felicitaciones, ganaste!")
    print(f"Valor Random: {valor_random}\nValor Ingresado: {valor_ingresado}")
    gano = True

if not gano:
    valor_ingresado = int(input("Adivine el valor generado: "))
    if valor_ingresado > valor_random:
        print("Te pasaste, intenta con un valor mas bajo.") 
    elif valor_ingresado < valor_random:
        print("Te falto, intenta con un valor mas alto.")
    elif valor_ingresado == valor_random:
        print("Felicitaciones, ganaste!")
        print(f"Valor Random: {valor_random}\nValor Ingresado: {valor_ingresado}")
        gano = True

if not gano:
    valor_ingresado = int(input("Adivine el valor generado: "))
    if valor_ingresado > valor_random:
        print("¡Te pasaste, mejor suerte la próxima!")
    elif valor_ingresado < valor_random:
        print("¡Te falto, mejor suerte la próxima!")
    elif valor_ingresado == valor_random:
        print("Felicitaciones, ganaste!")
        print(f"Valor Random: {valor_random}\nValor Ingresado: {valor_ingresado}")