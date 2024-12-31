import time
import random
import os
from colorama import Fore, Style, init

# Initialize colorama for cross-platform compatibility
init(autoreset=True)

# Function to display the logo
def display_logo():
    logo = f"""
{Fore.RED}     _______ _______  ______  ______  _____   ______
        {Fore.CYAN}|    |______ |_____/ |_____/ |     | |_____/
        {Fore.YELLOW}|    |______ |    \_ |    \_ |_____| |    \_

      {Fore.MAGENTA} TERROR - THE ULTIMATE GENERATOR TOOL 
{Style.RESET_ALL}
    """
    print(logo)

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

# Function to generate a song
def generate_song():
    song = "\n".join(random.sample(song_lines, k=4))
    return f"{Fore.GREEN}Generated Song:\n\n{song}\n"

# Function to generate a shayeri
def generate_shayeri():
    shayeri = "\n".join(random.sample(shayeri_couplets, k=2))
    return f"{Fore.BLUE}Generated Shayeri:\n\n{shayeri}\n"

# Function to add custom lines
def add_custom_text(category):
    if category == "song":
        new_line = input("Enter your custom song line: ")
        song_lines.append(new_line)
        print(f"{Fore.YELLOW}Custom song line added successfully!")
    elif category == "shayeri":
        new_couplet = input("Enter your custom shayeri couplet: ")
        shayeri_couplets.append(new_couplet)
        print(f"{Fore.YELLOW}Custom shayeri couplet added successfully!")

# Main menu
def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_logo()
        print(f"{Fore.CYAN}[1] Generate a Song")
        print(f"{Fore.MAGENTA}[2] Generate a Shayeri")
        print(f"{Fore.YELLOW}[3] Add Custom Song Line")
        print(f"{Fore.GREEN}[4] Add Custom Shayeri Couplet")
        print(f"{Fore.RED}[5] Exit")
        
        choice = input(f"{Fore.WHITE}\nEnter your choice: ")

        if choice == '1':
            print(generate_song())
        elif choice == '2':
            print(generate_shayeri())
        elif choice == '3':
            add_custom_text("song")
        elif choice == '4':
            add_custom_text("shayeri")
        elif choice == '5':
            print(f"{Fore.RED}Goodbye! Thank you for using TERROR.")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again!")
        input("\nPress Enter to continue...")

# Entry point
if __name__ == "__main__":
    main_menu()