# Función para convertir grados Celsius a Fahrenheit

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} °C equivalen a {fahrenheit} °F")
