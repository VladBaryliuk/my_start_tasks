solar_system = {'Jupiter': 1321,
                'Mars': 0.15,
                'Saturn': 764}
solar_system["Uranus"] = 63
solar_system['Mercury'] = 0.05
solar_system['Venus'] = 0.86
solar_system['Neptune'] = 57.7
solar_system['Pluto'] = 0.059
solar_system['Earth'] = 1
solar_system.pop("Pluto")
for key in solar_system:
    if solar_system[key] > 1:
        print(key)
for key in solar_system:
    if key[0] == "M":
        print(key)
