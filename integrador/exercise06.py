
##  Ejercicio 6 
##
##
# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construya los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.


class Persona(Object):
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre   = nombre
        self.__edad     = edad
        self.__dni      = dni
        
    @property
    def nombre(self):
        
        
        
        
        
        
        
        