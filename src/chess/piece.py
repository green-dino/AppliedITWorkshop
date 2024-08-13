class Piece:
    """
    The Piece class serves as a base class for all chess pieces. It defines common attributes
    and methods that all pieces share, such as their position and basic movement capabilities.
    """

    def __init__(self, position, piece_type):
        """
        Initializes a Piece object.

        Args:
            position (tuple): The position of the piece on the board.
            piece_type (str): The type of the piece (e.g., 'Knight').
        """
        self.position = position
        self.piece_type = piece_type
