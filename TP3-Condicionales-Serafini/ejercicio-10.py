#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.


hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()
mes = input("Ingrese el mes actual (ej: marzo): ").lower()
dia = int(input("Ingrese el día actual: "))

# esto de meses a numero facilita la comparacion.
meses_a_numero = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

numero_mes = meses_a_numero.get(mes)

if numero_mes is None:
    print("Mes inválido.")
else:
    fecha = (numero_mes, dia)

    if (fecha >= (12, 21) or fecha <= (3, 20)):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (fecha >= (3, 21) and fecha <= (6, 20)):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (fecha >= (6, 21) and fecha <= (9, 20)):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"

    if hemisferio == "N":
        print(f"Estás en {estacion_norte}")
    elif hemisferio == "S":
        print(f"Estás en {estacion_sur}")
    else:
        print("Hemisferio inválido.")