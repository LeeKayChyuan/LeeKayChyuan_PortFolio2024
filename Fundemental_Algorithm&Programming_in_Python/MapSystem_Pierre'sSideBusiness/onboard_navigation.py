from city_country_csv_reader import create_cities_countries_from_CSV
from locations import City, Country, create_example_countries_and_cities
from vehicles import Vehicle, create_example_vehicles,CrappyCrepeCar,DiplomacyDonutDinghy,TeleportingTarteTrolley
from trip import Trip, create_example_trips
from mpl_toolkits.basemap import Basemap
from map_plotting import plot_trip
from path_finding import find_shortest_path
import matplotlib.pyplot as plt
import csv
import time

create_cities_countries_from_CSV("worldcities_truncated.csv")

def int_input(prompt="", restrict=None):
    """ 
    This function modifies the input command which allows us to throw an exception whenever user inputs an improper value
    it also allows for restriction of the values that it accepts

    Arguments:
        - prompt: A parameter which accepts string as an argument
        - restrict:  Allows user to pass a list of integers as an argument which restricts the users choice when inputting

    Returns an integer
    """
    while True:
        choice = input(prompt)
        try:
            int_choice = int(choice)
        except ValueError:
            print("Please enter a valid number!")
            continue
        if restrict is None:
            break
        elif int_choice in restrict:
            break
    return int_choice

def fleet_of_vehicles():
    """

    Print options for users to choose for the fleets.
    Return a list of vehicle

    """

    print('1. CrappyCrepeCar(200km/h), DiplomacyDonutDinghy(100km/h, 500km/h), TeleportingTarteTrolley(3h, 2000km), DiplomacyDonutDinghy(300km/h, 700km/h)')
    print('2. CrappyCrepeCar(500km/h), DiplomacyDonutDinghy(300km/h, 700km/h), TeleportingTarteTrolley(2h, 2000km), DiplomacyDonutDinghy(100km/h, 500km/h)')
    print('3. Custom fleet of vehicle')
    fleet_choice = int_input(("Please choose your fleet of vehicles: "),[1,2,3])
    fleet_vehicles = []
    if fleet_choice == 1:                           #user chosen example fleets
        fleet_vehicles = [CrappyCrepeCar(200), DiplomacyDonutDinghy(100, 500), TeleportingTarteTrolley(3, 2000), DiplomacyDonutDinghy(300, 700)]
    elif fleet_choice == 2:
        fleet_vehicles = [CrappyCrepeCar(500), DiplomacyDonutDinghy(300, 700), TeleportingTarteTrolley(2, 2000), DiplomacyDonutDinghy(100, 500)]
    elif fleet_choice == 3:                         #user choose to create custom fleet

        vehicle_choice = 5

        while vehicle_choice != 0:                  
            print('1. CrappyCrepeCar(200)')
            print('2. DiplomacyDonutDinghy(100,500)')
            print('3. TeleportingTarteTrolley(3, 2000)')
            print('4. Custom vehicle')
            print('0. Finish')
            vehicle_choice = int_input(('Please choose your vehicle one by one: '),[1,2,3,4,0])
            
            if vehicle_choice == 1:                 #example vehicles
                fleet_vehicles += [CrappyCrepeCar(200)]
            elif vehicle_choice == 2:
                fleet_vehicles += [DiplomacyDonutDinghy(100,500)]
            elif vehicle_choice == 3:
                fleet_vehicles += [TeleportingTarteTrolley(3,2000)]
           
            elif vehicle_choice == 4:               #customize new vehicle
                print('1. CrappyCrepeCar')
                print('2. DiplomacyDonutDinghy')
                print('3. TeleportingTarteTrolley')
                custom_vehicle_choice = int_input(('Please choose the vehicle type you wish to create: '),[1,2,3]) 


                if custom_vehicle_choice == 1:         #input parameters for initializing the chosen vehicle
                    custom_vehicle_speed = int_input(("The speed of the vehicle in km/h : "))  
                    fleet_vehicles += [CrappyCrepeCar(custom_vehicle_speed)]
                elif custom_vehicle_choice == 2:
                    custom_vehicle_speed = int_input(("The speed of vehicle in normal in km/h : "))
                    custom_vehicle_speed_primary = int_input(("The speed of vehicle moving between capitals in km/h : ")) 
                    fleet_vehicles += [DiplomacyDonutDinghy(custom_vehicle_speed,custom_vehicle_speed_primary)]
                elif custom_vehicle_choice == 3:
                    custom_vehicle_duration = int_input(("The time taken for teleportation in h : ")) 
                    custom_vehicle_radius = int_input(("The radius for teleportation in km : "))
                    fleet_vehicles += [TeleportingTarteTrolley(custom_vehicle_duration,custom_vehicle_radius)]
    
    return fleet_vehicles                              #return list of vehicles


