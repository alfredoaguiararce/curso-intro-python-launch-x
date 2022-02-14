# Función para leer 3 tanques de combustible y muestre el promedio

def generate_report(main_tank, external_tank, hydrogen_tank):
    total_average = (main_tank + external_tank + hydrogen_tank) / 3
    return f"""Fuel Report:
    Total Average: {total_average}%
    Main tank: {main_tank}%
    External tank: {external_tank}%
    Hydrogen tank: {hydrogen_tank}% 
    """
    
# Función promedio 
def average(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items

    
if __name__ == '__main__':
    # Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))
    print(
        generate_report(main_tank = 80, 
                        external_tank = 70, 
                        hydrogen_tank = 85)
        ) 