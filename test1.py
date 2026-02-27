"""
XML Parsing Demo in Python
This script demonstrates how to parse XML data and extract values.
"""

import xml.etree.ElementTree as ET

# Sample XML string
xml_string = '''<?xml version="1.0" encoding="UTF-8"?>
<book id="1">
    <title>The Great Gatsby</title>
    <author>F. Scott Fitzgerald</author>
    <year>1925</year>
    <genres>
        <genre>Fiction</genre>
        <genre>Classic</genre>
    </genres>
    <available>true</available>
</book>
'''

# Parse XML string
root = ET.fromstring(xml_string)

# Access data from the parsed XML
print("Book ID:", root.attrib["id"])
print("Title:", root.find("title").text)
print("Author:", root.find("author").text)
print("Year:", root.find("year").text)

# Access nested elements (genres)
genres = root.find("genres")
genre_list = [genre.text for genre in genres.findall("genre")]
print("Genres:", ", ".join(genre_list))

# Access boolean (stored as string in XML)
available_text = root.find("available").text
available = available_text.lower() == "true"
print("Available:", available)


# Modify the XML

# Updating existing property
root.find('title').text = "The Great Gatsby!!!"

# Creating new property with ET.SubElement
rating = ET.SubElement(root, "rating")
rating.text = "4.5"

# Add a new genre
new_genre = ET.SubElement(genres, "genre")
new_genre.text = "Literary"

# Convert back to string
modified_xml = ET.tostring(root, encoding="unicode")
print("\nModified XML:")
print(modified_xml)