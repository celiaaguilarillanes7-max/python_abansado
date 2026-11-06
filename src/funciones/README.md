# funciones en python
las funciones no permiten ordenar mejor el codigo y reutilizarlo cuando sea necesario.
```python
# ejemplo deseamos crear un programa en python que nos permite sumar dos numeros
numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20
suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro
print(suma)
print(suma_dos)
```
como hacemos reutilizable del ejercicio anterior y mas lejible.
para eso utilizaremos funciones.
la caracteristica de una funcion en python es la siguiente:

1. debe comenzar con la palabra reservada `def`
2. debe tener un nombre que de a entender que realizara la funcion.
3. debera tener parametros y estos estaran enserrados en parentesis `()`. no todas las funciones resibiran.
4. las funciones deberan retornar datos a travez de la ´palabra recervada `return`.
   
 ```python
# crear un programa que me permita sumar dos numeros
def sumar(a,b):
    return a+b
print(sumar(78,56))
print(sumar(45,5))
 ```
 ## funciones avanzadas
 existes tres grandes conseptod para poder entender el uso abanzado de laqs funciones:
 1. argumentos, parametrosposicionales y nominales, *args y +kargs.
 2. anotaciones en la salida de una funcion.
 3. recurcividad.
```python
# anotaciones en una funcion
def suma(a:int,b:float)->int:
    return a+b
# crear solo las notaciones de una funcion que reciba 4 numeros enteros y como salida que me muestre los 4 numeros enteros en una lizta.
def numeros_lista(a: int, b: int, c: int, d: int) -> list[int]:
    return [a, b, c, d]
```
**Argumentos parametros**
-**parametros** - los parametros son las variables que se declaran en la definicion de la funcion 
- **argumentos** - es el dato concreto emviado en el llamado de la funcion
  **nota:** en ambos casos tenemos los posicionales/nominales
```python
# parametros
def suma(a,b): # en este caso tenemos una funcion suma que recibe dos parametros a,b
suma(34,45) # en este caso estoy llamando a la funcion pasandole como argumento los datos.
# en este caso en concreto podemos desir que estamos frente a un funcion que tiene parametros posicionales, eso significa que cada valor remplaza en el orden que le pasemos a las variables,34->a , 45->b

def login(usuario="",password=""):
return "acceso correcto"
login(password="12345678",usuario="tupapi")
# esta funcion es una funcion nominal por que para pasar los valores tengo que indicar la variable a la que se le va asociar en el parametro de la funcion.

```
## CONOCIENDO MAS SOBRE FUNCIONES *PARAMETROS Y ARGUMENTOS*

Sobre los parametros/argumentos nominales es ampliamente usado para distintas configuraciones ya que se puede pasar argumentos solo los argumentos que se usaran y dejar los parametros por defecto si no se van a modificar.

python
# Tenemos un programa que me permite acceder a internet que tiene parametros por defecto sin embargo si se actualiza uno de los accesos se podra modificar el valor.

## PRIMER CASO ACCESOS POR DEFECTO
def config (user="admin",pass="1234",port="8080",BSSID="WIFI"):
    return "conectado a la red"
config()

## SEGUNDO CASO 1 BSSID CAMBIO POR EL DE "LANORATORIO1"
def config (user="admin",pass="1234",port="8080",BSSID="WIFI"):
    return "conectado a la red"
config(BSSID="laboratorio1")

## REYNER DESEA CONECTARSE AL WIFI DE ANA LUZ,PREGUNTA COMO SE LLAMA TU WIFI Y CUAL ES LA CONTRASEÑA.RESPUESTA LE DISE EL WIFI ES A56 Y SU CONTRASEÑA ES 12345678
def config (user="admin",pass="1234",port="8080",BSSID="WIFI"):
    return "conectado a la red"
config(BSSID="A56",pass="12345678")


## CONOCIENDO *ARGS Y **KARGS (EMPAQUETADO Y DESEMPAQUETADO DE ARGUMENTOS POSICIONALES)

### DESEMPAQUETANDO ARGUMENTOS *POSICIONALES*

Esta tecnica nos permite empaquetar nuestros argumentos cuando no sabemos la cantidad de datos que vamos a pasar.Imaginemos que nos pide una funcion para sumar n cantidad de numeros la solucion seria empaquetar los argumentos y luego desempaquetarlos para ello en la definicion de la funcion detro de los parametros debemos usar el parametro * delante del nombre del parametro posicional esto hara que todos los argumentos se almacenan en una tupla (lista) esto nos permite recorer dentro de sus elementos para poder desempaquetarlo y realizar las operaciones necesarias.

