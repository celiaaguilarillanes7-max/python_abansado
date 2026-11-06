# en el siguiente funcion deberan escribir la documentacion segun la convencion para el docstring de funciones.

def area_rectangulo(b,h):
      """
    Calcula el área de un rectángulo.

    Args:
        b (float): este argumento sera la Base del rectángulo.
        h (float): este argumento sera la Altura del rectángulo.

        Raises:
            los argumentos no podran ser igual o menores a o 
    Returns:
        int|float: el resustado de la operacon b*h (base*haltura)
    """
      return b*h


# funcion para allar la potencia de un numero
def potencia(n:int,p:int)->int:
    """
calcula la potencia de un numero.

    Args:
        n (int): numero que se ba multiplicar (base)
        p (int): cantidad de veces que se multiplica (exponente)

    Returns:
        int: resultado de la potencia.
    """
    resultado:int=1
    for _ in range(p):
         resultado *= n
    return resultado
