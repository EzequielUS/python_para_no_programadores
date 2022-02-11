"""
Crear una función que tome 2 números como argumentos y retorne el resultado de su suma. 
"""
def sumar(a,b):
	c = a + b
	print(c)

sumar(10,30)


"""
Crea una función que reciba un dato ingresado por teclado(str), que verifique que sea un número entero posible de convertir (a int), y si no lo es vuelva a pedir ese dato, hasta que sea posible de convertirlo. Luego que retorne el entero convertido. Utilizarlo para verificar si el valor representa si una persona es mayor o menor de edad.
"""
def convertir(dato):
    while dato.isdecimal() == False:
        print("¡Error!")
        dato = input("Ingrese nuevamente: ")
    return int(dato)

edad = input("Ingrese su edad: ")
edad = convertir(edad)

if edad < 18:
    print("Menor de edad")
else:
    print("Menor de edad")


"""
Escribir un programa que cree un diccionario vacío y lo vaya llenando con personas. Donde el nombre(str) será la clave(el key) y el valor(value) la edad(int). El programa debe estar acompañado de un menú: 
Menú: 
A) Agregar. 
B) Mostrar el más chico. 
C) Mostrar el más grande. 
D) Salir. 
La opción de agregar inserta a una persona. Mostrar el más chico, nos debería mostrar el nombre de la persona más chica, y viceversa el de mostrar el más grande. Con la opción 4 deberíamos salir del programa.
"""
def verificar(texto):
    while texto == "":
        print("Error")
        texto = input("Ingrese nuevamente: ")
    return texto

def convertir(dato):
    while dato.isdecimal() == False:
        print("¡Error!")
        dato = input("Ingrese nuevamente: ")
    return int(dato)
personas = {}

while True:
    print("Menú:")
    print("1 - Agregar")
    print("2 - Mostrar el más chico")
    print("3 - Mostrar el más grande")
    print("4 - Salir")
    opcion = input(">>> ")
    if opcion == "1":
        nombre = input("Ingrese un nombre: ")
        nombre = verificar(nombre)
        edad = input("Ingrese una edad: ")
        edad = convertir(edad)
        personas[nombre] = edad
        print("¡Se agrego una persona!")
    elif opcion == "2":
        # El 'truco' consiste en poner el 200 para 
        # que arranque aux_edad con un número grande 
        # y siempre tome el primero del diccionario.
        aux_edad = 200 
        # aux_nombre la dejamos vacio
        aux_nombre = ""
        for n in personas:
            if personas[n] < aux_edad:
                aux_edad = personas[n]
                aux_nombre = n
        print(aux_nombre +" es la persona más chica")
    elif opcion == "3":
        # El 'truco' consiste en poner el 0 para 
        # que arranque aux_edad con cero
        # y siempre tome el primero del diccionario.
        aux_edad = 0
        # aux_nombre la dejamos vacio
        aux_nombre = ""
        for n in personas:
            if personas[n] > aux_edad:
                aux_edad = personas[n]
                aux_nombre = n
        print(aux_nombre +" es la persona más grande")
    elif opcion == "4":
        print("¡Gracias por utilizar el programa!")
        break
    else:
        print("¡Error de opción!")