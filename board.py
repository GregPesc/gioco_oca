import random


class Board:
    """Board class."""

    QUESTIONS_PERCENTAGE = 50
    DANGERS_PERCENTAGE = 25

    def __init__(self, tiles_number: int) -> None:
        self.tiles_number = tiles_number
        self.board = self.build_board()

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
        board[0] = " # "
        board[-1] = " @ "

        return board

    def print_board(self) -> None:
        """Print the board"""
        for i in range(0, len(self.board), 5):
            print("".join(self.board[i:i + 5]))