def manually():
    """

    When the user choose to custom trip manually, the input sequence of the user will return by this function as a trip object

    """
    done = False
    while done == False: 
        sequence = list(map(str, input("Enter cities to travel: ").split(' -> '))) #split the user's input by ' -> '
        d_trip = create_trip(sequence)
        if len(sequence) != len(d_trip):                                #if the length of input is different with the trip created
            print('Invalid input! Please try again')                    #prompt input again 
            d_trip = []                             
            continue
        print(f"Cities: {d_trip}")
        print("1. Confirm\n2. Reset")                                   #for user to confirm their choice
        manual_confirm = int_input("Please select a choice: ", [1, 2])
        if manual_confirm == 1:
            done = True
        elif manual_confirm == 2:
            continue
    trip = Trip(d_trip[0])                                               #initialize a trip
    for paths in d_trip[1:]:                                             #add city to the trip list
        trip.add_next_city(paths)                       
    print(f'Your path: {trip}')
    return trip                                                          #return a trip object

def example_path(d_trip):
    """

    When the user choose to use the example trip given, the function will return as trip object.

    """
    trip = Trip(d_trip[0])
    for paths in d_trip[1:]:
        trip.add_next_city(paths)
    return trip

def create_trip(sequence):
    """

    create a trip list with the sequence of the trip

    """
    d_trip = []
    for city in sequence:
        for i in range(len(City.cities.values())):              
            if city.lower() == list(City.cities.values())[i].name.lower():      #check if the input city is valid
                d_trip.append(list(City.cities.values())[i])    
    return d_trip

def chosen_trip():
    """

    Print out options for users to choose for their trip.
    Return trip object

    """
    print('1. Melbourne -> Paris')
    print('2. Sydney -> Tokyo')
    print('3. Make you own trip')
    print('4. Choose your destination and arrival city')
    trip_choice = int_input(('Please choose your trip: '),[1,2,3,4])
    if trip_choice == 1:                                    #user chose example trip 1
        departure = 'melbourne'
        arrival = 'paris'
        sequence = [departure,arrival]
        d_trip = create_trip(sequence)
        print(f'Your path: {example_path(d_trip)}')
        return example_path(d_trip)
    elif trip_choice == 2:                                  #user chose example trip 2
        departure = 'sydney'
        arrival = 'tokyo'
        sequence = [departure,arrival]
        d_trip = create_trip(sequence)
        print(f'Your path: {example_path(d_trip)}')
        return example_path(d_trip)
    if trip_choice == 3:                                    #user chose to define custom trip manually
        return manually()
    if trip_choice == 4:                                    #user chose to custom trip with destin
        return custom_trip_dna()

