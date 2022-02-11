def print_time(_endVelocidty, _startVelocity, _acceleration):
    time = (_endVelocidty - _startVelocity) / _acceleration
    print("Tiempo para alcanzar la velocidad deseada = ", time)

if __name__ == "__main__":
    endVelocity = 11200
    startVelocity = 0
    acceleration = 9.8
    
    # Mostramos el resultado
    print_time(endVelocity,
               startVelocity,
               acceleration)