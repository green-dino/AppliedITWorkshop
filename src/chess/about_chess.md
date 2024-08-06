In [knight.py](./knight.py) we learn about the considerations and components in Chess and how to think about the differences between methods, functions and classes. 

# About Chess

This module simulates a chess game focusing on the Knight piece. Each class and function has been designed to adhere to principles of separation of concerns.

## Scope
- Methods reside within classes, while functions can exist globally or within other functions or classes.
- Access to Attributes: Methods access the attributes of the object they're called on (using self), unlike functions, which lack this default access.
- Naming Conventions: Method names typically start with a verb and underscore (__init__), contrasting with function names that follow a broader naming convention (reverse_string()).

## Board Class
The Board class is responsible for managing the overall state of the chessboard, including the placement and movement of pieces. It provides a context for the pieces and their interactions.

### Responsibilities
- Initialize the board with pieces in their starting positions.
- Keep track of the positions of all pieces.
- Provide methods to check the state of specific squares (e.g., whether a square is occupied).
- Facilitate the movement of pieces by interacting with piece-specific methods.

## Piece Class
The Piece class serves as a base class for all chess pieces. It defines common attributes and methods that all pieces share, such as their position and basic movement capabilities.

### Responsibilities
- Store the piece's position and type.

## Knight Class
The Knight class extends the Piece class and defines specific behaviors and attributes unique to the Knight piece. It includes methods for moving according to the rules of how Knights move in chess.


1. Class vs. Global scope: Methods are defined within a class in
Python, whereas functions can be defined globally or within a
function or class.

2. Access to attributes: Methods have access to the attributes
of the object they're called on (i.e., self in the case of
instance methods), whereas functions do not have this access by
default.

3. Naming conventions: Method names are usually verb-based and
use leading underscores, such as `__init__(self)`, while
function names are more freeform, such as `reverse_string()`. 

Board Class
The Board class is responsible for managing the overall state of the chessboard, including the placement and movement of pieces. It provides a context for the pieces and their interactions.

Responsibilities

Initialize the board with pieces in their starting positions.
Keep track of the positions of all pieces.
Provide methods to check the state of specific squares (e.g., whether a square is occupied).
Facilitate the movement of pieces by interacting with piece-specific methods.
