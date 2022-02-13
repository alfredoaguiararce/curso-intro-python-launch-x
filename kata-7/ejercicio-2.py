def ask_planet():
    
    # Declaramos 2 variables
    new_planet = ''
    planets = []
    
    # Escribe el ciclo while solicitado
    
    while new_planet.lower() != 'done':
        if new_planet:
            planets.append(new_planet)
        new_planet = input('Enter a new planet, write done to finish ')
        
    print("You'r planets are : ")
    print_planets(planets)

def print_planets(_planets):
    for planet in _planets:
        print(planet)
    
    
if __name__ == '__main__':

    ask_planet()