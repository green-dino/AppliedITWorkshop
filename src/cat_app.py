from typing import Dict
from cat_data import Cat , cats
from cat_main import display_cats, add_cat, remove_cat, update_cat, sort_cats_by_age

# User command mapping
COMMANDS : Dict[str, str] = {
    "display": "display_cats",
    "add": "add_cat",
    "remove": "remove_cat",
    "update": "update_cat",
    "sort": "sort_cats_by_age",
}

def main():
    while True:
        print("\nWelcome to the Cat Management System")
        print("Enter 'exit' to quit.")

        # display the COMMANDS
        for cmd, func in COMMANDS.items():
            print(f"{cmd}: {func.capitalize()}")

        user_input = input("Select and option: ").strip().lower()

        if user_input == 'exit':
            break
        
        try:
            func_name = COMMANDS.get(user_input, "")
            if func_name:
                if func_name == "display_cats":
                    display_cats(cats)
                elif func_name == "sort_cats_by_age":
                    sorted_cats = sort_cats_by_age(cats)
                    display_cats(sorted_cats)
                elif func_name == "add_cat":
                    name = input("Enter the cat's name: ")
                    breed = input("Enter the cat's breed: ")
                    color = input("Enter the cat's color: ")
                    age = int(input("Enter the cat's age: "))
                    personality = input("Enter the cat's personality: ")
                    add_cat(cats, name, breed, color, age, personality)
                elif func_name == "remove_cat":
                    name = input("Enter the name of the cat to remove: ")
                    remove_cat(cats, name)
                elif func_name == "update_cat":
                    name = input("Enter the name of the cat to update: ")
                    breed = input("Enter the new breed (leave empty to keep current): ") or None
                    color = input("Enter the new color (leave empty to keep current): ") or None
                    age = input("Enter the new age (leave empty to keep current): ")
                    age = int(age) if age else None
                    personality = input("Enter the new personality (leave empty to keep current): ") or None
                    update_cat(cats, name, breed, color, age, personality)
                    

            # clear the console screen on exit
            print("\033c", end="")
        
        except KeyError:
            print("Invalid Command. Try again.")
if __name__ == "__main__":
    main()