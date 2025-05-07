#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_secreto = random.randint(1, 9)
intentos = 0

while True:
    intento = int(input("Adivine el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Adivinaste en {intentos} intentos.")
        break