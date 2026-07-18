import re
from src.report_database import LAB_TESTS


def extract_value(text, alias):
    """
    Extract numeric value after a test name.
    Supports multiple report layouts.
    """

    patterns = [
        # 150
        # Cholesterol Total
        rf"([0-9]+(?:\.[0-9]+)?)\s*\n\s*{re.escape(alias)}",
        # 150 Cholesterol Total
        rf"([0-9]+(?:\.[0-9]+)?)\s+{re.escape(alias)}",

        # Hemoglobin 13.5
        rf"{re.escape(alias)}\s+([0-9]+(?:\.[0-9]+)?)",

        # Hemoglobin : 13.5
        rf"{re.escape(alias)}\s*:\s*([0-9]+(?:\.[0-9]+)?)",

        # Hemoglobin = 13.5
        rf"{re.escape(alias)}\s*=\s*([0-9]+(?:\.[0-9]+)?)",

        # Hemoglobin - 13.5
        rf"{re.escape(alias)}\s*-\s*([0-9]+(?:\.[0-9]+)?)",

        # Hemoglobin.....13.5
        rf"{re.escape(alias)}[\.\s]*([0-9]+(?:\.[0-9]+)?)",

        # Hemoglobin
        # 13.5
        rf"{re.escape(alias)}[\s\n\r]+([0-9]+(?:\.[0-9]+)?)",

        # Hemoglobin    13.5    g/dL
        rf"{re.escape(alias)}\s+([0-9]+(?:\.[0-9]+)?)\s*[A-Za-z/%]+",

        # Hemoglobin    13.5    12-16
        rf"{re.escape(alias)}\s+([0-9]+(?:\.[0-9]+)?)\s+\d+(?:\.\d+)?",

    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE | re.MULTILINE
        )

        if match:
            try:
                return float(match.group(1))
            except ValueError:
                continue

    return None

def parse_report(text):
    # print("\n===== PARSER RUNNING =====")
    # print(text[:500])  # Print first 500 characters

    report = {}

    for test_name, info in LAB_TESTS.items():

        for alias in info["aliases"]:

            value = extract_value(text, alias)

            if value is None:
                continue

            report[test_name] = {

                "value": value,
                "unit": info["unit"],
                "category": info["category"],
                "reference": {
                    "low": info["low"],
                    "high": info["high"]
                }

            }

            break

    return report