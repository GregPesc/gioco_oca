import json
import random
import os

# global variables
tiles_number = 25
die_faces = 3
QUESTIONS_PERCENTAGE = 40
DANGERS_PERCENTAGE = 30


def main() -> None:
    """Main function"""
    menu()


def menu() -> None:
    """Display menu"""
    print("1 - Gioca\n2 - Personalizza\n3 - Esci")
    user_choice = None
    while user_choice not in ("1", "2", "3"):
        user_choice = input()
        if user_choice == "1":
            start_game()
        elif user_choice == "2":
            customize()
        elif user_choice == "3":
            exit()


def start_game():
    """Start game"""
    pass


def customize() -> None:
    """Customize menu"""
    global tiles_number
    print("Numero di caselle (numero intero):")
    while True:
        try:
            user_choice = int(input())
            break
        except ValueError:
            pass
    tiles_number = user_choice

def build_board() -> list[str]:
    """Build board initial board"""
    pass

def roll_dice() -> int:
    """Rolls dice"""
    pass



# start here
main()
