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


def create_text_with_relevant_information(animals):
    text = ""
    for animal in animals:
        name = get_name(animal)
        diet = get_diet(animal)
        first_location = get_locations(animal)[0]
        type_ = get_type(animal)
        if bool(name):
            text += (f"Name: {name}\n")
        if bool(diet):
            text += (f"Diet: {diet}\n")
        if bool(first_location):
            text += (f"Location: {first_location}\n")
        if bool(type_):
            text += (f"Type: {type_}\n")
        text += "\n"
    return text


def load_html(file_path):
    """ Loads a HTML file """
    with open(file_path, "r") as handle:
        return handle.read()


def save_document(new_file_name, file):
    with open(new_file_name, "w") as doc:
        doc.write(file)

def main():
    animals_data = load_data('animals_data.json')

    animals_template = load_html("animals_template.html")

    new_animals_template = animals_template.replace("__REPLACE_ANIMALS_INFO__", create_text_with_relevant_information(animals_data))

    save_document("animals.html", new_animals_template)


if __name__ == "__main__":
    main()