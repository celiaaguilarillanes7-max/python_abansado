## crear una funcion que reciba 5 numeros enteros y que retorne solo una lizta de numeros pares, tener encuenta las anotaciones

def num_pares(a: int, b: int, c: int, d: int, e: int) -> list[int]:
    numeros:list[int]=[a,b,c,d,e]
    numeros_pares:list[int]=[]
    for i in numeros:
        if i%2==0:
            numeros_pares.append(i)
    return numeros_pares
# print(num_pares(4, 2, 6, 8, 5))

def suma(a:int,b:int)->int:
    return a+b
print(suma(34))

def login(user="",passw=""):
    return "biembenido al sistema"
print(login(passw="11111", user="hol"))