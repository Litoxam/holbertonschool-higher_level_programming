#!/usr/bin/env python3
"""Converting CSV Data to JSON Format"""


import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, mode='r') as csvfile:
            csv_data = csv.DictReader(csvfile)
        with open("data.json", 'w', encoding="utf-8") as jsonfile:
            json.dump(csv_data, jsonfile)
        return True
    except Exception:
        return False
