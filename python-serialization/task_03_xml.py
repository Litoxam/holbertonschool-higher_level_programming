#!/usr/bin/env python3
"""Serializing and Deserializing with XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    data = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(data, key)
        item.text = value
    xmlstring = ET.tostring(data, encoding="unicode")

    with open(filename, 'w') as xmlfile:
        xmlfile.write(xmlstring)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for elem in root:
        dictionary[elem.tag] = elem.text
    return dictionary


if __name__ == "__main__":

    def main():
        sample_dict = {
            'name': 'John',
            'age': '28',
            'city': 'New York'
        }

        xml_file = "data.xml"
        serialize_to_xml(sample_dict, xml_file)
        print(f"Dictionary serialized to {xml_file}")

        banane = deserialize_from_xml(xml_file)
        print("\nDeserialized Data:")
        print(banane)

    main()
