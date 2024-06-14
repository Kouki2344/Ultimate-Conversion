distance_dict = {
    "mm": {"cm": 0.1, "m": 0.001, "km": 1e-6},
    "cm": {"mm": 10, "m": 0.01, "km": 1e-5},
    "m": {"mm": 1e+6, "cm": 100, "km": 0.001},
    "km": {"mm": 1e+6, "cm": 100000, "m": 1000},
}


time_dict = {
        "ms": {"s": 0.001, "min": 1.66667e-5, "h": 2.77778e-7, "day": 1.15741e-8, "year": 3.17098e-11},
        "s": {"ms": 1000, "min": 0.0166667, "h": 0.000277778, "day": 1.1547e-5, "year": 3.171e-8},
        "min": {"ms":60000, "s": 60, "h": 0.0166667, "day": 0.000694444, "year": 1.9026e-6},
        "h": {"ms": 3.6e+6, "s": 3600, "min": 60, "day": 0.0416667, "year": 0.000114155},
        "day": {"ms": 8.64e+7, "s": 86400, "min": 1440, "h": 24, "year": 0.00273973},
        "year": {"ms": 3.154e+10, "s": 3.154e+7, "min": 525600, "h": 8760, "day": 365},
        }

mass_dict = {
    "mg": {"g": 0.001, "kg": 1e-6, "t": 1e-9},
    "g": {"mg": 1000, "kg": 0.001, "t": 1e-6},
    "kg": {"mg": 1000000, "g": 1000, "t": 0.001},
    "t": {"mg": 1e+9, "g": 1000000, "kg": 1000},
}

# Get amount and units

while True:

    unit = input(str("Unit (distance, time, mass): "))
    if unit == 'Distance' or unit == 'distance' or unit == "DISTANCE":
        from_unit = input("Unit (mm, cm, m, km): ")
        to_unit = input("To Unit (mm, cm, m, km): ")  
        amount = int(input("Amount: "))
        multiply_by = amount * distance_dict[from_unit][to_unit]
        standard = print(f"{multiply_by}{to_unit}")
        print (standard)
    elif unit == 'Time' or unit == 'time' or unit == 'TIME':
        from_unit = input("Unit (ms, s, min, h, day, year): ")
        to_unit = input("To Unit (ms, s, min, h, day, year): ")    
        amount = int(input("Amount: "))
        multiply_by = amount * time_dict[from_unit][to_unit]
        standard = print(f"{multiply_by}{to_unit}")
        print(standard)
    elif unit == 'Mass' or unit == 'mass' or unit == 'MASS':
        from_unit = input("Unit (mg, g, kg, t): ")
        to_unit = input("To Unit (mg, g, kg, t): ")
        amount = int(input("Amount: "))
        multiply_by = amount * mass_dict[from_unit][to_unit]
        standard = print(f"{multiply_by}{to_unit}")
        print(standard)
        
    else:
      print("Invalid Unit")
    if from_unit != ('mm', 'cm', 'm', 'km','ms', 's', 'min', 'h', 'day', 'year', 'mg', 'g', 'kg', 't'):
      print("Invaild unit")