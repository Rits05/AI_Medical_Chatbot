LAB_TESTS = {

    # =========================
    # CBC (Complete Blood Count)
    # =========================

    "Hemoglobin": {
        "aliases": ["Hemoglobin", "Haemoglobin", "Hb", "HB"],
        "category": "CBC",
        "unit": "g/dL",
        "low": 12,
        "high": 16
    },

    "RBC": {
        "aliases": [
            "RBC",
            "RBC Count",
            "Red Blood Cell Count",
            "Red Blood Cells"
        ],
        "category": "CBC",
        "unit": "million/uL",
        "low": 4.2,
        "high": 5.8
    },

    "WBC": {
        "aliases": [
            "WBC",
            "WBC Count",
            "White Blood Cells",
            "Total WBC Count"
        ],
        "category": "CBC",
        "unit": "/uL",
        "low": 4000,
        "high": 11000
    },

    "Platelets": {
        "aliases": [
            "Platelets",
            "Platelet Count",
            "Platelet"
        ],
        "category": "CBC",
        "unit": "/uL",
        "low": 150000,
        "high": 450000
    },

    "Hematocrit": {
        "aliases": [
            "Hematocrit",
            "PCV",
            "Packed Cell Volume"
        ],
        "category": "CBC",
        "unit": "%",
        "low": 36,
        "high": 50
    },

    "MCV": {
        "aliases": ["MCV", "Mean Corpuscular Volume"],
        "category": "CBC",
        "unit": "fL",
        "low": 80,
        "high": 100
    },

    "MCH": {
        "aliases": ["MCH"],
        "category": "CBC",
        "unit": "pg",
        "low": 27,
        "high": 33
    },

    "MCHC": {
        "aliases": ["MCHC"],
        "category": "CBC",
        "unit": "g/dL",
        "low": 32,
        "high": 36
    },

    # =========================
    # Diabetes
    # =========================

    "Glucose": {
        "aliases": [
            "Glucose",
            "Blood Glucose",
            "Blood Sugar",
            "Random Blood Sugar",
            "RBS"
        ],
        "category": "Diabetes",
        "unit": "mg/dL",
        "low": 70,
        "high": 140
    },

    "Fasting Blood Sugar": {
        "aliases": [
            "FBS",
            "Fasting Blood Sugar",
            "Glucose Fasting",
            "Fasting Glucose"
        ],
        "category": "Diabetes",
        "unit": "mg/dL",
        "low": 70,
        "high": 99
    },

    "HbA1c": {
        "aliases": [
            "HbA1c",
            "A1C",
            "Glycated Hemoglobin"
        ],
        "category": "Diabetes",
        "unit": "%",
        "low": 4,
        "high": 5.6
    },

    # =========================
    # Lipid Profile
    # =========================

    "Total Cholesterol": {
        "aliases": [
            "Cholesterol",
            "Total Cholesterol"
        ],
        "category": "Lipid",
        "unit": "mg/dL",
        "low": 0,
        "high": 200
    },

    "HDL": {
        "aliases": [
            "HDL",
            "HDL Cholesterol"
        ],
        "category": "Lipid",
        "unit": "mg/dL",
        "low": 40,
        "high": 100
    },

    "LDL": {
        "aliases": [
            "LDL",
            "LDL Cholesterol"
        ],
        "category": "Lipid",
        "unit": "mg/dL",
        "low": 0,
        "high": 100
    },

    "Triglycerides": {
        "aliases": [
            "Triglycerides",
            "TG"
        ],
        "category": "Lipid",
        "unit": "mg/dL",
        "low": 0,
        "high": 150
    },

    # =========================
    # Liver Function Test
    # =========================

    "ALT": {
        "aliases": [
            "ALT",
            "SGPT"
        ],
        "category": "LFT",
        "unit": "U/L",
        "low": 0,
        "high": 56
    },

    "AST": {
        "aliases": [
            "AST",
            "SGOT"
        ],
        "category": "LFT",
        "unit": "U/L",
        "low": 0,
        "high": 40
    },

    "Bilirubin": {
        "aliases": [
            "Bilirubin",
            "Total Bilirubin"
        ],
        "category": "LFT",
        "unit": "mg/dL",
        "low": 0.2,
        "high": 1.2
    },

    "Albumin": {
        "aliases": [
            "Albumin"
        ],
        "category": "LFT",
        "unit": "g/dL",
        "low": 3.5,
        "high": 5.0
    },

    # =========================
    # Kidney Function Test
    # =========================

    "Creatinine": {
        "aliases": [
            "Creatinine",
            "Serum Creatinine"
        ],
        "category": "KFT",
        "unit": "mg/dL",
        "low": 0.7,
        "high": 1.3
    },

    "Urea": {
        "aliases": [
            "Urea",
            "Blood Urea"
        ],
        "category": "KFT",
        "unit": "mg/dL",
        "low": 15,
        "high": 40
    },

    "Uric Acid": {
        "aliases": [
            "Uric Acid"
        ],
        "category": "KFT",
        "unit": "mg/dL",
        "low": 3.5,
        "high": 7.2
    },

    # =========================
    # Thyroid
    # =========================

    "TSH": {
        "aliases": [
            "TSH",
            "Thyroid Stimulating Hormone"
        ],
        "category": "Thyroid",
        "unit": "uIU/mL",
        "low": 0.4,
        "high": 4.5
    },

    "T3": {
        "aliases": [
            "T3",
            "Triiodothyronine"
        ],
        "category": "Thyroid",
        "unit": "ng/dL",
        "low": 80,
        "high": 200
    },

    "T4": {
        "aliases": [
            "T4",
            "Thyroxine"
        ],
        "category": "Thyroid",
        "unit": "ug/dL",
        "low": 5,
        "high": 12
    },

    # =========================
    # Vitamins
    # =========================

    "Vitamin D": {
        "aliases": [
            "Vitamin D",
            "25-OH Vitamin D"
        ],
        "category": "Vitamin",
        "unit": "ng/mL",
        "low": 30,
        "high": 100
    },

    "Vitamin B12": {
        "aliases": [
            "Vitamin B12",
            "B12"
        ],
        "category": "Vitamin",
        "unit": "pg/mL",
        "low": 200,
        "high": 900
    },

    # =========================
    # Iron Profile
    # =========================

    "Serum Iron": {
        "aliases": [
            "Serum Iron",
            "Iron"
        ],
        "category": "Iron",
        "unit": "ug/dL",
        "low": 60,
        "high": 170
    },

    "Ferritin": {
        "aliases": [
            "Ferritin"
        ],
        "category": "Iron",
        "unit": "ng/mL",
        "low": 20,
        "high": 250
    },

    # =========================
    # Electrolytes
    # =========================

    "Sodium": {
        "aliases": [
            "Sodium",
            "Na+"
        ],
        "category": "Electrolytes",
        "unit": "mmol/L",
        "low": 135,
        "high": 145
    },

    "Potassium": {
        "aliases": [
            "Potassium",
            "K+"
        ],
        "category": "Electrolytes",
        "unit": "mmol/L",
        "low": 3.5,
        "high": 5.1
    },

    "Chloride": {
        "aliases": [
            "Chloride",
            "Cl-"
        ],
        "category": "Electrolytes",
        "unit": "mmol/L",
        "low": 98,
        "high": 107
    }
}