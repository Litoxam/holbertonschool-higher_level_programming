#!/usr/bin/env python3
"""Basic Serialization"""

import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as datafile:
        json.dump(data, datafile)


def load_and_deserialize(filename):
    with open(filename, "r") as datafile:
        return json.load(datafile)


if __name__ == "__main__":
    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')

    # Output: The data has been serialized and saved to 'data.json'
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Output: The deserialized data
    print("Deserialized Data:")
    print(deserialized_data)
