# Ejercicios para practicar
"""
1) Crear un script que me pregunte por el sabor de pizza que deseo ordenar, junto a una bebida.
Con base a la selección que realicemos el programa debera mostrar un mensaje por pantalla.
"""
gusto_de_pizza = input("Ingrese su gusto de pizza favorito: ")
bebida = input("Ingrese con que bebida le suele gusta acompañar a la pizza: ")


if gusto_de_pizza == "Mozzarella":
    print("Es un clásico")

    if bebida == "Sprite" or bebida == "Coca":
        print("Buena combinación")
    elif bebida == "Cerveza":
        print("Mas vale que sea Viernes")

elif gusto_de_pizza == "Anana" or gusto_de_pizza == "Cheddar":
    print("Pocos te van a entender")
else: 
    print("Ese gusto no lo conozco")


"""
2) Crear un script que solicite una edad, y con base a eso decida si el usuario es mayor o menor de edad.
"""
edad = int(input("¿Cuál es tu edad? "))
if edad < 18: 
    print ("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

"""
3) Crear un verificador de contraseñas. 
Mi script debe permitirme ingresar un dato y si coincide con la contraseña correcta, mostrarla por pantalla.
"""
key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")


"""
4) AFIP nos pidio un pequeño script que nos permita saber si un empleado debe pagar el impuesto a las ganancias.
Una persona paga el impuesto a las ganancias si su remuneración se encuentra por encima de los 175k y es mayor de edad. 
"""
edad = int(input("¿Cuál es tu edad? "))
ingreso = float(input("¿Cuales son tus ingresos mensuales?"))
if edad > 18 and ingreso >= 175000:
    print("Tienes pagar impuesto a las ganancias")


"""
5) Una consultora de recursos humanos nos pidio que los ayudemos a filtrar a sus candidatos.
Debemos desarrollar un script con el cual los candidatos deben interactuar, cargando su nombre, edad, rol y situación laboral.

. Si se encuentran empleados y son diseñadores, les corresponde la sala de ZOOM "MV 1"
. Si se encuentran empleados y son programadoras, les corresponde la sala de ZOOM "MV 2"

. Si se encuentran desempleados y son diseñadores, les corresponde la sala de ZOOM "NE 1"
. Si se encuentran desempleadas y son programadoras, les corresponde la sala de ZOOM "NE 2"

. Si se encuentran empleados y son mayores a 24 años, el programa debera mostrar por pantalla el mensaje: "Entrevista Técnica"
. Si se encuentran empleados y son menores a 24 años, el programa debera mostrar por pantalla el mensaje: "Entrevista Cultural"

. Si se encuentran desempleados, el programa debera mostrar por pantalla el mensaje: "Entrevista Técnica y Cultural"
"""

nombre = input("¿Cómo te llamas? ")
situacion_laboral = input("¿Situación laboral? (Empleado / Desempleado)? ")
if situacion_laboral.lower() == "desempleado":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Tu grupo es " + grupo)


"""
6) Crear el menu de presentación de una pizzeria:
. Generar un mensaje de bienvenida y mostrar las opciones de tipo de pizza:
    - Vegetariana (Tipo 1)
    . No vegetariana (Tipo 2)

. Mostrar los ingredientes para cada tipo de pizza y con base a la selección, mostrar por pantalla el pedido con sus agregados.

    - Vegetariana -> Morron - Tofu
    - No Vegetariana -> Peperoni - Jamon - Salmon
"""

# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")

# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")

"""
7) Con base al ejercicio que desarrollamos del calculo de areas, crear un menu que me permita decidir que area quiero calcular,
y me solicite los datos correspondientes segun la decisión que elija.
"""
