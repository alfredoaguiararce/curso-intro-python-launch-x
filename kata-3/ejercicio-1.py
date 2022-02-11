# Escribe una expresión de prueba para calcular si necesita una advertencia.
def calcular_advertencia(_velocidad_asteroide):
    if _velocidad_asteroide > 25:
        # Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.
        print('¡Alerta! ¡Un asteroide se acerca a velocidades peligrosas!')
    else:
        print('¡Sigue con tu día!')
    

if __name__ == "__main__":
    # Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
    velocidad_asteroide = 49 # Km/s
    calcular_advertencia(velocidad_asteroide)