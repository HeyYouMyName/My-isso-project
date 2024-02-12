import logging

import requests


class ApiClient:
    BASE_URL = "http://api.open-notify.org/"

    def get_iss_current_position(self):
        try:
            response = requests.get(url=f"{self.BASE_URL}iss-now.json")
            data = response.json()
            return data["iss_position"]["latitude"], data["iss_position"]["longitude"]
        except requests.RequestException as e:
            logging.error(f"Error fetching ISS position: {e}")

    def get_current_people_in_space(self):
        try:
            response = requests.get(url=f"{self.BASE_URL}astros.json")
            json_data = response.json()
            people_names = '\n'.join([person['name'] for person in json_data['people']])
            return people_names
        except requests.RequestException as e:
            logging.error(f"Error fetching people in space: {e}")