def custom_trip_dna():
    """
    When the user chooses to use the define custom trip with departure and arrival, the function will return path as trip object.
    Compute the shortest path for each vehicle in user's fleet
    Prints out options for users to finalize their trip
    """
    dna_complete = False
    while dna_complete != True:
        dna_list = []
        depart_flag = True
        arrive_flag = True
        while depart_flag == True:
            depart = input("Please input a departure city: ")
            for i in range(len(City.cities.values())):  # iterates through City.cities
                if depart.lower() == list(City.cities.values())[i].name.lower():    # lowercase the input for departure and checks it against the list of values in City.cities
                    dna_list.append(list(City.cities.values())[i])  # appends to dna_list
                    depart_flag = False
		
        while arrive_flag == True:
            arrive = input("Please input an arrival city: ")
            for i in range(len(City.cities.values())):
                if arrive.lower() == list(City.cities.values())[i].name.lower():    # lowercase the input for arrival and checks it against the list of values in City.cities
                    dna_list.append(list(City.cities.values())[i])
                    arrive_flag = False

        print(f"Destination: {dna_list[0]} Arrival: {dna_list[1]}")
        print("1. Confirm\n2. Reset")
        dna_confirm = int_input("Please select a choice: ", [1, 2])
        if dna_confirm == 1:    # checks for confirmation to proceed or restart 
            dna_complete = True
        elif dna_confirm == 2:  # restart the process
            continue
    
    print(f"You have chosen: \nDestination: {dna_list[0]} Arrival: {dna_list[1]}")

    x = 1
    for vehicle in fleet:
        print("{}. The shortest path for {} from {} to {} is {}".format(x, vehicle, dna_list[0], dna_list[1], find_shortest_path(vehicle, dna_list[0], dna_list[1])))
        x += 1
    
    path_chosen = False
    while path_chosen == False:
        path_choice = int_input("Please choose a path: ")   # changes input to interger and checks if it is within bounds, asks user to enter again if false
        if path_choice > 0 and path_choice <= len(fleet):
            path_chosen = True
        else:
            print("Please enter a proper integer.")

    for vehicle in fleet:
        if fleet.index(vehicle) == (path_choice - 1): 
            print("You have chosen path {}: \nDeparture: {} Arrival: {}\nPath: {}".format(path_choice, dna_list[0], dna_list[1], find_shortest_path(vehicle, dna_list[0], dna_list[1])))
            trip = find_shortest_path(vehicle, dna_list[0], dna_list[1])    #finds the shortest path for all vehicles in fleet
            return trip
            
            
def choose_frmfleet(path,fleet):
    """
    Print out options for user to choose their final vehicle (optimum or others)
    """
    done = False
    valid_choice = False
    fastest = (path.find_fastest_vehicle(fleet))[0]                     #find the fastest vehicle
    while done == False:
        print('1. Choose optimum vehicle from fleet')                 
        print('2. Other vehicles from fleet')
        vehi_choice = int_input(('Enter your choice: '),[1,2])
        if vehi_choice == 1:                                            #user chose the optimum vehicle(fastest)
            print(f'The optimum vehicle: {fastest}')
            print('1. Use the optimum vehicle')
            print('2. Other vehicles from fleet')
            confirm_choice = int_input(('Enter your choice: '),[1,2])
            if confirm_choice == 1:
                print(f'You have chosen vehicle: {fastest}')
                return fastest                                          #return the fastest vehicle
                done = True
            else:
                continue
        else:
            print(f"Choose one from: ")                                 #user chose the other vehicle
            restr = []
            for i in range(len(fleet)):
                print(f'{i+1}. {fleet[i]}')                             #print out each vehicle in the fleet for user to choose
                restr.append(i+1)
            choice = int_input(('Enter your choice: '),restr)
            for vehicle in fleet:
                if fleet.index(vehicle) == choice-1 :
                    print(f'You have chosen vehicle: {vehicle}')
                    done = True
                    return vehicle                                      #return the chosen vehicle
                    
def sim_path(path,vehicle):
    """
    Takes the parameters: trip and vehicle and simulates the trip 
    Returns sequence of travel with every hour represented by 0.1 seconds
    """
    t_time = path.total_travel_time(vehicle)                    #initialises the total time of the trip
    counter = 1
    while counter <= t_time:
        for i in range(len(path.trip)-1):
            travel_time = vehicle.compute_travel_time(path.trip[i], path.trip[i+1])      #compute the travel time between cities
            internal_count = 1
            while internal_count <= travel_time:
                print(f"Travelling from {path.trip[i]} -> {path.trip[i+1]} | Time traveled: {counter} hours")    #print travel statement each hour
                internal_count += 1
                counter += 1
                time.sleep(0.1)
    print(f"Arrived at {path.trip[-1]} | Total time travelled: {t_time} hours")     #final arrival message
    

fleet = fleet_of_vehicles()	
path = chosen_trip()
vehicle = choose_frmfleet(path,fleet)
sim_path(path, vehicle)
plot_trip(path, projection = 'robin', line_width=2, colour='b')
