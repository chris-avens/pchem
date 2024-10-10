from chem import get_composition, molecular_mass, get_element_property
from gas import gas_law

def calculate_molar_mass():
    # chemical_formula = "CH2CHCl"
    chemical_formula = input("chemical formula: ")
    print(get_composition(chemical_formula))
    print(f'molecular mass of {chemical_formula}: {molecular_mass(chemical_formula)}')

def write_element_property():
    element = input("element symbol: ")
    property = input("property: ")
    name = get_element_property(element, 'name')
    property_value = get_element_property(element, property)
    print(f'{property.replace('_', " ")} of {name} ({element}): {property_value}')

def get_missing_gas_condition():
    # print(gas_law(1,2,3))
    print('Indicate the values of condition below, put None if it is the missing condition.')
    P = input('Pressure: ')
    V = input('Volume: ')
    T = input('Temperature: ')
    if(V is None):
        print('V is None')
    if(V == "None"):
        print('V is "None"')
    P = None if P == "None" else float(P)
    V = None if V == "None" else float(V)
    T = None if T == "None" else float(T)
    # print(f'Pressure: {gas_law(V=0.024464, T=298.15)} Pa')
    # print(f'Volume: {gas_law(P=101325, T=298.15)} m^3')
    missing = 'Pressure' if P is None else 'Volume' if V is None else 'Temperature'
    unit = 'Pa' if P is None else 'm^3' if V is None else 'K'
    print(P, V, T)
    print(f'{missing}: {gas_law(P, V, T)} {unit}')


to_calculate = input('what do you want to calculate?  ')
procedures = {
    "molar mass": lambda: (calculate_molar_mass()),
    "element property": lambda: (get_element_property()),
    "gas condition": lambda: (get_missing_gas_condition()),
}

procedures[to_calculate]()






