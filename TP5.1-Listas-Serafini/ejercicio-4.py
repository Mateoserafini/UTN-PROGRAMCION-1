#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#Respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!
#animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
print("Lista Sin modificar: " , animales)
animales[1] = "loro"
animales[-1] = "oso"
print("Lista modificada: " , animales)
