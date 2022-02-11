def distance_in_km(_first_planet, _second_planet):
    # Calcular la distancia entre planetas
    return _second_planet - _first_planet

def distance_in_mi(_distance_km):
    # Calcular la distancia entre planetas
    return _distance_km * 0.621  
    
if __name__ == '__main__':
    # Crear variables para almacenar las dos distancias
    # ¡Asegúrate de quitar las comas!
    first_planet = int(input('Introduzca la distancia del sol para el primer planeta en KM : '))
    second_planet = int(input('Introduzca la distancia desde el sol para el segundo planeta en KM : '))

    distance_km = distance_in_km(first_planet,
                                 second_planet)
    distance_mi = distance_in_mi(distance_km)
    
    print(distance_km, ' km')
    print(distance_mi, ' mi')