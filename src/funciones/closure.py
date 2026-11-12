## crear un funcion tipo clousore que me permita ingresar nombre, apellido y me retornr un mensaje con ambos datos.
def creador(nombre:str):
    def apellido(ap:str):
        return f"tu nombre es: {nombre} y tu apellido es {ap}"
    return apellido

alumno1=creador("david") # def apellido (ap): return
alumno2=creador("noemy")
print(alumno1("gonzalez"))
print(alumno2("maikel"))


## usando closure crear un funcion multiplicador que reciva por parametro el factor que debuelba una funcion que permita multiplicar cualquier numero por el factor 
def multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar


doble = multiplicador(2)
triple = multiplicador(3)

print(doble(5))
print(triple(5))