import os
import time

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.getenv("ENDPOINT")
KEY = os.getenv("KEY")

client = TextAnalyticsClient(ENDPOINT, AzureKeyCredential(KEY))


def extract_skills_in_batches(df, column_name, batch_size=5):
    all_results = []
    descriptions = df[column_name].tolist()

    for i in range(0, len(descriptions), batch_size):
        batch = descriptions[i : i + batch_size]

        batch = [doc[:5000] for doc in batch]

        try:
            responses = client.recognize_entities(documents=batch)

            for doc in responses:
                if not doc.is_error:
                    skills = [
                        ent.text.lower()
                        for ent in doc.entities
                        if ent.category == "Skill"
                    ]
                    all_results.append(list(set(skills)))
                else:
                    all_results.append([])

            print(f"Processed up to row {i + batch_size}")

        except Exception as e:
            print(f"Error at batch starting at index {i}: {e}")
            all_results.extend([[]] * len(batch))

        time.sleep(0.1)

    return all_results
