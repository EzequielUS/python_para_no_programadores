"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""
## Versión 1
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")

print(monedas.get(moneda.title(), "La divisa no está."))

## Versión 2
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")

if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")


"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')

persona = {
    'nombre': nombre, 
    'edad': edad, 
    'direccion': direccion, 
    'telefono': telefono
    }

print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])


"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Fruta		Precio
Banana		80
Manzana	120
Pera		100
Naranja		65
"""
frutas = {
    'Plátano': 80, 
    'Manzana': 120, 
    'Pera': 100, 
    'Naranja': 60
    }

fruta = input('¿Qué fruta vas a pedir? \nFruta: ').title()
kg = float(input('¿Cuántos kilos? \nKilos: '))
if fruta in frutas:
    print(f"{kg} kilos de {fruta} valen ${frutas[fruta]*kg}")
else: 
    print(f"Lo siento, la fruta {fruta} no está disponible.")


