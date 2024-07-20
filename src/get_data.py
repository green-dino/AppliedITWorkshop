import logging
from data_readers import TextReader, CSVReader , JSONReader

#configure logging
logging.basicConfig(level=logging.INFO)

text_reader = TextReader("example.txt")

text_data = text_reader.read()

print("Text Data:", text_data)

# create for CSV and JSON Reader 

csv_reader = CSVReader("example.csv")
csv_data = csv_reader.read()

print("CSV Data", csv_data)