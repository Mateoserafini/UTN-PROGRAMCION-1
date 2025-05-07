#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#Dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print(f"El número tiene {cantidad_digitos} dígitos")