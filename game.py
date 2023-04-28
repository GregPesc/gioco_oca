import json
import random
import os

# global variables
tiles_number = 25  # multiple of 5
die_faces = 3
QUESTIONS_PERCENTAGE = 50
DANGERS_PERCENTAGE = 25


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
    global board
    board = build_board()
    print_board()


def customize() -> None:
    """Customize menu"""
    global tiles_number
    print("Numero di caselle (numero intero):")
    while True:
        try:
            user_choice = int(input())
            if user_choice % 5 == 0:
                break
        except ValueError:
            pass

    tiles_number = user_choice


def build_board() -> list[str]:
    """Build board initial board"""
    board = []

    # create empty board
    for i in range(tiles_number):
        board.append(" - ")

    # calculate the number of questions and dangers
    number_of_questions = int(tiles_number * QUESTIONS_PERCENTAGE / 100)
    number_of_dangers = int(tiles_number * DANGERS_PERCENTAGE / 100)

    # create a list of all the positions except the first and the last
    positions = [i for i in range(1, tiles_number - 1)]

    # replace random tiles with questions
    for _ in range(number_of_questions):
        position = random.choice(positions)
        board[position] = " ? "
        positions.remove(position)

    # replace random tiles with dangers
    for _ in range(number_of_dangers):
        position = random.choice(positions)
        board[position] = " ! "
        positions.remove(position)

    # add start and end tiles
    board[0] = " # "
    board[-1] = " @ "

    return board


def print_board() -> None:
    """Print the board"""
    global board
    for i in range(0, len(board), 5):
        print("".join(board[i:i + 5]))


def roll_dice() -> int:
    """Rolls dice"""
    number = random.randint(1, die_faces)
    return number


# start here
main()
