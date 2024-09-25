import city_country_csv_reader
from locations import create_example_countries_and_cities
from trip import Trip, create_example_trips
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import csv

def plot_trip(trip: Trip, projection = 'cyl', line_width=2, colour='b') -> None:
    """
    Plots a trip on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.
    """
    routes = f'{trip.trip[0].name}'
    for i in range(len(trip.trip)-1):
        lon1,lon2 = float(trip.trip[i].longitude), float(trip.trip[i+1].longitude)
        lat1,lat2 = float(trip.trip[i].latitude), float(trip.trip[i+1].latitude)
        lon_distance = abs(lon1) + abs(lon2)                #calculate the distance between two coordinates
        lat_distance = abs(lat1) + abs(lat2) 

        if lon_distance > 50 :
            add_lon = 5                                     #extend 5 degrees
        else :
            add_lon = (50 - lon_distance)/2                 #distribute degree equally to both side to ensure size are at least 50 degree
        if lat_distance > 50 :
            add_lat = 5
        else:
            add_lat = (50 - lat_distance)/2

        if (lon2 > lon1) & (lat2 > lat1):
            basemap = Basemap(projection='cyl', lon_0=(lon1 + lon2)/2 , lat_0=(lat1 + lat2)/2,
                              resolution='h', area_thresh=1000.0,
                              llcrnrlon=lon1 - add_lon, llcrnrlat=lat1 - add_lat,
                              urcrnrlon=lon2 + add_lon, urcrnrlat=lat2 + add_lat)
        elif (lon2 > lon1) & (lat2 < lat1):
            basemap = Basemap(projection='cyl', lon_0=(lon1 + lon2)/2 , lat_0=(lat1 + lat2)/2,
                              resolution='h', area_thresh=1000.0,
                              llcrnrlon=lon1 - add_lon, llcrnrlat=lat2 - add_lat,
                              urcrnrlon=lon2 + add_lon, urcrnrlat=lat1 + add_lat)
        elif (lon2 < lon1) & (lat2 < lat1):
            basemap = Basemap(projection='cyl', lon_0=(lon1 + lon2)/2 , lat_0=(lat1 + lat2)/2,
                              resolution='h', area_thresh=1000.0,
                              llcrnrlon=lon2 - add_lon, llcrnrlat=lat2 - add_lat,
                              urcrnrlon=lon1 + add_lon, urcrnrlat=lat1 + add_lat)
        else :  
            basemap = Basemap(projection='cyl', lon_0=(lon1 + lon2)/2 , lat_0=(lat1 + lat2)/2,
                              resolution='h', area_thresh=1000.0,
                              llcrnrlon=lon2 - add_lon, llcrnrlat=lat1 - add_lat,
                              urcrnrlon=lon1 + add_lon, urcrnrlat=lat2 + add_lat)

        basemap.drawgreatcircle(lon1,lat1,lon2,lat2,linewidth=2,color='b')
        basemap.drawcoastlines()
        basemap.fillcontinents()                               #draw the background of the map
        routes += f'_{trip.trip[i+1].name}'

    plt.show()
    plt.savefig(f'map_{routes}.png',dpi = 600, bbox_inches = 'tight')


if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    create_example_countries_and_cities()

    trips = create_example_trips()

    for trip in trips:
        plot_trip(trip)
