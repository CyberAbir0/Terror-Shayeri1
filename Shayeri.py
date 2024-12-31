import random

# Display logo with name
def display_logo():
    logo = """
     _______ _______  ______  ______  _____   ______
        |    |______ |_____/ |_____/ |     | |_____/
        |    |______ |    \_ |    \_ |_____| |    \_
                                                
    """
    print(logo)
    print("WELCOME TO THE TERROR SHAYERI GENERATOR!\n")

# Word pools for generating shayeri
subjects = [
    "Dil", "Zindagi", "Mohabbat", "Duniya", "Chand", "Sitam", "Khuda", "Ashq", 
    "Raat", "Tanhaai", "Safar", "Ishq", "Pyaar", "Gham", "Aansu", "Hawa"
]
adjectives = [
    "meethi", "sundar", "gumsum", "udasi bhari", "roshan", "gehri", "khushnuma", 
    "rangeen", "masoom", "narm", "bekhabar", "sookhi", "bheegi", "khoobsurat"
]
verbs = [
    "muskurata hai", "jalta hai", "sajta hai", "girta hai", "behta hai", "khilta hai", 
    "rohta hai", "udta hai", "chup ho jata hai", "chamkata hai", "bekaraar hota hai"
]
locations = [
    "aasman mein", "khwabon mein", "zakhmon mein", "samundar mein", 
    "raat ke andheron mein", "yaadon mein", "kuch lamhon mein", 
    "sooni galiyon mein", "dil ke kone mein"
]

# Function to generate a single shayeri
def generate_shayeri():
    line1 = f"{random.choice(subjects)} {random.choice(adjectives)} {random.choice(verbs)}."
    line2 = f"Ye sab hota hai {random.choice(locations)}."
    return f"{line1}\n{line2}"

# Function to generate multiple shayeris
def generate_multiple_shayeris(count):
    shayeris = []
    for _ in range(count):
        shayeris.append(generate_shayeri())
    return shayeris

# Main function
def main():
    display_logo()
    while True:
        try:
            count = int(input("How many shayeris do you want to generate? "))
            if count <= 0:
                print("Please enter a valid number greater than 0.")
                continue
            
            print("\nGenerating your shayeris...\n")
            shayeris = generate_multiple_shayeris(count)
            for i, shayeri in enumerate(shayeris, start=1):
                print(f"Shayeri {i}:")
                print("-" * 50)
                print(shayeri)
                print("-" * 50)
            
            again = input("\nDo you want to generate more shayeris? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Thank you for using the TERROR Shayeri Generator! Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()