from geopy.distance import geodesic
import json
import os

class GeoLocation():

    def __init__(self) -> None:

        self.db_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'databases', 'cities.json'))


    def find_nearby_cities(self, city_name, radius_km, city_data):

        if city_name not in city_data:

            return []

        your_location = city_data[city_name]
        nearby_cities = []

        for city, coordinates in city_data.items():
            if city != city_name:

                distance = geodesic(your_location, (coordinates[0], coordinates[1])).kilometers

                if distance <= radius_km:

                    nearby_cities.append(city)

        if nearby_cities == []:

            return None
        
        else:

            return nearby_cities
        
    def collect_data(self, file_name):

        with open(file_name, "r") as json_file:

            cities_data = json.load(json_file)

        return cities_data



