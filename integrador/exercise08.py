
# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta 
# nueva clase, además del titular y la cantidad se debe guardar 
# una bonificación que estará expresada en tanto por ciento. 
# Crear los siguientes métodos para la clase:
# . Un constructor.
# . Los setters y getters para el nuevo atributo.
# . En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
#   tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
#   mayor de edad pero menor de 25 años y falso en caso contrario.
# . Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# . El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
#   cuenta.

from exercise06 import Persona
from exercise07 import Cuenta


class CuentaJoven(Cuenta):
    def __init__(self, pers: Persona, saldo=0, bonif = 0 ):
        super().__init__(pers, saldo)        
        self.__bonificacion = bonif
    

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonif):
        self.__bonificacion = bonif

    def es_titular_valido(self):
        persona = self.persona
        return  ( persona.es_mayor_de_edad() and persona.edad < 25) 
            
    def ingresar(self,cantidad):
        super().ingresar(cantidad)
        
    def retirar(self,cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
            
    def mostrar(self):
        print("Es cuenta Joven")
        super().mostrar()
        print('Bonificación :',self.__bonificacion)
                        
                        
if __name__ == "__main__":
    
    persona1 = Persona("chavo del 8", 20,'11222333' )
    cuenta_joven = CuentaJoven(persona1, 0 , 25)
    
    cuenta_joven.mostrar()
    cuenta_joven.ingresar(100)            
    print(cuenta_joven.cantidad)
      
    cuenta_joven.retirar(73)
    print(cuenta_joven.cantidad)
    