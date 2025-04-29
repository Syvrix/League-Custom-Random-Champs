import random, json

# Load role-based champions from file
with open('champions_w_roles.json', 'r') as file:
    role_champions = json.load(file)

# Flatten all champions into one big list
all_champions = []
for champs in role_champions.values():
    all_champions.extend(champs)

def gen_random_champs(x):        
    # Randomly select x champions
    selected_champions = random.sample(all_champions, x)
    print_champions(selected_champions)
    
def gen_random_role_champs(x):
    # zipslide: gen_random_role_champs changes
    # modified to store both champion name and role as tuples
    # this allows us to track which role each champion belongs to
    selected_champions = []
    for role in role_champions:
        if len(role_champions[role]) >= x:
            # Create tuples of (champion_name, role) for each selected champion
            selected_champions.extend([(champ, role) for champ in random.sample(role_champions[role], x)])
    print_champions(selected_champions)
    
# zipslide: role function improvements
def random_jungler():
    return random.sample(role_champions["jungle"], 1)[0]

def random_top():
    return random.sample(role_champions["top"], 1)[0]

def random_mid():
    return random.sample(role_champions["mid"], 1)[0]

def random_adc():
    return random.sample(role_champions["adc"], 1)[0]

def random_support():
    return random.sample(role_champions["support"], 1)[0]

def print_champions(champions):
    # zipslide: print_champions
    # updated to handle two different types of input:
    # 1. simple champion names (from gen_random_champs)
    # 2. champion-role tuples (from gen_random_role_champs)
    for champ in champions:
        if isinstance(champ, tuple):
            # forr role-specific champions (champ, role)
            print(f"{champ[0]} - {champ[1]}")
        else:
            # for general champions (just name)
            print(champ)