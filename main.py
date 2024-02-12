from iss_spy import ISSSpy


def main():
    iss_spy = ISSSpy()

    print(iss_spy.create_map_and_mark_place_where_iss_currently_above("your_map"))
    print(iss_spy.write_iss_position_to_txt_file("iss_position"))
    print(iss_spy.write_people_in_space_into_txt_file("people_in_space"))


if __name__ == "__main__":
    main()
    