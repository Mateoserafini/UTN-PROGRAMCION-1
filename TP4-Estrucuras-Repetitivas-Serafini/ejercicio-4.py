#Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma = 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
print(f"La suma total es: {suma}")