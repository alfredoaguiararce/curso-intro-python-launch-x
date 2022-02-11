if __name__ == '__main__':
    # Creamos la lista planetas y la mostramos
    planetas = ['Mercurio', 
                'Venus', 
                'Tierra', 
                'Marte', 
                'Jupiter', 
                'Saturno', 
                'Urano', 
                'Neptuno']

    print('Hay ', len(planetas), 'planetas en la lista.')
    
    # Agregamos a plutón y mostramos el último elemento
    planetas.append('Pluton')

    print(planetas[-1], ', es el ultimo planeta.')