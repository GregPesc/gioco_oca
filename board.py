import random
import copy
import json
import os


class Board:
    """Board class."""

    QUESTIONS_PERCENTAGE = 50
    DANGERS_PERCENTAGE = 25
    PLAYER_ICON = "@"
    player_position = 0
    die_faces = 3

    def __init__(self, tiles_number: int) -> None:
        self.tiles_number = tiles_number
        self.initial_board = self.build_board()
        self.board = copy.deepcopy(self.initial_board)
        self.board[0] = f" {self.PLAYER_ICON} "
        self.questions = self.load_questions()

    def __str__(self) -> str:
        """Print board."""
        board_string = ""
        for i in range(0, len(self.board), 5):
            board_string += "".join(self.board[i:i + 5])
            board_string += "\n"

        return board_string

    def load_questions(self) -> dict:
        """Load questions from file."""
        with open("domande_e_risposte.json", "r") as file:
            questions = json.load(file)

        return questions

    def build_board(self) -> list[str]:
        """Build initial board."""
        board = []

        # create empty board
        for _ in range(self.tiles_number):
            board.append(" - ")

        # calculate the number of questions and dangers
        number_of_questions = int(
            self.tiles_number * self.QUESTIONS_PERCENTAGE / 100)
        number_of_dangers = int(
            self.tiles_number * self.DANGERS_PERCENTAGE / 100)

        # create a list of all the positions except the first and the last
        positions = [i for i in range(1, self.tiles_number - 1)]

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
        board[0] = " < "
        board[-1] = " > "

        return board

    def roll_dice(self) -> int:
        """Roll dice."""

        number = random.randint(1, self.die_faces)
        return number

    def clear_screen(self) -> None:
        """Clear screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def set_player_position(self, move_to_position: int) -> None:
        """Set player position."""
        # remove player icon from current position and replace it with original tile
        self.board[self.player_position] = self.initial_board[self.player_position]
        # set player position to new position
        self.player_position = move_to_position
        # replace new position with player icon
        self.board[self.player_position] = f" {self.PLAYER_ICON} "

    def handle_tile(self) -> None:
        """Handle tile."""
        tile = self.board[self.player_position]
        if tile == " ? ":
            self.handle_question()
        elif tile == " ! ":
            self.handle_danger()
        elif tile == " - ":
            pass
        elif tile == " < ":
            pass
        elif tile == " > ":
            self.handle_end()
        else:
            raise Exception(f"Invalid tile: {tile}")

    def handle_question(self) -> None:
        """Handle question."""
        question, options = self.get_random_question()
        correct_answer = options.pop(4)
        self.clear_screen()
        print(f"Domanda: {question}")
        for i, option in enumerate(options):
            print(f"{i + 1} - {option}")
        while True:
            user_choice = input()
            if user_choice in ("1", "2", "3", "4"):
                break
        self.clear_screen()
        if user_choice == correct_answer:
            print("Risposta corretta!")
            print("Premi invio per tirare il dado e muoverti avanti.")
            number = self.roll_dice()
            print(f"Hai tirato {number}!")
            self.set_player_position(self.player_position + number)
        else:
            print("Risposta sbagliata!")
            print("Premi invio per tirare il dado e muoverti indietro.")
            number = self.roll_dice()
            print(f"Hai tirato {number}!")
            self.set_player_position(self.player_position - number)

    def get_random_question(self) -> tuple[str, list[str]]:
        """Get random question."""
        question, options = random.choice(list(self.questions.items()))
        return question, options

    def handle_danger(self) -> None:
        """Handle danger."""
        raise NotImplementedError

    def handle_end(self) -> None:
        """Handle end."""
        raise NotImplementedError
