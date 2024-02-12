import logging


class FileWriter:
    @staticmethod
    def write_to_file(data, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(str(data))
        except Exception as e:
            logging.error(f"Error writing to file: {e}")
