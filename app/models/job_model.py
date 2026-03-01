from sqlalchemy import JSON, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..db.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    revenue = Column(Integer)
    years_exp = Column(Integer)
    location = Column(String(100))
    ownership = Column(String(100))
    sector = Column(String(100))
    job_description_text = Column(Text)
    predicted_salary = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="jobs")


class JobSkills(Base):
    __tablename__ = "job_skills"
    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String(100), nullable=True)
    skills_extracted = Column(JSON)
