#!/usr/bin/env python3
"""Converting CSV Data to JSON Format"""


import csv
import json


def convert_csv_to_json(filename):
    """Open csv file and then write it into json file"""
    try:
        with open(filename, mode='r') as csvfile:
            csv_data = list(csv.DictReader(csvfile))
        with open("data.json", 'w', encoding="utf-8") as jsonfile:
            json.dump(csv_data, jsonfile)
        return True
    except FileNotFoundError:
        return False


if __name__ == "__main__":
    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")
