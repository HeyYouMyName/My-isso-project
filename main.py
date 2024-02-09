import time
import requests
from geopy.geocoders import Nominatim
from datetime import datetime


def get_iss_current_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return iss_latitude, iss_longitude


# print(get_iss_current_position())


def where_is_iss():
    geolocator = Nominatim(user_agent="your_app_name")

    latitude_longitude_list = get_iss_current_position()
    latitude, longitude = get_iss_current_position()

    address = geolocator.reverse((latitude, longitude))

    country = address.address.get("country_code")

    print(f"The country at these coordinates is: {country}")

where_is_iss()