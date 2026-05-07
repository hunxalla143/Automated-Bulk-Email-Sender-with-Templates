import csv
import json

def load_csv(file_path):
    contacts = []
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)
    return contacts


def load_json(file_path):
    with open(file_path) as file:
        return json.load(file)
    