# Importing required typing modules
from typing import List, Dict, Tuple, Optional, Union, Any, Callable
from typing_extensions import TypedDict, Protocol, Literal, Final

# Exercise: Demonstrating the use of various typing modules

# Step 1: TypedDict
class Person(TypedDict):
    name: str
    age: int
    email: Optional[str]

def print_person_details(person: Person) -> None:
    print(f"Name: {person['name']}, Age: {person['age']}, Email: {person.get('email', 'N/A')}")

# Step 2: Protocol
class Greetable(Protocol):
    def greet(self) -> str:
        ...

class Greeter:
    def greet(self) -> str:
        return "Hello, world!"

def greet_entity(entity: Greetable) -> None:
    print(entity.greet())

# Step 3: Literal
def get_status(status: Literal["open", "closed", "pending"]) -> str:
    return f"The status is {status}"

# Step 4: Final
API_KEY: Final = "1234567890ABCDEF"

def print_api_key() -> None:
    print(f"API Key: {API_KEY}")

# Step 5: Union
def process_data(data: Union[int, str]) -> str:
    if isinstance(data, int):
        return f"Processed number: {data}"
    else:
        return f"Processed string: {data}"

# Step 6: Callable
def execute_function(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

# Step 7: List, Dict, Tuple, Any
def demonstrate_collection_usage() -> None:
    my_list: List[int] = [1, 2, 3, 4, 5]
    my_dict: Dict[str, Any] = {"name": "Alice", "age": 30, "hobbies": ["reading", "swimming"]}
    my_tuple: Tuple[str, int] = ("John", 25)
    
    print(f"List: {my_list}")
    print(f"Dict: {my_dict}")
    print(f"Tuple: {my_tuple}")

# Testing the exercise functions
if __name__ == "__main__":
    # TypedDict
    person = {"name": "Alice", "age": 30, "email": "alice@example.com"}
    print_person_details(person)
    
    # Protocol
    greeter = Greeter()
    greet_entity(greeter)
    
    # Literal
    print(get_status("open"))
    
    # Final
    print_api_key()
    
    # Union
    print(process_data(42))
    print(process_data("Hello"))
    
    # Callable
    def add(a: int, b: int) -> int:
        return a + b
    
    print(execute_function(add, 10, 20))
    
    # List, Dict, Tuple, Any
    demonstrate_collection_usage()
