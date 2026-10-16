## RECURSIVIDAD EN PYTHON
# DEFINICION
La recursividad en Python es una técnica de programación en la que una función se llama a sí misma para resolver un problema. Se utiliza para dividir un problema en partes más pequeñas hasta llegar a una condición que detenga las llamadas.

# EJEMPLOS
Ejemplo 1: Contar números del 5 al 1
Este programa utiliza la recursividad para mostrar los números en orden descendente.
```python
def contar(n):
    if n == 0:
        return
    print(n)
    contar(n - 1)

contar(5)
Resultado:
5
4
3
2
1
```
¿Cómo funciona?
La función recibe el número 5.
Muestra el número en pantalla.
Se llama nuevamente restando 1 al número.
El proceso se repite hasta que el número llega a 0.
Cuando llega a 0, la función se detiene.
Ejemplo 2: Calcular el factorial de un número
El factorial consiste en multiplicar un número por todos los enteros positivos menores que él hasta llegar a 1.
def factorial(n):
```python
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
Resultado:
120
```
# COMO FUNCIONA
La función recibe el número 5.
Multiplica el número por el resultado de llamar nuevamente a la función con un número menor.
El proceso continúa con 4, 3, 2 y 1.
Cuando llega a 1, devuelve el valor 1.
Finalmente, se realizan las multiplicaciones y se obtiene 120.
Ejemplo 3: Sumar números del 1 hasta n
Este programa utiliza la recursividad para sumar todos los números desde 1 hasta el número indicado.
```python
def sumar(n):
    if n == 0:
        return 0
    return n + sumar(n - 1)

print(sumar(5))
Resultado:
15
```

