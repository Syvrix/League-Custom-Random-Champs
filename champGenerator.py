import random, json

# Load role-based champions from file
with open('roles.json', 'r') as file:
    role_champions = json.load(file)


# Flatten all champions into one big list
# CHANGE THIS, IT ADDS DUPLICATED CHAMPIONS TO ATM.
all_champions = []
for champs in role_champions.values():
    all_champions.extend(champs)

def gen_random_champs(x):        
    # Load all champions
    with open('champions.json', 'r') as file:
        all_champions = json.load(file)
    
    # Randomly select x champions
    selected_champions = random.sample(all_champions, x)
    print_champions(selected_champions)
    
def gen_random_role_champs(x):
    
        
def random_jungler():
    random_junglers = random.sample(role_champions["jungle"])

def random_top():
    random_top = random.sample(role_champions["top"])

def random_mid():
    random_mid = random.sample(role_champions["mid"])

def random_adc():
    random_adc = random.sample(role_champions["adc"])

def random_support():
    random_support = random.sample(role_champions["support"])
    
def print_champions(champions):
    # Print selected champions
    for champ in champions:
        print(f"{champ['name']} - {champ['role']}")