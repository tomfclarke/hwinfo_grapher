import csv
import re
from datetime import datetime


def parse_csv(csv_file_path):
    """ Parses a CSV file and generates a JSON (dict) array """
    json = []
    with open(csv_file_path, encoding='unicode-escape') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            json.append(row)
    # last two rows contain a repeat of keys and system info
    return json[:len(json)-2]


def extract_values(json_array, key):
    """ Obtain all values for a key in the JSON (dict) array """
    return [item[key] for item in json_array]


def to_numbers(string_array):
    """ Convert an array of strings to floating point numbers """
    return [float(string) for string in string_array]


def to_datetimes(date_array, time_array):
    """ Convert date and time values to datetime objects for plotting """
    datetimes = []
    for date, timestamp in zip(date_array, time_array):
        day, month, year = date.split('.')
        hour, minute, second = timestamp.split(':')
        second, microsecond = second.split('.')
        dt = datetime(
            int(year),
            int(month),
            int(day),
            int(hour),
            int(minute),
            int(second),
            int(microsecond))
        datetimes.append(dt)
    return datetimes


def find_units(keys):
    """ Find all unique units in a list of keys """
    units = set()
    for key in keys:
        units.add(re.search('\[.*\]', key).group(0))
    return list(units)