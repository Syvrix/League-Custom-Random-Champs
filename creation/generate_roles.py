import json

# Load the champion names
with open('champions.json', 'r') as file:
    champions = json.load(file)

# Create empty role dictionary
roles = {
    "top": [],
    "jungle": [],
    "mid": [],
    "adc": [],
    "support": []
}

print("Assign roles to each champion.")
print("Available roles: top, jungle, mid, adc, support\n")

# Assign a role to each champion
for champ in champions:
    while True:
        role = input(f"What role is {champ}? ").strip().lower()
        if role in roles:
            roles[role].append(champ)
            break
        else:
            print("Invalid role. Please choose from: top, jungle, mid, adc, support.")

# Save the roles to a file
with open('roles.json', 'w') as file:
    json.dump(roles, file, indent=4)

print("\nroles.json has been created!")
