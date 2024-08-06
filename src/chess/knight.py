from piece import Piece

class Knight(Piece):
    """
    The Knight class extends the Piece class and defines specific behaviors and attributes 
    unique to the Knight piece. It includes methods for moving according to the rules of 
    how Knights move in chess.
    """
    
    def __init__(self, position, board):
        """
        Initializes a Knight object.

        Args:
            position (tuple): The position of the Knight on the board.
            board (Board): The board the Knight belongs to.
        """
        super().__init__(position, "Knight")
        self.board = board

    def move(self, x_change, y_change):
        """
        Attempts to move the Knight to a new position based on the given changes.

        Args:
            x_change (int): Change in the x-coordinate.
            y_change (int): Change in the y-coordinate.

        Returns:
            bool: True if the move is successful, False otherwise.
        """
        new_x = self.position[0] + x_change
        new_y = self.position[1] + y_change

        if 0 <= new_x < 8 and 0 <= new_y < 8:
            if not self.board.grid[new_x][new_y]:
                self.board.move_piece(self, x_change, y_change)
                return True
        return False
