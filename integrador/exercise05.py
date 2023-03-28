
#### Ejercicio 5 
## Función que solicita un valor al usuario , en caso de ser un entero lo imprime. En caso contrario lo sigue solicitando.

def get_int():
    sigue = True
    
    while sigue:
        try:
            value = int(input("Ingrese un valor entero :" ))
        except ValueError:
            print("Valor ingresado incorrecto")
        else:
            print(value)
            sigue = False


def get_int_recursive():
        try:
            value = int(input("Ingrese un valor entero :" ))
        except ValueError:
            return get_int_recursive()
        else:
            return value

        

if __name__ == "__main__":
    print("Ejemplo 1 : usando exception")
    get_int()
    print("Ejemplo 2 : con excepcion y recursión")
    get_int_recursive()
            

        