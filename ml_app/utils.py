def clean_name(name):
    # join the words 'Land Rover' together to form one word
    if f"{name[0]} {name[1]}" == "Land Rover":
        return f"{name[0]}-{name[1]} {' '.join(name[2:])}"
    elif f"{name[1]} {name[2]}" == "Range Rover":
        return f"{name[0]} {name[1]}-{name[2]} {' '.join(name[3:])}"
    elif name[0] == "Mercedes-Benz" and name[1] == "New":
        return " ".join(name.pop(1))
    elif name[0] == "Fiat" and name[1] == "Grande":
        return " ".join(name.pop(1))
    elif f"{name[1]} {name[2]}" == "Wagon R":
        return f"{name[0]} {name[1]}-{name[2]} {' '.join(name[3:])}"
    elif name[0] == "BMW" and name[2] == "Series":
        return f"{name[0]} {name[1]}-{name[2]} {' '.join(name[3:])}"
    elif name[0] == "Tata" and name[2] == "Safari":
        return f"{name[0]} {name[1]}-{name[2]} {' '.join(name[3:])}"
    elif name[0] == "N" and name[1] == "e" and name[2] == "w":
        return f"{''.join(name)} - -"
    else:
        return name

def process_name(name):
    name = clean_name(name.split())
    name = name.split()
    brand, model, variant = name[0], name[1], " ".join(name[2:])
    return brand, model, variant