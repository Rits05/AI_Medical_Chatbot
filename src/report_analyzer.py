def analyze_report(report):

    analysis = {

        "normal": [],
        "high": [],
        "low": [],
        "categories": {}

    }

    for test, data in report.items():

        value = data["value"]

        low = data["reference"]["low"]

        high = data["reference"]["high"]

        unit = data["unit"]

        category = data["category"]

        # -------------------------
        # Determine Status
        # -------------------------

        if value < low:

            status = "Low"

            analysis["low"].append(
                f"{test}: {value} {unit} (Normal: {low}-{high})"
            )

        elif value > high:

            status = "High"

            analysis["high"].append(
                f"{test}: {value} {unit} (Normal: {low}-{high})"
            )

        else:

            status = "Normal"

            analysis["normal"].append(
                f"{test}: {value} {unit}"
            )

        # -------------------------
        # Category-wise storage
        # -------------------------

        if category not in analysis["categories"]:

            analysis["categories"][category] = []

        analysis["categories"][category].append({

            "test": test,

            "value": value,

            "unit": unit,

            "status": status,

            "reference": f"{low}-{high}"

        })

    return analysis