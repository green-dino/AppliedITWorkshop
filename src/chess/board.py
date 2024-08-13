from knight import Knight


class Board:
    """
    The Board class is responsible for managing the overall state of the chessboard,
    including the placement and movement of pieces. It provides a context for the pieces
    and their interactions.
    """

    def __init__(self):
        """
        Initializes a Board object with pieces in their starting positions.
        """
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.knight = Knight((5, 4), self)
        self.place_piece(self.knight)

    def place_piece(self, piece):
        """
        Places a piece on the board at its position.

        Args:
            piece (Piece): The piece to be placed on the board.
        """
        x, y = piece.position
        self.grid[x][y] = piece

    def move_piece(self, piece, x_change, y_change):
        """
        Moves a piece to a new position on the board.

        Args:
            piece (Piece): The piece to be moved.
            x_change (int): Change in the x-coordinate.
            y_change (int): Change in the y-coordinate.

        Returns:
            bool: True if the move is successful, False otherwise.
        """
        x, y = piece.position
        new_x = x + x_change
        new_y = y + y_change

        if 0 <= new_x < 8 and 0 <= new_y < 8:
            if not self.grid[new_x][new_y]:
                self.grid[x][y] = None
                piece.position = (new_x, new_y)
                self.grid[new_x][new_y] = piece
                return True
        return False
