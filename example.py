from champGenerator import (
    gen_random_champs,
    gen_random_role_champs,
    random_jungler,
    random_top,
    random_mid,
    random_adc,
    random_support,
    get_champ_icon_url
)

def main():
    print("\n1. Generate 3 random champions from all roles:")
    gen_random_champs(3)
    
    print("\n2. Generate 2 random champions from each role:")
    gen_random_role_champs(2)
    
    print("\n3. Generate a random team composition:")
    print("Top:", random_top())
    print("Jungle:", random_jungler())
    print("Mid:", random_mid())
    print("ADC:", random_adc())
    print("Support:", random_support())
    
    print("\n4. Generate a random duo lane (ADC + Support):")
    print("ADC:", random_adc())
    print("Support:", random_support())
    
    #print("\n5. Generate a URL icon for selected champion:")
    #print (get_champ_icon_url(random_support()))
    
if __name__ == "__main__":
    main() 