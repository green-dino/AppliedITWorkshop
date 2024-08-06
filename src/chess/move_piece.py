def move_piece(board, piece, x_change, y_change):
    """
    Attempts to move a piece on the board.

    Args:
        board (Board): The board containing the piece.
        piece (Piece): The piece to be moved.
        x_change (int): Change in the x-coordinate.
        y_change (int): Change in the y-coordinate.

    Returns:
        bool: True if the move is successful, False otherwise.
    """
    return piece.move(x_change, y_change)
