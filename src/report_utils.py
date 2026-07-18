import re


def clean_text(text):
    """
    Clean OCR/PDF extracted medical report text.
    """

    if not text:
        return ""

    # Convert Windows line endings
    text = text.replace("\r", "\n")

    # Replace tabs with spaces
    text = text.replace("\t", " ")

    # Remove repeated dots
    text = re.sub(r"\.{2,}", " ", text)

    # Remove repeated dashes
    text = re.sub(r"-{2,}", " ", text)

    # Remove repeated underscores
    text = re.sub(r"_{2,}", " ", text)

    # Collapse multiple spaces
    text = re.sub(r"[ ]{2,}", " ", text)

    # Collapse multiple blank lines
    text = re.sub(r"\n{2,}", "\n", text)

    return text.strip()


def normalize_aliases(text):
    """
    Convert different laboratory names to one standard name.
    """

    replacements = {

        # CBC
        "Haemoglobin": "Hemoglobin",
        "HB": "Hemoglobin",
        "Hb": "Hemoglobin",

        "Platelet Count": "Platelets",

        "White Blood Cells": "WBC",
        "WBC Count": "WBC",
        "Total WBC Count": "WBC",

        # Diabetes
        "Blood Sugar": "Glucose",
        "Random Blood Sugar": "Glucose",
        "RBS": "Glucose",

        "FBS": "Fasting Blood Sugar",
        "Fasting Glucose": "Fasting Blood Sugar",

        "A1C": "HbA1c",
        "Glycated Hemoglobin": "HbA1c",

        # Lipid
        "Total Cholesterol": "Cholesterol",

        # LFT
        "SGPT": "ALT",
        "SGOT": "AST",

        # KFT
        "Serum Creatinine": "Creatinine",

        # Thyroid
        "Thyroid Stimulating Hormone": "TSH",

        # Vitamins
        "25-OH Vitamin D": "Vitamin D",

        "B12": "Vitamin B12"
    }

    for old, new in replacements.items():

        text = re.sub(
            old,
            new,
            text,
            flags=re.IGNORECASE
        )

    return text