# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.
def comprobacion(_velocidad_asteroide, _tamano_asteroide):
    if _velocidad_asteroide > 25 and _tamano_asteroide > 25:
        print('¡Alerta, Un asteroide muy peligroso viene hacia la Tierra!')
        
    elif _velocidad_asteroide >= 20:
        print('Look up! ¡Hay una luz mágica en el cielo!')
        
    elif _tamano_asteroide < 25:
        print('Nada que ver aquí :)')
        
    else:
        print('Nada que ver aquí :)')
        
    
if __name__ == "__main__":
    # Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
    velocidad_asteroide = 25
    tamano_asteroide = 40
    comprobacion(velocidad_asteroide, 
                 tamano_asteroide)