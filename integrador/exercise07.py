# Crea una clase llamada Cuenta que tendrá
# los siguientes atributos: titular (que es una persona) y
# cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
# . Un constructor, donde los datos pueden estar vacíos.
# . Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
#   directamente, sólo ingresando o retirando dinero.
# . mostrar(): Muestra los datos de la cuenta.
# . ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
#   negativa, no se hará nada.
# . retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
#   rojos.

from exercise06 import Persona


class Cuenta():
    def __init__(self, pers: Persona, saldo=0):
        if not isinstance(pers, Persona):
            raise ValueError("el parametro pers no es del tipo Persona")
        self.__titular = pers
        self.__cantidad = saldo

    @property
    def persona(self):
        return self.__titular

    @persona.setter
    def persona(self, pers: Persona):
        self.__titular = pers

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        self.__titular.mostrar()
        print('Cantidad :',self.__cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self,cantidad):
        self.__cantidad = self.__cantidad - cantidad
                        
                        
if __name__ == "__main__":
    
    persona1 = Persona("chavo del 8", 8,'11222333' )
    cuenta1 = Cuenta(persona1)
    cuenta1.mostrar()
    cuenta1.ingresar(100)            
    print(cuenta1.cantidad)
    cuenta1.retirar(73)
    print(cuenta1.cantidad)
    cuenta1.ingresar(22)            
    print(cuenta1.cantidad)
    persona2 = Persona("Don Ramón", 8,'11222333' )
    cuenta1.persona = persona2
    cuenta1.mostrar()