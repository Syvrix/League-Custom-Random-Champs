import random, json

#!zipslide -> file path changes
#!zipslide -> using the pre-generated roles.json file for better performance
with open('lists/roles.json', 'r') as file:
    role_champions = json.load(file)


#!zipslide -> using champions.json for general champion selection
with open('lists/champions.json', 'r') as file:
    all_champions = json.load(file)


#!Syphex -> gets the champion icon from Riots CDN for league assets.
def get_champ_icon_url(champ_name, patch="14.8.1"):
    normalized = champ_name.replace("'", "").replace(" ", "")
    return f"https://ddragon.leagueoflegends.com/cdn/{patch}/img/champion/{normalized}.png"
    
def gen_random_champs(x):        
    # randomly select x champions from all champions
    selected_champions = random.sample(all_champions, x)
    print_champions(selected_champions)
    
def gen_random_role_champs(x):
    #!zipslide -> gen_random_role_champs changes
    #!zipslide -> modified to store both champion name and role as tuples
    #!zipslide -> this allows us to track which role each champion belongs to
    selected_champions = []
    for role in role_champions:
        if len(role_champions[role]) >= x:
            pool = []
            while len(pool) < x:
                # Create tuples of (champion_name, role) for each selected champion
                champ = [(champ, role) for champ in random.sample(role_champions[role], 1)]
                if champ not in pool:
                    #!Syphex -> Ensures no duplicates are generated.
                    pool.append(champ)                
                    selected_champions.extend(champ)
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
    #!zipslide -> print_champions
    #!zipslide -> updated to handle two different types of input:
    #!zipslide -> 1. simple champion names (from gen_random_champs)
    #!zipslide -> 2. champion-role tuples (from gen_random_role_champs)
    for champ in champions:
        if isinstance(champ, tuple):
            #!zipslide -> for role-specific champions (champ, role)
            print(f"{champ[0]} - {champ[1]}")
        else:
            #!zipslide -> for general champions (just name)
            print(champ)