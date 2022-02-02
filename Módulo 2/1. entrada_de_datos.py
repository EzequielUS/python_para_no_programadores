"""
Crear un programa que permita ingresar dos cadenas vía la consola y luego las compara, imprimiendo un mensaje en caso que sean iguales y otro en caso que sean diferentes.
"""
cadena_1 = input("Ingrese una cadena: ")
cadena_2= input("Ingrese otra cadena: ")

if cadena_1 == cadena_2:
  	print("Las cadenas son iguales")
else:
  	print("Las cadenas son distintas")

"""
Crear un programa que solicite el nombre de un alumno a través de la consola, y luego chequee que no esté vacío. En caso de estarlo, debe imprimir un mensaje de error; en caso contrario, imprimir un mensaje indicando que se ingresó correctamente.
"""
alumno = input("Ingrese un nombre: ")

if alumno == "":
  	print("El nombre ingresado se encuentra vacio")
else:
  print("Se ingreso el nombre correctamente")


"""
Se preguntará el tipo de rol que desempeña una persona en una institución por una entrada del tipo input. Los valores posibles son “admin” o “profesor”. Luego si la persona es “admin” o “profesor”, se debería pedir la contraseña, siendo la única válida “1234” (la contraseña se toma como string). Si la contraseña ingresada es válida, se procederá a pedir el nombre de la persona, y si no es vacío, se lo saludará. Contemplar los casos donde no se cumple como corresponde, y mostrar un mensaje en pantalla. 
"""