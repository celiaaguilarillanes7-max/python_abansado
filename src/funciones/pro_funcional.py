#ejercicio para map()
##recuerde map sirve para transformar todos los elementos 
##ejercicio 1: tienes una lista de numeros y quieres obtener una nueva lista con el cubo (elevado a 3) de cada umero.
numeros:list[int]=[1,2,3,4]
nueva_lista=list(map(lambda e:e**3,numeros))
print(nueva_lista)
def cubo(e):
    return e**3
map(cubo,numeros)

# ejercicio para filter()
##ejercicio 2. tienes una lista de temperaturas (algunas bajo cero). filtrar la lista para quedarte solo con las temperaturas positivas (mayores a 0).
temp:list[int|float]=[-2,10,0,-20,-1,-10,18,23.0]
nueva_temp=list(filter(lambda t:t>0,temp))
print(f"las temperaturas mayores a cero son: {nueva_temp}")

# ejercicio combinado map() y filter()
## tienes una lista de numeros . primero filtra paran quedarte solo con los numeros pares. luego usa, map para multiplicarlos por 10 los numeros pares.
numeros:list[int]=[2,3,5,8,7,4,6]
pares=list(filter(lambda n:n%2==0,numeros))
nueva_lista=list(map(lambda n:n*10,pares))
print(f"los numeros pares multiplicado *10: {nueva_lista}")