import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


def manage_student_grades():
    """
    Manages a dictionary of student grades.

    This function demonstrates various operations on a dictionary,
    such as adding, modifying, deleting entries, retrieving values,
    checking for keys, iterating over items, using dictionary methods,
    and clearing the dictionary.
    """
    # Step 1: Create a dictionary
    student_grades = {}

    # Step 2: Add entries
    student_grades["Alex"] = 85
    student_grades["Bella"] = 92
    student_grades["Casey"] = 78
    student_grades["Dana"] = 90
    student_grades["Ethan"] = 88

    # Log the addition of entries
    logging.info("Added initial set of student grades.")

    # Step 3: Modify an entry
    student_grades["Alex"] = 95

    # Log the modification of an entry
    logging.info("Updated Alex's grade.")

    # Step 4: Delete an entry
    del student_grades["Casey"]

    # Log the deletion of an entry
    logging.info("Removed Casey's grade from the dictionary.")

    # Step 5: Retrieve a value
    grade_of_bella = student_grades.get("Bella")
    logging.info(f"Retrieved Bella's grade: {grade_of_bella}")

    # Step 6: Check for a key
    is_dana_present = "Dana" in student_grades
    logging.info(f"Dana present in the dictionary: {is_dana_present}")

    # Step 7: Iterate over the dictionary
    logging.info("Iterating over all students and their grades:")
    for student, grade in student_grades.items():
        logging.info(f"{student}: {grade}")

    # Step 8: Use dictionary methods
    logging.info("Using dictionary methods to retrieve keys, values, and items:")
    logging.info(f"Student names: {list(student_grades.keys())}")
    logging.info(f"Grades: {list(student_grades.values())}")
    logging.info(f"Students and grades: {list(student_grades.items())}")

    # Step 9: Clear the dictionary
    student_grades.clear()

    # Log the clearing of the dictionary
    logging.info("Cleared the dictionary.")


if __name__ == "__main__":
    manage_student_grades()
