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

def output_tier(t):
    output = ""

    output += '<li class="cards__item">'

    name = get_name(t)
    if name is not None:
        output += f"Name: {name}<br/>\n"

    diet = get_diet(t)
    if diet is not None:
        output += f"Diet: {diet}<br/>\n"

    first_loc = get_first_location(t)
    if first_loc is not None:
        output += f"Location: {first_loc}<br/>\n"

    typ = get_type(t)
    if typ is not None:
        output += f"Type: {typ}<br/>\n"
        
    output += '</li>'

    if output:
        print(output)
        return output
    return ""

def print_tier(data):
    all_output = []
    for animal in data:
        s = output_tier(animal)
        if s:
            all_output.append(s)
    return "\n".join(all_output)

def main():
    with open("animals_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    with open("animals_template.html", "r", encoding="utf-8") as f:
        html = f.read()

        output = print_tier(data)

        new_html = html.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(new_html)

if __name__ == "__main__":
    main()

