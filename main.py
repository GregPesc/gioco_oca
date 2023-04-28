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
        clear_screen()
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

    while True:
        clear_screen()
        print("Numero di caselle (multiplo di 5) (consigliato: 25):")

        try:
            user_choice = int(input())
            if user_choice % 5 == 0 and user_choice > 0:
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


def clear_screen() -> None:
    """Clear screen."""
    os.system("cls" if os.name == "nt" else "clear")


def start_game(tiles_number: int) -> None:
    """Start game."""
    global board
    board = Board(tiles_number)

    # temp
    clear_screen()
    print(board)
    board.set_player_position(4)
    print(board)
    board.set_player_position(0)
    print(board)
    input("Premi invio per continuare...")
    # end temp


# start here
if __name__ == "__main__":
    main()
