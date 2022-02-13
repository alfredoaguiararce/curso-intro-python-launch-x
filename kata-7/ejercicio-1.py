def ask_planet():
    
    # Declaramos 2 variables
    new_planet = ''
    planets = []
    
    # Escribe el ciclo while solicitado
    
    while new_planet.lower() != 'done':
        if new_planet:
            planets.append(new_planet)
        new_planet = input('Enter a new planet, write done to finish ')


if __name__ == '__main__':

    ask_planet()