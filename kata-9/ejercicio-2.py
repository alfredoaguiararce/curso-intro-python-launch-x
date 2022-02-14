# Función con un informe preciso de la misión. Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno

def first_mission_report(pre_launch_time, flight_time, destination, external_tank, main_tank):
    return f"""
    Mission to {destination}
    Total travel time: {pre_launch_time + flight_time} minutes
    Total fuel left: {external_tank + main_tank} gallons
    """

# Escribe tu nueva función de reporte considerando lo anterior

def second_mission_report(destination, *minutes, **fuel_reservoirs):
    return f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """
    
# Escribe tu nueva función

def third_mission_report(destination, *minutes, **fuel_reservoirs):
    main_report = f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """
    for tank_name, gallons in fuel_reservoirs.items():
        main_report += f"{tank_name} tank --> {gallons} gallons left\n"
    return main_report
  
        
if __name__ == '__main__':
    #   Primer función
    print(
        first_mission_report(
            14, 
            51, 
            "Moon", 
            200000, 
            300000)
        )
    
    #   Segunda función
    print(
        second_mission_report(
            "Moon", 
            10, 
            15, 
            51, 
            main=300000, 
            external=200000))
    
    #   Tercer función
    print(
        third_mission_report(
            "Moon", 
            8, 
            11, 
            55, 
            main=300000, 
            external=200000))