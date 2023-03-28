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

#### Ejercicio 2
## Función para calcular el mínimo común múltiplo
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


print(mcp(2366,273))
    
#### Ejercicio 3
## Función para calcular la palabras y sus frecuencias de una cadena de caracteres

def word_freq():
    
    texto = input("Ingrese el texto a procesar: ")
    lista = texto.split(" ")
    diccionario = dict()
    for word in lista:
        if word in diccionario:
            try:
                diccionario[word] = diccionario[word] + 1 
            except IndexError:
                pass
        else:
            diccionario[word] =  1
            
    
    return diccionario


print(word_freq())

#### Ejercicio 4
## Función para calcular la palabras y sus frecuencias de una cadena de caracteres, y devolver una tupla con la palabra más repetida

def word_freq():
    
    texto = input("Ingrese el texto a procesar: ")
    lista = texto.split(" ")
    diccionario = dict()
    for word in lista:
        if word in diccionario:
            try:
                diccionario[word] = diccionario[word] + 1 
            except IndexError:
                pass
        else:
            diccionario[word] =  1
            
    
    return diccionario


def top_word_freq(diccionario):
    lista = []
    for key,item in diccionario.items():
        if len(lista) == 0:
            lista.append( key)
            lista.append(item)
        else:
            if item > lista[1]:
                lista[0] = key
                lista[1] = item 
    
    
    return (lista[0],lista[1])
    
print( top_word_freq(word_freq() ))




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

        

#get_int()
            
print ( get_int_recursive()    )
        
#### Ejercicio 6
## 
        
class Persona():
    def __init__(self, nombre= None, edad = None, dni=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre
    
    @property 
    def edad(self):
        return self.__edad
    
    @
    
    
    



# class Cuenta(object):
    
#     def __init__(self,titular = None, cantidad = None )->None:
#         self.__titular = titular
#         self.__cantidad = cantidad 
            
#     @property
#     def titular(self):
#         return self.__titular
    
#     @property
#     def cantidad(self):
#         return self.__cantidad
    
#     @titular.setter
#     def titular(self,value):
#         self.__titular
        
#     @cantidad.setter    
#     def cantidad(self,cantidad: float):
#         self.__cantidad = cantidad
    
#     def mostrar(self) -> str:
#         return f"Nombre : {self.titular()} - Cantidad : {self.cantidad()}"
    
#     def ingresar(self, cantidad):
#         if cantidad > 0:
#             self.cantidad(self, self.__cantidad + cantidad)
            
#     def retirar(self, cantidad):
#         self.cantidad( self.cantidad() - cantidad )
    
# class CuentaJoven(Cuenta):
#     def __init__(self, titular = None, cantidad = None, bonificacion = None):
#         super().__init__(titular=titular, cantidad= cantidad)
#         self.__bonificacion = bonificacion
        
#     @property
#     def bonificacion(self):
#         return self.__bonificacion
#     @bonificacion.setter
#     def bonificacion(self,bonificacion = None):
#         self.__bonificacion = bonificacion
