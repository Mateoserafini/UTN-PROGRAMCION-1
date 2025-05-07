#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

limite = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(limite + 1):
    suma += i

print(f"La suma de los números de 0 a {limite} es: {suma}")