import time
import random
import os
from rich.console import Console
from rich.text import Text

# Initialize Rich Console
console = Console()

# Function to display the animated logo
def display_logo():
    logo_lines = [
        "     _______ _______  ______  ______  _____   ______",
        "        |    |______ |_____/ |_____/ |     | |_____/",
        "        |    |______ |    \\_ |    \\_ |_____| |    \\_",
        "",
        "      TERROR - THE ULTIMATE GENERATOR TOOL"
    ]
    for line in logo_lines:
        console.print(Text(line, style="bold red"))
        time.sleep(0.2)

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
        console.print(Text("Custom song line added successfully!", style="bold yellow"))
    elif category == "shayeri":
        new_couplet = input("Enter your custom shayeri couplet: ")
        shayeri_couplets.append(new_couplet)
        console.print(Text("Custom shayeri couplet added successfully!", style="bold yellow"))

# Main menu
def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_logo()
        console.print(Text("\n[1] Generate Songs", style="cyan"))
        console.print(Text("[2] Generate Shayeri", style="magenta"))
        console.print(Text("[3] Add Custom Song Line", style="yellow"))
        console.print(Text("[4] Add Custom Shayeri Couplet", style="green"))
        console.print(Text("[5] Exit", style="red"))

        choice = input("\nEnter your choice: ")

        if choice == '1':
            count = int(input("How many songs do you want to generate? "))
            songs = generate_multiple_songs(count)
            for i, song in enumerate(songs, start=1):
                console.print(Text(f"\nSong {i}:\n{song}\n", style="bold green"))
        elif choice == '2':
            count = int(input("How many shayeri do you want to generate? "))
            shayeris = generate_multiple_shayeri(count)
            for i, shayeri in enumerate(shayeris, start=1):
                console.print(Text(f"\nShayeri {i}:\n{shayeri}\n", style="bold blue"))
        elif choice == '3':
            add_custom_text("song")
        elif choice == '4':
            add_custom_text("shayeri")
        elif choice == '5':
            console.print(Text("Goodbye! Thank you for using TERROR.", style="bold red"))
            break
        else:
            console.print(Text("Invalid choice. Please try again!", style="bold red"))
        input("\nPress Enter to continue...")

# Entry point
if __name__ == "__main__":
    main_menu()