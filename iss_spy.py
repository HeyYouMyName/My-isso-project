import folium
import logging
from geopy.geocoders import Nominatim

from api_client import ApiClient
from file_writer import FileWriter


class ISSSpy:

    def __init__(self):
        self.geolocator = Nominatim(user_agent="ISS_tracker")
        self.api_client = ApiClient()

    def find_place_iss_currently_above(self):
        latitude, longitude = self.api_client.get_iss_current_position()
        address = self.geolocator.reverse((latitude, longitude))
        if address is None:
            raise ValueError("Unable to determine ISS location.")
        else:
            return address

    def create_map_and_mark_place_where_iss_currently_above(self, name_your_map) -> None:
        latitude, longitude = self.api_client.get_iss_current_position()
        if latitude is None or longitude is None:
            raise ValueError("Unable to create map due to missing ISS location.")
        else:
            folium_map_object = folium.Map(location=(latitude, longitude), zoom_start=6)
            folium.Marker((latitude, longitude)).add_to(folium_map_object)
            folium_map_object.save(f'{name_your_map}.html')

    def write_iss_position_to_txt_file(self, name_of_txt_file):
        try:
            FileWriter.write_to_file(self.find_place_iss_currently_above(), f"{name_of_txt_file}.txt")
        except Exception as e:
            logging.error(f"Error writing ISS position to {name_of_txt_file}.txt: {e}")

    def write_people_in_space_into_txt_file(self, name_of_txt_file):
        try:
            FileWriter.write_to_file(self.api_client.get_current_people_in_space(), f"{name_of_txt_file}.txt")
        except Exception as e:
            logging.error(f"Error writing people in space to {name_of_txt_file}.txt: {e}")
