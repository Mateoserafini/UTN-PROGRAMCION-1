# Crear una función que reciba un nombre y devuelva un saludo personalizado

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")

saludo = saludar_usuario(nombre)
print(saludo)