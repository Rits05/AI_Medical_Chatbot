import pandas as pd


class MedicineDatabase:
    def __init__(self, csv_path="medicine.csv"):
        self.df = pd.read_csv(csv_path)

        # Convert medicine names to lowercase for easy searching
        self.df["medicine"] = self.df["medicine"].str.lower()

    def search_medicine(self, question):
        """
        Search for a medicine name in the user's question.
        Returns medicine details if found, else None.
        """

        question = question.lower()

        for _, row in self.df.iterrows():

            if row["medicine"] in question:

                return {
                    "medicine": row["medicine"].title(),
                    "used_for": row["used_for"],
                    "side_effects": row["side_effects"],
                    "interactions": row["interactions"],
                    "contraindications": row["contraindications"]
                }

        return None