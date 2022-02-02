# Ejercicios para practicar
"""
AREAS:
- Triangulo
    (base * altura)/2

- Cincunferencia
    (π * r)**2

- Cilindro
    2π * rh + 2π * r**2 .

- Cuadrado
    l**2

- Rectangulo
    (base * altura)

1) Realizar un script que me permita calcular el area de las figuras definidas.
"""

#Triangulo
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))
area = (base * altura)/2

#Circunferencia
import math
radio = int(input("Ingrese el radio de la circunferencia: "))
area = (math.pi* radio)**2

#Cilindro
import math
pi = math.pi
radio = int(input("Ingrese el radio de la circunferencia: "))
altura = int(input("Ingrese la altura del cilindro: "))
area = (2*pi) * radio*altura + (2*pi) * radio**2

#Cuadrado
lado = int(input("Ingrese el valor de un lado: "))
are = lado**2

#Rectangulo
base = int(input("Ingrese el valor de la base: "))
altura = int(input("Ingrese la altura del rectangulo: "))

"""
2) Escribir un programa que pida al usuario dos números enteros y con ellos:
Imprimir en pantalla el resultado de sumar ambos valores
Imprimir en pantalla el resultado de restar ambos valores
Imprimir en pantalla el resultado de dividir ambos valores
Imprimir en pantalla el resultado de multiplicar ambos valores
Imprimir en pantalla el resultado de elevar cada valor a la potencia del otro
Imprimir en pantalla el resultado de la división entera entre ambos valores
"""
valor_entero_1 = int(input("Ingrese un valor entero: "))
valor_entero_2 = int(input("Ingrese otro valor entero: "))

print(valor_entero_1 + valor_entero_2)
print(valor_entero_1 - valor_entero_2)
print(valor_entero_1 / valor_entero_2)
print(valor_entero_1 * valor_entero_2)
print(valor_entero_1 ** valor_entero_2)
print(valor_entero_2 ** valor_entero_1)
print(valor_entero_1 // valor_entero_2)

"""
3) En un script de Python, crear tres variables nombradas a, b y c con valores numéricos cualesquiera; una cuarta llamada resultado que sea la suma de las primeras tres, y por último imprimir en pantalla cada una de ellas. Antes de mostrar el valor de cada variable, indicar su nombre en una línea anterior. 
"""
a = 1
b = 2
c = 3
resultado = a + b + c

print("a")
print(a)

print("b")
print(b)

print("c")
print(c)

"""
4) Crear dos variables, saludo y nombre, cuyos contenidos sean "Hola, " en el primer caso y tu nombre en el segundo. Imprimir en pantalla el resultado de sumarlas.
"""
saludo = "Hola, "
nombre = "Ezequiel"

print(saludo + nombre)


