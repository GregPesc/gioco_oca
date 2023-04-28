import random
import copy


class Board:
    """Board class."""

    QUESTIONS_PERCENTAGE = 50
    DANGERS_PERCENTAGE = 25
    PLAYER_ICON = "@"
    player_position = 0

    def __init__(self, tiles_number: int) -> None:
        self.tiles_number = tiles_number
        self.initial_board = self.build_board()
        self.board = copy.deepcopy(self.initial_board)
        self.board[0] = f" {self.PLAYER_ICON} "

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

    def __str__(self) -> str:
        """Print board."""
        board_string = ""
        for i in range(0, len(self.board), 5):
            board_string += "".join(self.board[i:i + 5])
            board_string += "\n"

        return board_string

    def set_player_position(self, move_to_position: int) -> None:
        """Set player position."""
        # remove player icon from current position and replace it with original tile
        self.board[self.player_position] = self.initial_board[self.player_position]
        # set player position to new position
        self.player_position = move_to_position
        # replace new position with player icon
        self.board[self.player_position] = f" {self.PLAYER_ICON} "