python
# Deseamos crear una funcion que nos permita sumar n cantidad de numeros
# n -> es un numero variable puede ser 3,7,8.....n

def suma (*args):
    # *args =(2,5,7,8,9)
    acumulado=0
    for i in args:
        acumulado += i
    return acumulado
print(suma(2,5,7,8,9))


## DESEMPAQUETANDO ARGUMENTOS *NOMINALES*

En este caso como en el anterior utilizaremos el operador * la casuistica es el mismo sin embargo para desempaquetar argumento nominales usaremos ** delante del nombre del parametr nominal,diferrencia del anterior esto se empaquetara en un diccionario ({clave:valor})

python
# Debemos crear una funcion que me permita saber encontrar la persona con mayor calificacion.
```python
def mejor_alumno(**kwargs):
    # **kwargs={'Noemmy'=20,'Eduardo'=18,'David'=1}
    for alumno,nota in kwargs.items():
        if nota > nota_maxima:
            nota_maxima = nota
            mejor_alumno = alumno
    return mejor_alumno
mejor_alumno(Noemmy=20,Eduardo=18,David=19)
```
## funciones anonimas 
las funciones anonimas en python son llamadas `lambda`, estas funciones tienen las siguientes propiedades: 
1. se escribe en una unica sentencia `(linea)`.
2. no tiene nombre`(anonima)`.
3. su cuerpo conlleva un `return` implicito.
4. puede recibir cualquier numero de parametros.

la estructura para defenir una funcion `lambda` es la siguiente:
1. escribir la palabra recervada `lambda`
2. especificar la cantidad de parametros.
3. indicar los datos de retorno.
```python
lambda a,b: a+b
```
> [!TIP] puesto que esta funcion es anonima para ejecutar la debemos almacenar la funcion en una variable.

```python
suma=lambda a,b: a+b
suma(3,6)
```
## Documentacion
python nos permite documentar un funcion con el objetivo de explicar mejor determinadas zonas de nuestro codigo, para esto usamos una cadena de texto despues de la defenicion de una funcion, a esta cadena de texto se le conoce como `docstring` y esta delimitado por triples `"""aqui el texto"""`.
```python
"""
funcion para realizar la suma de dos numeros
"""
## los docstring tambien nos permite explicar los parametros que recibe y los datos de salida
def resta(a,b):
"""
a= un numero entero.
b= un numero entero.
en ambos casos a,b no deben recivir balores menores o.
retornara un dato entero <int> positivo
"""
return a-b
```
> [!WARNING] en el proceso de documentacion tener encuenta de incluir a lo menos lo siguiente: 
> 1. breve explicacion sobre que hace la funcion. 
> 2. especificaciones  y caracteristicas de los parametros incluyendo sus tipos. 
> 3. restricciones de la funcion. 
> 4.el valor que retorna y sus caracteristicas

## type-hints (Anotaciones de tipo)
nos permite indicar que tipo de datos tendra una variable, parametro y el  valor de retorno.
para utilizarlos devemos indicar el tipo de datocdespues del separador `:`, en el caso del valor de retorno usaremos `->` luego el tipo de datos y finalmente el separador `:` que indica el inicio del bloque de codigo de la funcion.
las `anotaciones de tipo ` son una erramienta que nos permite complementar la documentacion de nuestro codigo
**tenemos los siguentes**
- **simples**
    - int -> numeros enteros
    - float -> numeros decimales
    - bool -> datos boleanos (verdad o falso)
    - srt -> datos de tipo texto o cada 
    - list -> listas `[]`
    - tuple -> tuplas `()`
    - dict -> diccionario `{}`
- **compuestos**
existen casos en los que necesitamos mas expresividad en la *anotacion de tipo*  ¿Que ocurre si queremos indicar una *lista de cadenas* o un *conjunto de enteros*.?
- list[str] -> lista de cadenas de texto
- list[int] -> lista de numeros enteros
- dict[str,float] ->diccionario donde las claves son cadenas de texto y los valores son flotantes/decimales.
- **Multiples**
  en el caso que queremos indicar que un determinado parametro puede ser de un `tipo o de otro` tenemos que especificar lo usado el opedor `|`9
- tuple|dict -> puede ser datos  de tipo tupla o diccionario.
- list[srt|int] ->lista cuyos elementos pueden ser cadena de texto o enteros.
- dict[srt|int,float|int] -> dicionario cuya clave puede ser cadena o entero cuyo valor puede ser flotante o entero.