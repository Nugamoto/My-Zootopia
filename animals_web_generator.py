import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')


def get_name(animal):
    return animal["name"]


def get_diet(animal):
    return animal["characteristics"]["diet"] if "diet" in animal["characteristics"] else False


def get_locations(animal):
    return animal["locations"]


def get_type(animal):
    return animal["characteristics"]["type"] if "type" in animal["characteristics"] else False


def print_data(animals):
    for animal in animals:
        name = get_name(animal)
        diet = get_diet(animal)
        first_location = get_locations(animal)[0]
        type_ = get_type(animal)
        print()
        if bool(name):
            print("Name:", name)
        if bool(diet):
            print("Diet:", diet)
        if bool(first_location):
            print("Location:", first_location)
        if bool(type_):
            print("Type:", type_)
        print()

