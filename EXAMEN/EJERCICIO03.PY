## 3. Type-hints (Anotaciones de tipo) Diseña una función llamada obtener_promedio que reciba una lista de números enteros (list[int]) y retorne un número flotante (float) que represente el promedio de los valores. Incluye las anotaciones de tipo estrictas vistas en el apunte. 

def obtener_promedio(numeros: list[int]) -> float:
    return sum(numeros) / len(numeros)


print(obtener_promedio([10, 15, 20, 25]))