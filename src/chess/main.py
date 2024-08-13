from board import Board
from move_piece import move_piece


def main():
    """
    Main function to initialize the board and attempt to move the Knight piece.
    """
    board = Board()

    print("Initial position of the Knight:", board.knight.position)

    # Attempt to move the Knight
    successful_move = move_piece(board, board.knight, 1, 2)

    if successful_move:
        print("Knight moved to:", board.knight.position)
    else:
        print("Invalid move for the Knight")


if __name__ == "__main__":
    main()
