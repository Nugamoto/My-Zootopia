import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_name(animal):
    return animal["name"]


def get_diet(animal):
    return animal["characteristics"]["diet"] if "diet" in animal["characteristics"] else False


def get_locations(animal):
    return animal["locations"]


def get_type(animal):
    return animal["characteristics"]["type"] if "type" in animal["characteristics"] else False


def load_html(file_path):
    """ Loads an HTML file """
    with open(file_path, "r") as handle:
        return handle.read()


def save_document(new_file_name, file):
    with open(new_file_name, "w") as doc:
        doc.write(file)


def create_html_content(animals):
    content = ""
    for animal in animals:
        name = get_name(animal)
        diet = get_diet(animal)
        locations = ", ".join(get_locations(animal))
        type_ = get_type(animal)

        content += '<li class="cards__item">\n'
        content += f'<div class="card__title">{name}</div>\n'
        content += '<p class="card__text">\n'
        if bool(diet):
            content += f"<strong>Diet:</strong> {diet}<br/>\n"
        if bool(locations):
            content += f"<strong>Location:</strong> {locations}<br/>\n"
        if bool(type_):
            content += f"<strong>Type:</strong> {type_}<br/>\n"
        content += '</p>\n'
        content += '</li>\n'

    return content


def main():
    animals_data = load_data('animals_data.json')

    animals_template = load_html("animals_template.html")

    new_animals_template = animals_template.replace("__REPLACE_ANIMALS_INFO__", create_html_content(animals_data))

    save_document("animals.html", new_animals_template)


if __name__ == "__main__":
    main()