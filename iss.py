import requests
import folium
from geopy.geocoders import Nominatim


class ISS:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="ISS_tracker")

    @staticmethod
    def _get_iss_current_position():
        try:
            response = requests.get(url="http://api.open-notify.org/iss-now.json")
            response.raise_for_status()
            data = response.json()
            return float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"])
        except requests.RequestException as e:
            print(f"Error fetching ISS position: {e}")
            return None, None

    def get_iss_country_currently_above(self):
        latitude, longitude = self._get_iss_current_position()
        if latitude is not None and longitude is not None:
            address = self.geolocator.reverse((latitude, longitude))
            if address is not None:
                return address
            else:
                return "Unable to determine ISS location."
        else:
            return "Unable to determine ISS location."

    def create_map_iss_currently_above(self):
        latitude, longitude = self._get_iss_current_position()
        if latitude is not None and longitude is not None:
            folium_map_object = folium.Map(location=[latitude, longitude], zoom_start=6)
            folium.Marker([latitude, longitude]).add_to(folium_map_object)
            folium_map_object.save("my_map.html")
            return "Map saved as my_map.html"
        else:
            return "Unable to create map due to missing ISS location."

    @staticmethod
    def get_current_people_in_space():
        try:
            response = requests.get(url="http://api.open-notify.org/astros.json")
            response.raise_for_status()
            data_json = response.json()
            return [people["name"] for people in data_json["people"]]
        except requests.RequestException as e:
            print(f"Error fetching people in space: {e}")
            return []
