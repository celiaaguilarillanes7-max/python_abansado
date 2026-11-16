## 1. Funciones Básicas Crea una función llamada calcular_area_rectangulo que reciba la base y la altura de un rectángulo (números enteros o flotantes) y retorne su área calculada. Pruébala llamándola con dos valores distintos e imprime el resultado. 
def calcular_area_rectangulo(base: float, altura: float) -> float:
    return base * altura


print(calcular_area_rectangulo(5, 4))
print(calcular_area_rectangulo(7.5, 3))
