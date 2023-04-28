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
        user_choice = None
        while user_choice not in ("1", "2", "3"):
            clear_screen()
            print("1 - Gioca\n2 - Personalizza\n3 - Esci")
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


def clear_screen() -> None:
    """Clear screen."""
    os.system("cls" if os.name == "nt" else "clear")


def start_game(tiles_number: int) -> None:
    """Start game."""
    global board
    board = Board(tiles_number)
    while board.game_finished is False:
        turn()


def turn() -> None:
    """Turn."""
    board.load_questions()
    show_UI()
    board.handle_tile()
    if board.game_finished is True:
        return
    show_UI()
    print(
        f"Sei arrivato su una casella {board.initial_board[board.player_position]}.")
    print("Premi invio per continuare...")
    input()


def show_UI() -> None:
    """Show UI."""
    clear_screen()
    print(f"Icona giocatore: {board.PLAYER_ICON} | Posizione: {board.player_position + 1} / {board.tiles_number} | < = Inizio | > = Fine | - = Niente | ? = Domanda | ! = Pericolo\n")
    print(board)


# start here
if __name__ == "__main__":
    main()
