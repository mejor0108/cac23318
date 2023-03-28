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
    ##texto = "Si algo le faltaba al 2023 para ser uno de los peores años de la historia para el campo argentino, teniendo en cuenta la sequía extrema que está viviendo, era la caída de los precios internacionales de los granos que se dio en lo que va de marzo. Si bien en la última jornada se registró una pequeña mejora en algunos contratos, la soja perdió USD 33 por tonelada en lo que va del mes en el mercado de Chicago, por lo que, teniendo también en cuenta las bajas en el aceite y la harina, podría representar pérdidas para el país de USD 1.500 millones adicionales."
    print(word_freq(texto))