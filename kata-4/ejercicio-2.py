def title(_name, _planet):
    # Creamos el titulo
    titulo = 'Talking about the gravity in the {luna} and the {tierra} : '.format(
        luna = _name,
        tierra = _planet
        )
    return titulo
    
def template( _name, _gravity, _planet):
    # Creamos la plantilla
    hechos = """Name of the planet : {planeta}
    Gravity in {nombre} : {gravedad} m/s^2.""".format(
        planeta = _planet,
        nombre = _name,
        gravedad = _gravity * 1000
    )
    return hechos
    
def separador(item):
    return item * 84
    
def print_all(_title, _template):
    print(_title)
    print(separador('-'))
    print(_template)

if __name__ == '__main__':
    # Datos con los que vas a trabajar
    name = "Moon"
    gravity = 0.00162 # km/s
    planet = "Earth"
    title_1 = title(name,
                      planet)
    template_1 = template(name,
                          gravity,
                          planet)  
    print_all(title_1,
              template_1) 
    
    # Nuevos datos muestra
    planet = 'Marte '
    gravity  = 0.00143
    name = 'Ganímedes'
    title_2 = title(name,
                      planet)
    template_2 = template(name,
                          gravity,
                          planet)  
    print_all(title_2,
              template_2) 