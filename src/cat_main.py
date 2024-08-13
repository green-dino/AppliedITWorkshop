from typing import List, Optional
import json
from cat_data import Cat, cats


def display_cats(cats: List[Cat]) -> None:
    """
    Displays information about all cats in the given list.

    Parameters:
    - cats (List[Cat]): A list of Cat objects to display.

    Returns:
    - None
    """
    for cat in cats:
        print(cat)


def find_cat_by_name(cats: List[Cat], name: str) -> Cat:
    """
    Finds and returns a Cat object by its name from the given list.

    Parameters:
    - cats (List[Cat]): A list of Cat objects to search through.
    - name (str): The name of the cat to find.

    Returns:
    - Cat: The Cat object with the matching name, or raises a ValueError if not found.
    """
    for cat in cats:
        if cat.name == name:
            return cat
    raise ValueError(f"No cat found with name {name}")


def add_cat(
    cats: List[Cat], name: str, breed: str, color: str, age: int, personality: str
) -> None:
    """
    Adds a new Cat object to the given list.

    Parameters:
    - cats (List[Cat]): The list of Cat objects to which the new cat will be added.
    - name (str): The name of the new cat.
    - breed (str): The breed of the new cat.
    - color (str): The color of the new cat.
    - age (int): The age of the new cat.
    - personality (str): The personality description of the new cat.

    Returns:
    - None
    """
    new_cat = Cat(name, breed, color, age, personality)
    cats.append(new_cat)


def remove_cat(cats: List[Cat], name: str) -> None:
    """
    Removes a Cat object with the specified name from the given list.

    Parameters:
    - cats (List[Cat]): The list of Cat objects from which the cat will be removed.
    - name (str): The name of the cat to remove.

    Returns:
    - None
    """
    cat = find_cat_by_name(cats, name)
    if cat:
        cats.remove(cat)
    else:
        raise ValueError(f"No cat found with {name}")


def update_cat(
    cats: List[Cat],
    name: str,
    breed: Optional[str] = None,
    color: Optional[str] = None,
    age: Optional[int] = None,
    personality: Optional[str] = None,
) -> None:
    """
    Updates the attributes of a Cat object with the specified name in the given list.

    Parameters:
    - cats (List[Cat]): The list of Cat objects to update.
    - name (str): The name of the cat to update.
    - breed (Optional[str]): The new breed of the cat, defaults to None.
    - color (Optional[str]): The new color of the cat, defaults to None.
    - age (Optional[int]): The new age of the cat, defaults to None.
    - personality (Optional[str]): The new personality description of the cat, defaults to None.

    Returns:
    - None
    """
    cat = find_cat_by_name(cats, name)
    if cat:
        if breed:
            cat.breed = breed
        if color:
            cat.color = color
        if age:
            cat.age = age
        if personality:
            cat.personality = personality
    else:
        raise ValueError(f"No cat found with {name}")


def sort_cats_by_age(cats: List[Cat]) -> List[Cat]:
    """
    Sorts the given list of Cat objects by their age.

    Parameters:
    - cats (List[Cat]): The list of Cat objects to sort.

    Returns:
    - List[Cat]: The sorted list of Cat objects.
    """
    return sorted(cats, key=lambda cat: cat.age)
