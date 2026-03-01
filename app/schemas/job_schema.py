from pydantic import BaseModel, Field


class SalaryPredictionRequest(BaseModel):
    revenue: int = Field(..., json_schema_extra={"example": 5000000})
    years_exp: int = Field(..., json_schema_extra={"example": 3})
    location: str = Field(..., json_schema_extra={"example": "NY"})
    ownership: str = Field(..., json_schema_extra={"example": "Private"})
    sector: str = Field(..., json_schema_extra={"example": "Information Technology"})
    job_description_text: str = Field(
        ..., json_schema_extra={"example": "Looking for..."}
    )


class JobSkillsCreate(BaseModel):
    id: int
    job_title: str | None = "Unknown"
    skills_extracted: list[str]


class JobSkillsResponse(JobSkillsCreate):
    class Config:
        from_attributes = True
