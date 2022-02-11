def imprimir_palabras_clave(_texto):
    # Dividimos el texto con '.split'
    texto_dividido = _texto.split(' ')
    # print(texto_dividido)
    
    # Palabras clave
    palabras_clave = ["average", 
                    "temperature", 
                    "distance"]

    # Ciclo for para recorrer la cadena
    for palabra in texto_dividido:
        for palabra_clave in palabras_clave:
            if palabra_clave in palabra:
                print(palabra)

def modificar_c(_texto):
    # Reemplazar C a Celsius
    print(_texto.replace('C', 'Celsius'))

if __name__ == "__main__":
    texto = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
    print("Parte 1: ")
    imprimir_palabras_clave(texto)
    print("Parte 2: ")
    modificar_c(texto)