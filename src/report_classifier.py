from src.report_database import LAB_TESTS


def classify_report(report):

    categories = {}

    for _, data in report.items():

        category = data["category"]

        categories[category] = categories.get(category, 0) + 1

    if not categories:
        return "Unknown"

    return max(categories, key=categories.get)