import json, re
from collections import defaultdict

with open('PeriodicTable.json', encoding="utf8") as file:
    file_contents = file.read()
    parsed_json = json.loads(file_contents)

def get_element_property(symbol: str, property: str):
    element_dict = [x for x in parsed_json["elements"] if x["symbol"] == symbol][0]
    return element_dict[property]

def molecular_mass(chemical_formula: str) -> float:
    composition = get_composition(chemical_formula)
    mass = 0
    for element in composition:
        atomic_mass = get_element_property(element, "atomic_mass")
        mass += atomic_mass * composition[element]
        print(element, composition[element], atomic_mass)
    
    return mass

def get_composition(chemical_formula: str) -> dict:
    element_pattern = r"([A-Z][a-z]?)(\d*)"
    element_counts = defaultdict(int)

    matches = re.findall(element_pattern, chemical_formula)

    for element, count in matches:
        count = int(count) if count else 1
        element_counts[element] += count
    
    return dict(element_counts)