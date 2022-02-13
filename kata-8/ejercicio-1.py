if __name__ == '__main__':
    # Crea un diccionario llamado planet con los datos propuestos
    planet = {
        'name': 'Mars',
        'moons': 2
    }

    # Muestra el nombre del planeta y el número de lunas que tiene.
    print('{planet_name} has {planet_moons} moons.'.format(
        planet_name = planet['name'],
        planet_moons = planet['moons']
    ))
    
    # Agrega la clave circunferencia con los datos proporcionados previamente
    planet['circunference (km)'] = {
        'polar': 6752,
        'equatorial': 6792
    }

    # Imprime el nombre del planeta con su circunferencia polar.
    print('{planet_name} has a polar circunference of {planet_circunference} polar.'.format(
        planet_name = planet['name'],
        planet_circunference = planet['circunference (km)']['polar']
    ))