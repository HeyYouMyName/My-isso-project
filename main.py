from iss import ISS


iss_tracker = ISS()
print(iss_tracker.get_iss_country_currently_above())
print(iss_tracker.create_map_iss_currently_above())
print(iss_tracker.get_current_people_in_space())
