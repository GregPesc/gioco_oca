import json
import random
import os

from board import Board


def main() -> None:
    """Main function."""
    menu()


def menu() -> None:
    """Display menu."""

    # default tiles number
    tiles_number = 25

    while True:

        print("1 - Gioca\n2 - Personalizza\n3 - Esci")

        user_choice = None
        while user_choice not in ("1", "2", "3"):
            user_choice = input()
            if user_choice == "1":
                start_game(tiles_number)
            elif user_choice == "2":
                tiles_number = customize()
            elif user_choice == "3":
                exit()


def customize() -> int:
    """Customize menu."""

    print("Numero di caselle (multiplo di 5):")

    while True:
        try:
            user_choice = int(input())
            if user_choice % 5 == 0:
                break
        except ValueError:
            pass

    return user_choice


def roll_dice() -> int:
    """Roll dice."""

    # default die faces
    die_faces = 3

    number = random.randint(1, die_faces)
    return number


def start_game(tiles_number: int) -> None:
    """Start game."""
    global board
    board = Board(tiles_number)
    board.print_board()


# start here
main()
