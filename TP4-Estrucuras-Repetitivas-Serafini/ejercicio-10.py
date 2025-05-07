#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un número: ")
numero_invertido = numero[::-1] #se supone que usemos estructuras repetitivas pero se usar el "slicing"
print(f"Número invertido: {numero_invertido}")


#Igual dejo por aca el mismo ejercicio pero con estructuras repetitivas

#numero = input("Ingrese un número: ")
#numero_invertido = ""
#for caracter in numero:
#    numero_invertido = caracter + numero_invertido
#print(f"Número invertido: {numero_invertido}")