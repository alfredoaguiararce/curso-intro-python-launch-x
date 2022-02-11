if __name__ == '__main__':
    # Creamos la lista planetas y la mostramos
    planetas = ['Mercurio', 
                'Venus', 
                'Tierra', 
                'Marte', 
                'Jupiter', 
                'Saturno',
                'Neptuno']
    print("Basado en la siguiente lista : ")
    for planeta in planetas:
        print(planeta)
        
    # Solicitamos el nombre de un planeta
    user_planeta = str(input("Escribe el nombre de cualquiera de los planetas en el arreglo: ")).lower().capitalize()
    # Busca el planeta en la lista
    user_planeta_index =  planetas.index(user_planeta)
    
    # Muestra los planetas más cercanos al sol
    print('Aqui hay algunos planetas mas cercanos al sol que -> ' + user_planeta)
    print(planetas[0:user_planeta_index])    
    # Muestra los planetas más alejados al sol
    print('Aqui hay algunos planetas mas lejanos al sol que -> ' + user_planeta)
    print(planetas[user_planeta_index + 1::])