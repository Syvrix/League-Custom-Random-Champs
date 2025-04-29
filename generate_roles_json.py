'''
the purpose of this, is to generate a roles.json
which organizes the data as

role: [champ1, champ2, champ3, etc..]

this is easier when chosing a random selection.
'''

import json

def generate_roles_json():
    with open('lists/champions_w_roles.json', 'r') as file:
        champions_data = json.load(file)
    
    roles_dict = {
        "top": [],
        "jungle": [],
        "mid": [],
        "adc": [],
        "support": []
    }
    
    for champ in champions_data:
        for role in champ["roles"]:
            if role in roles_dict:
                roles_dict[role].append(champ["name"])
    
    with open('lists/roles.json', 'w') as file:
        json.dump(roles_dict, file, indent=4)
    
    print('created roles.json~~')

if __name__ == "__main__":
    generate_roles_json() 