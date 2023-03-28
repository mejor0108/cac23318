#### Ejercicio 4
## Función para calcular la palabras y sus frecuencias de una cadena de caracteres, y devolver una tupla con la palabra más repetida

from exercise03 import word_freq


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

if __name__ == "__main__":
    texto = input("Ingrese el texto a procesar: ")
    print(top_word_freq( word_freq(texto)))
    


