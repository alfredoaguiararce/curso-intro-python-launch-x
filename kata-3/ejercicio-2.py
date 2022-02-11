# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False
def is_rayo_visible(_velocidad_asteroide):
    if _velocidad_asteroide >= 20:
        print('Look up! ¡Hay una luz mágica en el cielo!')
    else:
        print('¡Nada que ver aquí!')
        
    
if __name__ == "__main__":
    # Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
    velocidad_asteroide = 19 # km/s
    is_rayo_visible(velocidad_asteroide)