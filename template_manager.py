import json

def load_templates():
    with open('data/templates.json') as f:
        return json.load(f)

def render_template(template, data):
    return template.format(**data)