import json

def gas_law(P: float = None, V: float = None, T: float = None, n: float = 1, formula: str = "ideal", chemical_formula: str = None, R_unit: str = 'J/molK'):
    def const(const: str):
        formula_info = formula_dict[formula]

        with open(formula_info["file"], encoding="utf8") as file:
            file_contents = file.read()
            parsed_json = json.loads(file_contents)
        
        list = parsed_json[formula_info["list"]]
        item = formula_info["searching algo"](list)
        return item[const]


    null_count = sum(x is None for x in [P, V, T])
    if null_count != 1:
        print('at least one value should be missing')
        return
    R_dict = {
        'J/molK': 8.314,
        'Latm/molK': 0.0821
    }
    R = R_dict[R_unit]
    formula_dict = {
        'ideal': {
            'P': lambda: (n * R * T / V),
            'V': lambda: (n * R * T / P),
            'T': lambda: (P * V / (n * R)),
        },
        'van der Waals': {
            'P': lambda: (n * R * T / (V - n * const('b')) - const('a') * n**2 / V**2),
            'V': lambda: (n * R * T / P),
            'T': lambda: (P * V / (n * R)),
            'file': 'vdw.json',
            'list': 'varDerWaalsConstants',
            'searching algo': lambda list: [x for x in list if x["gas"] == chemical_formula][0]
        }
    }

    missing = 'P' if P is None else 'V' if V is None else 'T' if T is None else 'one should be missing'

    return formula_dict[formula][missing]()


print(gas_law(formula='van der Waals', V=4.7, T=326, chemical_formula="CO2", n=2.75, R_unit='Latm/molK'))