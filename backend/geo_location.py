from geopy.distance import geodesic
import json
import os

class GeoLocation():

    def __init__(self) -> None:

        self.cities = {
            "wrocław": (51.1109, 17.0343),
            "legnica": (51.2073, 16.1615),
            "wałbrzych": (50.7732, 16.2845),
            "głogów": (51.6677, 16.0848),
            "jelenia góra": (50.9033, 15.7392),
            "lubin": (51.3962, 16.2003),
            "oława": (50.9458, 17.2827),
            "świdnica": (50.8505, 16.4832),
            "gorzów śląski": (51.0716, 17.5012),
            "środa śląska": (51.1641, 17.2790),
            "polkowice": (51.5045, 16.0710),
            "nowa ruda": (50.5793, 16.5032),
            "kłodzko": (50.4335, 16.6580),
            "zgorzelec": (51.1510, 14.9730),
            "góra": (51.6694, 16.5133),
            "kędzierzyn-koźle": (50.3475, 18.2043),
            "legionowo": (52.3983, 20.9263),
            "bolesławiec": (51.2711, 15.5680),
            "złotoryja": (51.1267, 15.9148),
            "żarów": (51.0632, 16.0462),
            "oleśnica": (51.2057, 17.3883),
            "wołów": (51.4110, 16.6138),
            "ząbkowice śląskie": (50.5931, 16.8405),
            "strzelin": (50.7750, 17.0642),
            "jawor": (51.0593, 16.1913),
            "ziębice": (50.5911, 16.7007),
            "lwówek śląski": (51.1163, 15.6140),
            "środa śląska": (51.1641, 17.2790),
            "góra siewierz": (50.5973, 19.2304),
            "lubań": (51.1166, 15.2916),
            "milicz": (51.5548, 17.2761),
            "paczków": (50.4864, 17.0075),
            "prudnik": (50.3232, 17.6985),
            "strzelce opolskie": (50.4905, 18.2969),
            "bogatynia": (50.9070, 14.9664),
            "lubań": (51.1166, 15.2916),
            "lwówek": (51.1061, 15.5833),
            "legnickie pole": (51.1928, 16.0862),
            "góra": (51.6565, 16.5201),
            "gryfów śląski": (51.0342, 15.5380),
            "pszów": (50.5050, 16.2378),
            "dzierżoniów": (50.7322, 16.6452),
            "ozimek": (50.6246, 18.2152),
            "bierutów": (51.1047, 17.4797),
            "łagiewniki": (51.2434, 19.3930),
            "syców": (51.2906, 17.7063),
            "jaworzyna śląska": (51.0059, 16.4587),
            "nowogrodziec": (51.0692, 14.4514),
            "strzegom": (50.9884, 16.3393),
            "ołobok": (51.1087, 16.3963),
            "krotoszyce": (51.2442, 16.3172),
            "ścinawa": (51.3694, 16.3985),
            "głubczyce": (50.1542, 17.3814),
            "opole": (50.6756, 17.9213),
            "nysa": (50.4724, 17.3317),
            "prusice": (51.0136, 17.3484),
            "dąbrowa": (50.5127, 18.0253),
            "świeradów-zdrój": (50.9031, 15.2852),
            "wąsosz": (51.3956, 17.0596),
            "mieroszów": (50.8374, 16.3442),
            "międzybórz": (51.3966, 16.1865),
            "kraśnik dolny": (51.1881, 17.3023),
            "twardogóra": (51.1680, 17.3890),
            "otmuchów": (50.5146, 17.2905),
            "pszczyna": (49.9773, 18.9482),
            "milówka": (49.6587, 19.2234),
            "gieraltowice": (49.9603, 18.7294),
            "stronie śląskie": (50.2992, 16.7789),
            "łaziska górne": (50.1409, 18.7847),
            "lubawka": (50.7774, 16.1379),
            "bukowno": (50.2853, 19.3897),
            "bartoszyce": (54.2473, 20.8117),
            "chorzów": (50.2909, 18.9703),
            "głuchołazy": (50.3180, 17.3833),
            "przemyśl": (49.7849, 22.7678),
            "świdnica": (50.8529, 16.4910),
            "góra": (51.6701, 16.5147),
            "kędzierzyn-koźle": (50.3486, 18.2079),
            "złotoryja": (51.1264, 15.9164),
            "nowa ruda": (50.5792, 16.5046),
            "paczków": (50.4863, 17.0077),
            "strzelce opolskie": (50.4903, 18.2971),
            "jawor": (51.0592, 16.1921),
            "lwówek": (51.1065, 15.5837),
            "żarów": (51.0628, 16.0467),
            "krotoszyce": (51.2441, 16.3175),
            "strzelin": (50.7746, 17.0639),
            "legnickie pole": (51.1925, 16.0868),
            "góra siewierz": (50.5971, 19.2303),
            "lubań": (51.1165, 15.2918),
            "milicz": (51.5545, 17.2770),
            "bogatynia": (50.9072, 14.9669),
            "łagiewniki": (51.2436, 19.3929),
            "jelenia góra": (50.9032, 15.7394),
            "syców": (51.2903, 17.7067),
            "jaworzyna śląska": (51.0061, 16.4590),
            "nowogrodziec": (51.0694, 14.4518),
            "bierutów": (51.1049, 17.4795),
            "oleśnica": (51.2059, 17.3885),
            "pszów": (50.5047, 16.2380),
            "prudnik": (50.3230, 17.6988),
            "syców": (51.2903, 17.7067),
            "dzierżoniów": (50.7323, 16.6454),
            "ozimek": (50.6248, 18.2156),
            "środa śląska": (51.1641, 17.2790),
            "lwówek śląski": (51.1163, 15.6140),
            "krasiejów": (51.0065, 18.0292),
        }


        self.db_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'databases', 'cities.json'))

    def find_nearby_cities(self, city_name, radius_km):

        if city_name not in self.cities:

            return []

        your_location = self.cities[city_name]
        nearby_cities = []

        for city, coordinates in self.cities.items():
            if city != city_name:

                distance = geodesic(your_location, (coordinates[0], coordinates[1])).kilometers

                if distance <= radius_km:

                    nearby_cities.append(city)

        if nearby_cities == []:

            return None
        
        else:

            return nearby_cities
        
    # def collect_data(self, file_name):

    #     with open(file_name, "r") as json_file:

    #         cities_data = json.load(json_file)

    #     return cities_data



