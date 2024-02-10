from iss import ISS


def main():
    iss_tracker = ISS()
    print(iss_tracker.find_place_iss_currently_above_and_write_into_txt_file())
    print(iss_tracker.create_map_and_mark_place_where_iss_currently_above())
    print(iss_tracker.create_current_people_in_space_txt_file())


if __name__ == "__main__":
    main()