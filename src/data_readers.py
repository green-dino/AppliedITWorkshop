import csv
import json
import logging


def batched(iterable, n):
    """Helper function to split an iterable into batches of size n."""
    for i in range(0, len(iterable), n):
        yield iterable[i : i + n]


class Reader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        raise NotImplementedError("Subclasses must implement this method")


class TextReader(Reader):
    def read(self):
        try:
            with open(self.filename, encoding="utf-8") as file:
                for batch in batched(file.readlines(), 3):
                    yield [item.strip() for item in batch]
        except FileNotFoundError:
            logging.error(f"File not found: {self.filename}")
        except Exception as e:
            logging.error(f"An error occurred while reading {self.filename}: {e}")


class CSVReader(Reader):
    def read(self):
        try:
            with open(self.filename, encoding="utf-8", newline="") as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            logging.error(f"File not found: {self.filename}")
        except Exception as e:
            logging.error(f"An error occurred while reading {self.filename}: {e}")


class JSONReader(Reader):
    def read(self):
        try:
            with open(self.filename, encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error(f"File not found: {self.filename}")
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from file: {self.filename}")
        except Exception as e:
            logging.error(f"An error occurred while reading {self.filename}: {e}")
