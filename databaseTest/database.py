print("\033c")
import json

data='{"t":"te"}'

try:
    with open("data.json", 'r', encoding='utf-8') as json_config:
        lang = json.load(json_config)
        json_config.close
except:
    w = open("data.json", "w")
    s = json.loads(data)
    d = json.dumps(s, indent = 4, sort_keys=True)
    w.write(d)
    
# Getting dictionary
person_dict = json.loads(data)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))


import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))

