from CoolProp.CoolProp import PropsSI

temperature = 373.15
pressure = 101325

enthalpy = PropsSI('H', 'T', temperature, 'P', pressure, 'Water')
entropy = PropsSI('S', 'T', temperature, 'P', pressure, 'Water')
specific_volumne = 1 / PropsSI('D', 'T', temperature, 'P', pressure, 'Water')
density = 1 / specific_volumne

print(f"Enthalpy: {enthalpy} J/kg")
print(f"Entropy: {entropy} J/K.kg")
print(f"Specific Volume: {specific_volumne} m^3/kg")
print(f"Density: {density} kg/m^3")
