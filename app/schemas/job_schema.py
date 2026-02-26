from pydantic import BaseModel, Field


class SalaryPredictionRequest(BaseModel):
    revenue: int = Field(..., example=5000000)
    years_exp: int = Field(..., example=3)
    location: str = Field(..., example="NY")
    ownership: str = Field(..., example="Private")
    sector: str = Field(..., example="Information Technology")
    job_description_text: str = Field(..., example="Looking for a Data Scientist...")
