import json 

person = '''
{
    "name": "pranjal",
    "address": "sitapaila"
}
'''

person_dict = json.loads(person)

print(person_dict)
print(person_dict['name'])
person_dict['address'] = "kathmandu"
print(person_dict)

json_output = json.dumps(person_dict,indent=4)
print("\n Modified json")
print(json_output)