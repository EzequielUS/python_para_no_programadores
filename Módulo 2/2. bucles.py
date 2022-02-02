# Ejercicios para practicar

# WHILE
"""
Con un bucle while incrementar una variable entera de uno en uno (desde 0 a 10 sin incluir). Mostrar por pantalla el resultado por vuelta.
"""
contador = 0
while contador < 10:
    print(contador)
    contador += 1

"""
Pedir por teclado el nombre de usuario, si está vacío, volver a pedirlo hasta que se ingrese un nombre. Luego, saludar al usuario. 
"""
nombre = input("Ingrese un nombre: ")
while nombre == "":
    nombre = input("Ingrese un nombre: ")

print(f"Hola {nombre}")

"""
Nos pidieron mejorar el script de ingreso de sesión. Ahora el usuario podrá intentar ingresar 3 veces su usuario, y 3 veces su contraseña. De no poder acertar, se deberá mostrar por pantalla un mensaje que indique que la cantidad de intentos máxima ha sido superada. 
"""
contraseña = "1234"
contador_usuario = 1
contador_contraseña = 1

rol = input("Ingrese si su rol es admin o profesor: ")

while (rol != 'admin' and rol != 'profesor') and contador_usuario < 3:
    print("¡El usuario ingresado es incorrecto!")
    rol = input("Ingrese si su rol es admin o profesor: ")  
    contador_usuario += 1

if rol == 'admin' or rol == 'profesor':
    contraseña = input("Ingrese la contraseña: ")

    while contraseña != '1234' and contador_contraseña < 3:
        print("La contraseña ingresada es incorrecta!")
        rol = input("Ingrese si su contraseña: ")  
        contador_contraseña += 1

    if  contraseña == '1234':
        nombre = input("Ingrese su nombre: ")
        if nombre != '':
            print(f"Hola {nombre}!")
        else:
            print("El nombre ingresado no es válido")
    else:
        print("Cantidad de ingresos de contraseña maximos superados")
else:
    print("Cantidad de ingresos de usuario maxima superados")


# FOR
"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""
lista = [1,2,3,4,5,6,7,8,9,10]
for valor in lista[::-1]:
    print(valor)

"""
Se tiene una lista de nombres y se desea recorrer con un bucle for. 
nombres = ["Agustina","Marisa","Juan","Osvaldo"]. Imprimir los nombres por pantalla.
"""
nombres = ["Agustina","Marisa","Juan","Osvaldo"]

for nombre in nombres:
    print(nombre)


"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y muestre por pantalla el mensaje “Yo estudio <asignatura>”, donde <asignatura> es cada una de las asignaturas de la lista.
"""
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for materia in materias:
    print(f"Yo estudio {materia}")

"""
Se tienen dos listas con nombres: 
lista_uno = ["Pablo", “Ariel", “Junior"] 
lista_dos = [“Matias", “Mailen", “Sarah"] 
Se nos pide concatenar las listas, y luego mostrar los nombres por pantalla en mayúscula.
"""
lista_1 = ["Pablo", "Ariel", "Junior"]
lista_2 = ["Matias", "Mailen", "Sarah"]

lista_resultante = lista_1 + lista_2
for nombre in lista_resultante:
    print(nombre.upper())


