import json
import xml.etree.ElementTree as etree

"""
has a parsed_data() method that returns all data as a dictionary (dict). 
The property decorator is used to make parsed_data() appear 
as a normal attribute instead of a method
"""
class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)
    @property
    def parsed_data(self):
        return self.data
"""
 parses the XML file 
 and has a parsed_data() method that returns all data as a list of xml.etree.Element
"""
class XMLDataExtractor:
    def __init__(self, filepath): 
        self.tree = etree.parse(filepath) 
    @property
    def parsed_data(self):
        return self.tree

# factory method. It returns an instance of JSONDataExtractor or XMLDataExtractor 
# depending on the extension of the input file
def dataextraction_factory(filepath): 
    if filepath.endswith('json'):
        extractor = JSONDataExtractor 
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor 
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath)) 
    return extractor(filepath)

# a wrapper of dataextraction_factory().
# adds exception handling
def extract_data_from(filepath): 
    factory_obj = None
    try:
        factory_obj = dataextraction_factory(filepath) 
    except ValueError as e:
           print(e)
    return factory_obj

json_factory = extract_data_from('./movies.json') 
json_data = json_factory.parsed_data
print(f'Found: {len(json_data)} movies')
for movie in json_data:
    print(f"Title: {movie['title']}") 
    year = movie['year']
    if year:
        print(f"Year: {year}")
    director = movie['director'] 
    if director: 
        print(f"Director: {director}") 
    genre = movie['genre']
    if genre:
        print(f"Genre: {genre}")
        print()

xml_factory = extract_data_from('./person.xml') 
xml_data = xml_factory.parsed_data
liars = xml_data.findall(f".//person[lastName='Liar']") 
print(f'found: {len(liars)} persons')
for liar in liars:
    firstname = liar.find('firstName').text 
    print(f'first name: {firstname}')
    lastname = liar.find('lastName').text
    print(f'last name: {lastname}')
    [print(f"phone number ({p.attrib['type']}):", p.text) for p in liar.find('phoneNumbers')]
    print()