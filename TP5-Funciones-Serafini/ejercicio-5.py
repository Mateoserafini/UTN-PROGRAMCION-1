# Función para convertir segundos a horas

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))

horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas} horas")