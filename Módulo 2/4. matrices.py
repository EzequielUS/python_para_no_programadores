"""
Crear un programa que solicite una fila y una columna e imprima en pantalla el número en esa posición según la siguiente matriz.  
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]] - acceso a un elemento: matriz[fila][columna]
"""

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

fila = int(input("Fila: "))
columna = int(input("Columna: "))

if fila < len(matriz):
	if columna < len(matriz[fila]):
		print(matriz[fila][columna])
	else:
		print("Error en las columnas")
else:
	print("Error en las filas")






