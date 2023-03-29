# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construya los siguientes métodos para la clase:
# . Un constructor, donde los datos pueden estar vacíos.
# . Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
#   datos.
# . mostrar(): Muestra los datos de la persona.
# . Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona():
    def __init__(self,nombre = None, edad = None, dni = None):
        self.__nombre   = nombre
        self.__edad 	= edad
        self.__dni      = dni
        
    @property 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter 
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property 
    def edad(self):
        return self.__edad
    
    @edad.setter 
    def edad(self, edad: int):
        if ( 0 <= edad < 150):
            self.__edad = edad
        else:
            raise ValueError("la edad no es correcta")
            
        
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter 
    def dni(self, dni):
        self.__dni = dni
        
        
    def mostrar(self):
        print(f"Nombre: {self.__nombre} \nEdad :{self.__edad}\nDNI :{self.__dni}")
        
    def es_mayor_de_edad(self):
        return ( self.__edad > 17 )
    
    
    
if __name__ == "__main__":
    test = Persona("Don Ramón")
    test.mostrar()
    print('-----')
    
    test = Persona("chavo del 8", 5, '11222333')
    test.mostrar()
    print( test.es_mayor_de_edad() )
    print('-----')
    
    test = Persona("chavo del 8", 5, '11222333')
    test.mostrar()
    test.dni = '77888999'
    test.nombre = "La bruja del 71"
    test.edad = 71
    print( test.es_mayor_de_edad() )
    test.mostrar()
    print('-----')
    