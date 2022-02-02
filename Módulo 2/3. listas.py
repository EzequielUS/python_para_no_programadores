"""
Se tiene la siguiente lista de nombres: 
nombres = ["Pablo", "Tomas", "Ricardo"] 
Insertar entre Tomas y Ricardo a Mailen. Y luego agregar al final a Sarah. Para finalizar, hay que recorrer la lista y mostrar a todos los nombres por pantalla.
"""

nombres = ["Pablo", "Tomas", "Ricardo"] 
nombres.insert(2,"Mailen")
nombres.append("Sarah")
posicion = 0

while posicion<len(nombres):
    print(nombres[posicion])
    posicion+=1

"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""
cantidad_materias = input("Ingrese la cantidad de materias a ingresar: ")
while not cantidad_materias.isdecimal():
    cantidad_materias = input("Esta ingrensado un valor no númerico. Ingrese un número: ")

cursos = []
contador = 0
cantidad_materias = int(cantidad_materias)

while contador < cantidad_materias:
    materia = input("Ingrese un nombre: ")
    cursos.append(materia)
    contador += 1

print(cantidad_materias)



