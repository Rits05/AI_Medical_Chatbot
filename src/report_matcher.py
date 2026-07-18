from rapidfuzz import fuzz
from src.report_database import LAB_TESTS


def find_matching_test(line, threshold=85):
    """
    Finds the best matching laboratory test
    from a line of text.
    """

    best_test = None
    best_score = 0

    line = line.lower()

    for test_name, info in LAB_TESTS.items():

        for alias in info["aliases"]:

            score = fuzz.partial_ratio(
                alias.lower(),
                line
            )

            if score > best_score:

                best_score = score
                best_test = test_name

    if best_score >= threshold:
        return best_test

    return None