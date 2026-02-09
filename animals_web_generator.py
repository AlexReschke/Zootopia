import json

def get_name(t):
    """get the name out of animal_data.json"""
    return t.get("name")

def get_diet(t):
    """get the diet out of animal_data.json"""
    ch = t.get("characteristics", {})
    return ch.get("diet")

def get_first_location(t):
    """get the location out of animal_data.json"""
    locs = t.get("locations")
    if isinstance(locs, list) and len(locs) > 0:
        return locs[0]

def get_type(t):
    """get the type out of animal_data.json"""
    ch = t.get("characteristics", {})
    tpe = ch.get("type")
    return tpe

def output_html(t):
    """create the output list and format the html for the cards"""
    output = ""
    output += '<li class="cards__item">'

    name = get_name(t)
    if name is not None:
        output += f'<div class="card__title">{name}</div>'
        output += '<div class="card__text">'
        output += '<ul>'

        diet = get_diet(t)
        if diet is not None:
            output += f'<li><strong>Diet:</strong> {diet}</li>'

        first_loc = get_first_location(t)
        if first_loc is not None:
            output += f'<li><strong>Location:</strong> {first_loc}</li>'

        typ = get_type(t)
        if typ is not None:
            output += f'<li><strong>Type:</strong> {typ}</li>'

        output += '</ul>'

        output += '</div>'
    output += '</li>'

    if output:
        return output
    return ""

def iter_data(data):
    """iterates through the data of animal_data.json"""
    all_output = []
    for animal in data:
        s = output_html(animal)
        if s:
            all_output.append(s)
    return "\n".join(all_output)

def main():
    with open("animals_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    with open("animals_template.html", "r", encoding="utf-8") as f:
        html = f.read()

        output = iter_data(data)

        new_html = html.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(new_html)

if __name__ == "__main__":
    main()

