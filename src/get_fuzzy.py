"""
Install rapidfuzz library for string matching and similarity calculation.
"""

from rapidfuzz import fuzz, process

def calculate_similarity_scores():
    """
    Calculates and prints various similarity scores between two strings using different methods from the rapidfuzz library.
    """
    # Define two strings for comparison
    string1 = "Hello, world!"
    string2 = "hello, World"

    # Calculate similarity scores
    ratio = fuzz.ratio(string1, string2)
    partial_ratio = fuzz.partial_ratio(string1, string2)
    token_sort_ratio = fuzz.token_sort_ratio(string1, string2)
    token_set_ratio = fuzz.token_set_ratio(string1, string2)

    print(f"Ratio: {ratio}")
    print(f"Partial Ratio: {partial_ratio}")
    print(f"Token Sort Ratio: {token_sort_ratio}")
    print(f"Token Set Ratio: {token_set_ratio}")

def find_best_and_multiple_matches():
    """
    Finds the best match for a query string among a list of choices and extracts multiple top matches along with their scores.
    """
    # Define a query string and a list of choices
    query = "fuzzy wuzzy was a bear"
    choices = ["fuzzy was a bear", "wuzzy fuzzy bear", "fuzzy fuzzy was a bear", "fuzzy wuzzy"]

    # Find the best match
    best_match = process.extractOne(query, choices)
    print(f"Best Match: {best_match}")

    # Extract multiple matches with scores
    matches = process.extract(query, choices, limit=3)
    print("Top Matches:")
    for match in matches:
        print(match)

if __name__ == "__main__":
    calculate_similarity_scores()
    find_best_and_multiple_matches()
