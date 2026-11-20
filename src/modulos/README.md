# modularidad
la `modularidad` consiste en dividir un programa grande en archivos pequeños y reutilizables llamados `modulos` bcada modulo es  simplemente un archivo `.py`
**ventajas:**
- `Reutilizacion:` escribes el codigo una vez y lo usas en muchos programas.
- `
- organizacion:` cada archivo tiene una responsabilidad clara.
- `mantenimiento:` es mas facil encontrar y corregir errores.
- `trabajo en equipo:`cada persona puede desarrollar su propio modulo.

## 1. crear un modulo
basta con crear un archivo con la extencion `.py` por ejemplo `matematicas.py`. 
## 2. importar un modulo completo
la manera de como reutilizamos los modulos es haciendo uso de la palabra reserbada `import` esto se deve declarar en el archivo donde reutilizaremos ciertas funciones o variables de un modulo.
para importar un modulo completo usamos `import nombre_archivo`.
`matematicas.py`
```python
def suma(a,b):
    returna+b
def resta(a,b):, 
    return a-b
```
`main.py`
```python
import matematicas
## para hacer uso de una de las funciones tengo que acceder al archivo luego 8un punto y el nombre de dato, funcion que deseamos utilizar
matematicas.resta(5,8)
```