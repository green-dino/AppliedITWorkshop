from typing import List, Dict, Tuple, Optional, Union, Any, Callable
from typing_extensions import TypedDict, Protocol, Literal, Final

# Step 1: Define a TypedDict for a book
class Book(TypedDict):
    """A dictionary representing a book."""
    title: str
    author: str
    pages: int
    genre: Optional[str]

def print_book_details(book: Book) -> None:
    """
    Prints the details of a book.
    
    Parameters:
    - book (Book): A dictionary containing book details.
    """
    print(f"Title: {book['title']}, Author: {book['author']}, Pages: {book['pages']}, Genre: {book.get('genre', 'Unknown')}")

# Step 2: Define a Protocol for a readable object
class Readable(Protocol):
    """Defines a protocol for objects that can be read."""
    def read(self) -> str:
        ...

class Newspaper:
    """Represents a newspaper."""
    def read(self) -> str:
        return "Reading today's news."

class Magazine:
    """Represents a magazine."""
    def read(self) -> str:
        return "Reading the latest articles."

def read_content(item: Readable) -> None:
    """
    Reads the content of a readable item.
    
    Parameters:
    - item (Readable): An object implementing the Readable protocol.
    """
    print(item.read())

# Step 3: Use Literal for a function with specific argument values
def order_status(status: Literal["ordered", "shipped", "delivered"]) -> str:
    """
    Returns the status of an order.
    
    Parameters:
    - status (Literal["ordered", "shipped", "delivered"]): The status of the order.
    
    Returns:
    - str: The status message.
    """
    return f"The order status is {status}."

# Step 4: Use Final for a constant value
DATABASE_URL: Final = "https://database.example.com"

def get_database_url() -> str:
    """
    Returns the database URL.
    
    Returns:
    - str: The database URL.
    """
    return DATABASE_URL

# Step 5: Use Union for a function that handles multiple types
def handle_input(data: Union[int, str, List[str]]) -> str:
    """
    Handles input data of various types.
    
    Parameters:
    - data (Union[int, str, List[str]]): The input data.
    
    Returns:
    - str: A message indicating the type of received data.
    """
    if isinstance(data, int):
        return f"Received an integer: {data}"
    elif isinstance(data, str):
        return f"Received a string: {data}"
    elif isinstance(data, list):
        return f"Received a list of strings: {', '.join(data)}"
    return "Unknown type"

# Step 6: Use Callable to pass a function as an argument
def apply_operation(operation: Callable[[float, float], float], x: float, y: float) -> float:
    """
    Applies a given operation to two numbers.
    
    Parameters:
    - operation (Callable[[float, float], float]): The operation to apply.
    - x (float): The first operand.
    - y (float): The second operand.
    
    Returns:
    - float: The result of applying the operation.
    """
    return operation(x, y)

# Step 7: Use List, Dict, Tuple, Any for various data structures
def collection_demo() -> None:
    """
    Demonstrates the use of various data structures.
    """
    fruits: List[str] = ["apple", "banana", "cherry"]
    phone_book: Dict[str, Any] = {"Alice": "123-4567", "Bob": "987-6543", "Eve": None}
    coordinates: Tuple[float, float] = (34.05, -118.25)

    print(f"Fruits: {fruits}")
    print(f"Phone Book: {phone_book}")
    print(f"Coordinates: {coordinates}")

# Testing the exercise functions
if __name__ == "__main__":
    # TypedDict
    book = {"title": "1984", "author": "George Orwell", "pages": 328, "genre": "Dystopian"}
    print_book_details(book)
    
    # Protocol
    newspaper = Newspaper()
    magazine = Magazine()
    read_content(newspaper)
    read_content(magazine)
    
    # Literal
    print(order_status("shipped"))
    
    # Final
    print(get_database_url())
    
    # Union
    print(handle_input(42))
    print(handle_input("Hello, World!"))
    print(handle_input(["one", "two", "three"]))
    
    # Callable
    def multiply(a: float, b: float) -> float:
        return a * b
    
    print(apply_operation(multiply, 5.0, 3.0))
    
    # List, Dict, Tuple, Any
    collection_demo()
