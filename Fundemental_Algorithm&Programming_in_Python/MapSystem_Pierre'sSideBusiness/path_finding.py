import city_country_csv_reader
from locations import City, Country
from trip import Trip
from vehicles import Vehicle, create_example_vehicles
import networkx as nx
import math


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Trip:
    """
    Returns a shortest path between two cities for a given vehicle,
    or None if there is no path.
    """
    G = nx.Graph()
    city_list = list(City.cities.values())  # creates a city list using the values from the City.cities dictionary
    G.add_nodes_from(city_list) # adds each city object from the list as a node 
    for city in city_list:  # iterate though each city in the list
        for city2 in city_list: # against all other cities
            if city != city2 and vehicle.compute_travel_time(city, city2) != math.inf:  # if 1st city and 2nd city are not the same and travel time does not equal math.inf
                G.add_edge(city, city2, weight = vehicle.compute_travel_time(city, city2))  # add an from node city to node city2 with travel time being the weight
    try:
        path = nx.shortest_path(G, from_city, to_city)  # use shortest_path function to look for shortest path between two nodes
    except:
        return None
    
    trip = Trip(path[0])    # calls Trip class with index 0 of path as argument (departure)
    for paths in path[1:]:  # loops through all other indexes starting from index 1 to end
        trip.add_next_city(paths)   # adds it to the trip sequence
    return trip
        


if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")
    vehicles = create_example_vehicles()

    australia = Country.countries["Australia"]
    melbourne = australia.get_city("Melbourne")
    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")

    for vehicle in vehicles:
        print("The shortest path for {} from {} to {} is {}".format(vehicle, melbourne, tokyo, find_shortest_path(vehicle, melbourne, tokyo)))
