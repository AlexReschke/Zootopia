import json

def get_name(t):
    return t.get("name")

def get_diet(t):
    ch = t.get("characteristics", {})
    return ch.get("diet")

def get_first_location(t):
    locs = t.get("locations")
    if isinstance(locs, list) and len(locs) > 0:
        return locs[0]

def get_type(t):
    ch = t.get("characteristics", {})
    tpe = ch.get("type")
    if tpe is None:
        return None
    else:
        return tpe

def print_tier(t):
    parts = []

    name = get_name(t)
    if name is not None:
        parts.append(f"Name: {name}")

    diet = get_diet(t)
    if diet is not None:
        parts.append(f"Diet: {diet}")

    first_loc = get_first_location(t)
    if first_loc is not None:
        parts.append(f"Location: {first_loc}")

    typ = get_type(t)
    if typ is not None:
        parts.append(f"Type: {typ}")

    if parts:
        print("\n".join(parts))
        print()

def main():
    with open("animals_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

        for animal in data:
            print_tier(animal)

if __name__ == "__main__":
    main()

