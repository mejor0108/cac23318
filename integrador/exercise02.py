#### Ejercicio 2
## Función para calcular el mínimo común múltiplo

from exercise01 import mcd

def mcp(num1 , num2):
    """
    Función para calcular el mínimo común múltiplo
    Arguments:  num1 : int
                num2 : int
    Return : minimo_comun_multiplo(num1, num2) : int
    Description : Si conocemos el mcd, podemos aplicar la ecuación 

    mcm (a, b)  = ( a * b ) / (mcd(a,b))
    """
    value_mcd =  mcd(num1, num2)
    
    return ((num1 * num2) / value_mcd )

if __name__ == "__main__":
    num1 = int( input('Ingrese el primer numero: ') )
    num2 = int( input('Ingrese el segundo numero: ') )
    print("El minimo comun multiplo ",mcp(num1,num2))

