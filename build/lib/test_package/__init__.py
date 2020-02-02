import json
def print_func(name):
    return f" my name is  {name}"


def add(a, b):
    return a + b


def messages_json_path():
    return 'test_package/example.json'


def print_json_file_data(func):
    with open(func) as file:
        data = json.load(file)
        for content in data['menu']['items']:
            print(content)
