import os

import joblib
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer


class SalaryPredictor:
    def __init__(self, model_filename, columns_filename):
        base_path = os.path.dirname(__file__)
        self.model = joblib.load(os.path.join(base_path, model_filename))
        self.model_columns = joblib.load(os.path.join(base_path, columns_filename))
        self.encoder = SentenceTransformer("all-MiniLM-L6-v2")
        print("Predictor ready.")

    def predict(
        self, revenue, years_exp, location, ownership, sector, job_description_text
    ):
        input_df = pd.DataFrame(
            [
                {
                    "Revenue": revenue,
                    "years_exp_required": years_exp,
                    "Location": location,
                    "Type of ownership": ownership,
                    "Sector": sector,
                }
            ]
        )

        input_df_encoded = pd.get_dummies(input_df)

        for col in self.model_columns:
            if col not in input_df_encoded.columns:
                input_df_encoded[col] = 0

        X_tabular = input_df_encoded[self.model_columns].values

        desc_vector = self.encoder.encode([job_description_text])

        X_combined = np.hstack([X_tabular, desc_vector])

        prediction = self.model.predict(X_combined)
        return float(prediction[0])


# # --- TEST SCRIPT ---
# if __name__ == "__main__":
#     # Ensure you saved 'model_columns.pkl' from your training script first!
# predictor = SalaryPredictor("v1/salary_xgb_model.pkl", "v1/model_columns.pkl")

# sample_job_desc = "We are looking for a Data Scientist with 3 years of experience in Python and XGBoost."

# salary = predictor.predict(
#     revenue=5000000,
#     years_exp=3,
#     location="NY",
#     ownership="Private",
#     sector="Information Technology",
#     job_description_text=sample_job_desc,
# )

#     print(f"Predicted Salary: ${salary:,.2f}")
