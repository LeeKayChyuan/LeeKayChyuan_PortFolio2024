from abc import ABC, abstractmethod
from locations import CapitalType, City, Country
from locations import create_example_countries_and_cities
import math
class Vehicle(ABC):
    """
    A Vehicle defined by a mode of transportation, which results in a specific duration.
    """

    @abstractmethod
    def compute_travel_time(self, departure: City, arrival: City) -> float:
        """
        Returns the travel duration of a direct trip from one city
        to another, in hours, rounded up to an integer.
        Returns math.inf if the travel is not possible.
        """
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns the class name and the parameters of the vehicle in parentheses.
        """
        raise NotImplementedError


class CrappyCrepeCar(Vehicle):
    """
    A type of vehicle that:
        - Can go from any city to any other at a given speed.
    """

    def __init__(self, speed: int) -> None:
        """
        Creates a CrappyCrepeCar with a given speed in km/h.
        """
        self.speed = speed

    def compute_travel_time(self, departure: City, arrival: City) -> float:
        """
        Returns the travel duration of a direct trip from one city
        to another, in hours, rounded up to an integer.
        """
        dist = departure.distance(arrival)
        time = round(dist) / self.speed
        return math.ceil(time)

    def __str__(self) -> str:
        """
        Returns the class name and the parameters of the vehicle in parentheses.
        For example "CrappyCrepeCar (100 km/h)"
        """
        return f"{self.__class__.__name__} ({self.speed} km/h)"


class DiplomacyDonutDinghy(Vehicle):
    """
    A type of vehicle that:
        - Can travel between any two cities in the same country.
        - Can travel between two cities in different countries only if they are both "primary" capitals.
        - Has different speed for the two cases.
    """

    def __init__(self, in_country_speed: int, between_primary_speed: int) -> None:
        """
        Creates a DiplomacyDonutDinghy with two given speeds in km/h:
            - one speed for two cities in the same country.
            - one speed between two primary cities.
        """
        self.in_country_speed = in_country_speed
        self.between_primary_speed = between_primary_speed

    def compute_travel_time(self, departure: City, arrival: City) -> float:
        """
        Returns the travel duration of a direct trip from one city
        to another, in hours, rounded up to an integer.
        Returns math.inf if the travel is not possible.
        """
        if departure.country == arrival.country:
            dist = departure.distance(arrival)
            time = dist / self.in_country_speed
            return math.ceil(time)
        elif departure.capital_type == "primary" and arrival.capital_type == "primary":
            dist = departure.distance(arrival)
            time = dist / self.between_primary_speed
            return math.ceil(time)
        return math.inf


    def __str__(self) -> str:
        """
        Returns the class name and the parameters of the vehicle in parentheses.
        For example "DiplomacyDonutDinghy (100 km/h | 200 km/h)"
        """
        return f"{self.__class__.__name__} ({self.in_country_speed} km/h | {self.between_primary_speed} km/h)"


class TeleportingTarteTrolley(Vehicle):
    """
    A type of vehicle that:
        - Can travel between any two cities if the distance is less than a given maximum distance.
        - Travels in fixed time between two cities within the maximum distance.
    """

    def __init__(self, travel_time:int, max_distance: int) -> None:
        """
        Creates a TarteTruck with a distance limit in km.
        """
        self.travel_time = travel_time
        self.max_distance = max_distance

    def compute_travel_time(self, departure: City, arrival: City) -> float:
        """
        Returns the travel duration of a direct trip from one city
        to another, in hours, rounded up to an integer.
        Returns math.inf if the travel is not possible.
        """
        dist = departure.distance(arrival)
        if dist < self.max_distance:
            return self.travel_time
        
        return math.inf

    def __str__(self) -> str:
        """
        Returns the class name and the parameters of the vehicle in parentheses.
        For example "TeleportingTarteTrolley (5 h | 1000 km)"
        """
        return f"{self.__class__.__name__} ({self.travel_time} h | {self.max_distance} km)"


def create_example_vehicles() -> list[Vehicle]:
    """
    Creates 3 examples of vehicles.
    """
    return [CrappyCrepeCar(200), DiplomacyDonutDinghy(100, 500), TeleportingTarteTrolley(3, 2000)]


if __name__ == "__main__":
    create_example_countries_and_cities()
    france = Country.countries["France"]
    paris = france.get_city("Paris")
    australia = Country.countries["Australia"]
    melbourne = australia.get_city("Melbourne")
    canberra = australia.get_city("Canberra")
    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")

    vehicles = create_example_vehicles()

    for vehicle in vehicles:
        for from_city, to_city in [(melbourne, paris), (tokyo, canberra), (tokyo, melbourne)]:
            print("Travelling from {} to {} will take {} hours with {}".format(from_city, to_city, vehicle.compute_travel_time(from_city, to_city), vehicle))
