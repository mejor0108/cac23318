#### Ejercicio 3
## Función para calcular la palabras y sus frecuencias de una cadena de caracteres

def word_freq(texto):
    
    
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

if __name__ == "__main__":
    texto = input("Ingrese el texto a procesar: ")
    print(word_freq(texto))