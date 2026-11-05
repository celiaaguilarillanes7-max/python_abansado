# haciendo uso de lambda crear un funcion muestre un mensaje personalizado

mensaje=lambda texto:texto
print(mensaje("hola mundo"))

#crear un funcion para calcular el area de un rectangulo, siendo la formula la siguiente area =base*altura

area_rectangulo:int=lambda b,h: b*h
print(area_rectangulo(h=8,b=4))
print(area_rectangulo(10,7))

#crear una funcion que verefique si un numero es par inpar
#primera forma
es_par=lambda n: n%2 == 0
if es_par(4):
    print("es par")
else:
    print("es impar")
# segunda forma
si_es_par=lambda n: "es par" if n%2==0 else"es impar"
print(si_es_par(100))