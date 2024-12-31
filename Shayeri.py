import time
import random
import os

# Function to display the logo
def display_logo():
    logo = """
     _______ _______  ______  ______  _____   ______
        |    |______ |_____/ |_____/ |     | |_____/
        |    |______ |    \_ |    \_ |_____| |    \_
                                                
    """
    print(logo)
    print("THE ULTIMATE GENERATOR TOOL\n")

# Sample lines for songs and shayeri
song_lines = [
    "I'm on top of the world, ain't coming down.",
    "They doubted me once, who's laughing now?",
    "Success in my pocket, haters beware.",
    "I'm a shooting star, lighting up the air.",
    "No chains can hold me, I'm free as the wind.",
    "They tried to stop me, but I always win."
]

shayeri_couplets = [
    "Duniya jalti hai toh jalne de, hum apni raah chalenge.",
    "Jaha log rukte hai, wahi se hum shuru karte hai.",
    "Mitti se bana hoon, magar sitare chhoota hoon.",
    "Mushkile aayi toh kya, hum toh toofan se khelte hai.",
    "Mera attitude meri pehchaan hai, dil se nahi khelte hum.",
    "Samundar ki gehraai se zyada, mere jazbe gehre hain."
]

# Function to generate multiple songs
def generate_multiple_songs(count):
    result = []
    for _ in range(count):
        song = "\n".join(random.sample(song_lines, k=min(len(song_lines), 4)))
        result.append(song)
    return result

# Function to generate multiple shayeri
def generate_multiple_shayeri(count):
    result = []
    for _ in range(count):
        shayeri = "\n".join(random.sample(shayeri_couplets, k=min(len(shayeri_couplets), 2)))
        result.append(shayeri)
    return result

# Function to add custom lines
def add_custom_text(category):
    if category == "song":
        new_line = input("Enter your custom song line: ")
        song_lines.append(new_line)
        print("Custom song line added successfully!")
    elif category == "shayeri":
        new_couplet = input("Enter your custom shayeri couplet: ")
        shayeri_couplets.append(new_couplet)
        print("Custom shayeri couplet added successfully!")

# Main menu
def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_logo()
        print("[1] Generate Songs")
        print("[2] Generate Shayeri")
        print("[3] Add Custom Song Line")
        print("[4] Add Custom Shayeri Couplet")
        print("[5] Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            count = int(input("How many songs do you want to generate? "))
            songs = generate_multiple_songs(count)
            for i, song in enumerate(songs, start=1):
                print(f"\nSong {i}:\n{song}\n")
        elif choice == '2':
            count = int(input("How many shayeri do you want to generate? "))
            shayeris = generate_multiple_shayeri(count)
            for i, shayeri in enumerate(shayeris, start=1):
                print(f"\nShayeri {i}:\n{shayeri}\n")
        elif choice == '3':
            add_custom_text("song")
        elif choice == '4':
            add_custom_text("shayeri")
        elif choice == '5':
            print("Goodbye! Thank you for using TERROR.")
            break
        else:
            print("Invalid choice. Please try again!")
        input("\nPress Enter to continue...")

# Entry point
if __name__ == "__main__":
    main_menu()