import json

# Load JSON
with open('config.json', 'r') as file:
    config = json.load(file)

# Dump JSON
new_config = {'threshold': 0.7, 'model': 'XGBoost'}
with open('new_config.json', 'w') as file:
    json.dump(new_config, file, indent=4)