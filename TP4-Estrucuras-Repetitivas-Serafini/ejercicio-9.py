#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cantidad = 100  # cambiar a un número menor para probar
suma = 0

for _ in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / cantidad
print(f"La media de los números es: {media}")