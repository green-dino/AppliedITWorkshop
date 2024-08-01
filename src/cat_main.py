from typing import List
from cat_data import Cat, cats

def display_cats(cats: List[Cat]) -> None:
    for cat in cats:
        print(cat)

def find_cat_by_name(cats: List[Cat], name: str) -> Cat:
    for cat in cats:
        if cat.name == name:
            return cat
    raise ValueError(f"No cat found with name{name}")

 