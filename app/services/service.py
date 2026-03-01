import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.job_model import Job, JobSkills  # noqa: F401
from app.models.user_model import User  # noqa: F401

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


def upload_limited_csv(file_path):
    try:
        df = pd.read_csv(file_path, nrows=100)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return

    print(f"Processing {len(df)} rows...")

    for index, row in df.iterrows():
        raw_skills = str(row["extracted_skills"])
        skills_list = [s.strip() for s in raw_skills.split(",") if s.strip()]

        job_entry = JobSkills(
            id=int(index) + 1,
            job_title="Unknown",
            skills_extracted=skills_list,
        )

        session.merge(job_entry)

    try:
        session.commit()
        print("✅ Successfully uploaded the first 100 rows!")
        print(df.columns.tolist())
    except Exception as e:
        session.rollback()
        print(f"❌ Database Error: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    upload_limited_csv("ml/extracted_skills_only.csv")
