from vehicles import Vehicle, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley
from vehicles import create_example_vehicles
from locations import City, Country
from locations import create_example_countries_and_cities
import math


class Trip():
    """
    Represents a sequence of cities.
    """

    def __init__(self, departure: City) -> None:
        """
        Initialises a Trip with a departure city.
        """
        self.departure = departure
        self.trip = [departure]                         #initialise a list of the trip

    def add_next_city(self, city: City) -> None:
        """
        Adds the next city to this trip.
        """
        self.trip.append(city)                          #append city to the list of trip

    def total_travel_time(self, vehicle: Vehicle) -> float:
        """
        Returns a travel duration for the entire trip for a given vehicle.
        Returns math.inf if any leg (i.e. part) of the trip is not possible.
        """
        total_time = 0
        for i in range(len(self.trip)-1):
            travel_time = vehicle.compute_travel_time(self.trip[i], self.trip[i+1])     #compute the total_time
            if travel_time == math.inf:
                return math.inf                         #if part of the trip is not possible, return infinity
            total_time += travel_time
        return total_time

    def find_fastest_vehicle(self, vehicles: list[Vehicle]) -> (Vehicle, float):
        """
        Returns the Vehicle for which this trip is fastest, and the duration of the trip.
        If there is a tie, return the first vehicle in the list.
        If the trip is not possible for any of the vehicle, return (None, math.inf).
        """
        min_dur = math.inf
        min_dur_vehicle = None
        for vehicle in vehicles:
            travel_time = self.total_travel_time(vehicle)       #compute the total time
            if travel_time < min_dur:
                min_dur = travel_time
                min_dur_vehicle = vehicle                       #find vehicle with shortest travel duration
        if min_dur == math.inf:
            return (None, math.inf)
        return (min_dur_vehicle, min_dur)                       #return the fastest vehicle and the shortest time taken

    def __str__(self) -> str:
        """
        Returns a representation of the trip as a sequence of cities:
        City1 -> City2 -> City3 -> ... -> CityX
        """
        if len(self.trip)==1:
            return f'{self.departure}'
        sequence = f'{self.departure}'
        for city in self.trip[1:]:
            sequence += f' -> {city}'   
        return sequence                                         #print the sequence of the trip

def create_example_trips() -> list[Trip]:
    """
    Creates examples of trips.
    """

    #first we create the cities and countries
    create_example_countries_and_cities()

    australia = Country.countries["Australia"]
    melbourne = australia.get_city("Melbourne")
    sydney = australia.get_city("Sydney")
    canberra = australia.get_city("Canberra")
    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")

    #then we create trips
    trips = []

    for cities in [(melbourne, sydney), (canberra, tokyo), (melbourne, canberra, tokyo), (canberra, melbourne, tokyo)]:
        trip = Trip(cities[0])
        for city in cities[1:]:
            trip.add_next_city(city)

        trips.append(trip)
        
    return trips


if __name__ == "__main__":
    vehicles = create_example_vehicles()
    trips = create_example_trips()

    for trip in trips:
        print(trip)
        vehicle, duration = trip.find_fastest_vehicle(vehicles)
        print("The trip {} will take {} hours with {}".format(trip, duration, vehicle))
