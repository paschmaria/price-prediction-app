def clean_name(name):
    
    # join the words 'Land Rover' together to form one word
    if f"{name[0]} {name[1]}" == "Land Rover":
        return f"{name[0]}-{name[1]} {' '.join(name[2:])}"
    # join the words 'Range Rover' together to form one word
    elif f"{name[1]} {name[2]}" == "Range Rover":
        return f"{name[0]} {name[1]}-{name[2]} {' '.join(name[3:])}"
    # Remove the word 'New' from Mercedes-Benz
    elif name[0] == "Mercedes-Benz" and name[1] == "New":
        return " ".join(name.pop(1))
    # Replace words 'Grande Punto' with Punto
    elif name[0] == "Fiat" and name[1] == "Grande":
        return " ".join(name.pop(1))
    # combine words 'Wagon R' into one
    elif f"{name[1]} {name[2]}" == "Wagon R":
        return f"{name[0]} {name[1]}-{name[2]} {' '.join(name[3:])}"
    # join '{num} Series' together for BMWs
    elif name[0] == "BMW" and name[2] == "Series":
        return f"{name[0]} {name[1]}-{name[2]} {' '.join(name[3:])}"
    # join 'New Safari' together for Tata
    elif name[0] == "Tata" and name[2] == "Safari":
        return f"{name[0]} {name[1]}-{name[2]} {' '.join(name[3:])}"
    # join name with letters 'N e w' together to form one word
    elif name[0] == "N" and name[1] == "e" and name[2] == "w":
        return f"{''.join(name)} - -"
    else:
        return ' '.join(name)

def process_name(name):
    name = clean_name(name.split())
    name = name.split()
    brand, model, variant = name[0], name[1], " ".join(name[2:])
    return brand, model, variant


# {
# "name": "Maruti Alto K10 LXI CNG",
# "location": "Delhi",
# "year": 2014,
# "km_driven": 40929,
# "fuel_type": "CNG",
# "transmission": "Manual",
# "owner_type": "First",
# "mileage": 32.26,
# "engine": 998,
# "power": 58.2,
# "seats": 4
# }