from locations import City, Country, test_example_countries_and_cities
import csv
def create_cities_countries_from_CSV(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.
    Checks 1st row for column names and gets the index of each column and assigns them to their respective variables

    Arguments: 
    path_to_csv: A string which accepts a csv file as an argument

    Creates instances of City and Country objects
    """
    country_list = []
    with open(path_to_csv, "r") as file:
        csv_reader = csv.reader(file)
        
        col_name = next(csv_reader) # reads the 1st line of the csv file 
        city_ascii = col_name.index('city_ascii')   # gets index of city_ascii from the 1st line and assigns it to variable city_ascii
        lat = col_name.index('lat') # following codes do the same as above for their respective variables
        lng = col_name.index('lng')
        country = col_name.index('country')
        iso3 = col_name.index('iso3')
        capital = col_name.index('capital')
        city_id = col_name.index('id')

        for line in csv_reader: # iterates through each line of the csv file
            if line[country] not in country_list:   # if a specific country object has not been created
                Country(line[country], line[iso3])  # creates the country object
                country_list.append(line[country])  # appends it to the country list
            City(line[city_ascii], line[lat], line[lng], line[country], line[capital], line[city_id])   # creates a city object 
            

if __name__ == "__main__":
    create_cities_countries_from_CSV("worldcities_truncated.csv")
    test_example_countries_and_cities()
    
