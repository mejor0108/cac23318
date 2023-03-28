#!/bin/python

#### Ejercicio 1
## Función para calcular el máximo común 

def mcd(num1 , num2):
    """
    Función para calcular el máximo común divisor
    Arguments:  num1 : int
                num2 : int
    Return : 
            maximo_comun_divisor(num1, num2) : int
    """
    if num1 <= num2:
        num1, num2 = num2,num1
    resto = num1 % num2 
    
    if resto == 0:
        return num2
    else:
        return mcd(num2,resto)
    
if __name__ == "__main__" :
    num1 = int( input('Ingrese el primer numero: ') )
    num2 = int( input('Ingrese el segundo numero: ') )
    
    print( "El maximo comun divisor es : ",mcd(num1, num2) )