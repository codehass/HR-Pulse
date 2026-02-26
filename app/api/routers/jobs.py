from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.authentication.auth import get_current_user
from app.db.database import get_db
from app.models.job_model import Job
from app.models.user_model import User
from app.schemas.job_schema import SalaryPredictionRequest
from ml.models.salary_prediction import SalaryPredictor

router = APIRouter(prefix="/api/v1/jobs", tags=["Jobs routes"])

MODEL_PATH = "v1/salary_xgb_model.pkl"
COLUMNS_PATH = "v1/model_columns.pkl"

predictor = SalaryPredictor(MODEL_PATH, COLUMNS_PATH)


@router.get("/search")
def search_jobs_by_skill(
    skill: str = Query(..., description="The skill to search for, e.g., 'Python'"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Search through the job descriptions for specific skills or keywords.
    """
    search_filter = f"%{skill}%"

    results = (
        db.query(Job)
        .filter(
            Job.owner_id == current_user.id,
            Job.job_description_text.like(search_filter),
        )
        .all()
    )

    return {
        "status": "success",
        "query": skill,
        "results_found": len(results),
        "data": results,
    }


@router.get("/")
def get_user_jobs(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    """
    Retrieve all salary predictions created by the logged-in user.
    """
    jobs = db.query(Job).filter(Job.owner_id == current_user.id).all()
    return {"status": "success", "count": len(jobs), "data": jobs}


@router.post("/salary_prediction", status_code=status.HTTP_201_CREATED)
def predict_and_save_salary(
    payload: SalaryPredictionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        salary = predictor.predict(
            revenue=payload.revenue,
            years_exp=payload.years_exp,
            location=payload.location,
            ownership=payload.ownership,
            sector=payload.sector,
            job_description_text=payload.job_description_text,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"ML Model Prediction Error: {str(e)}",
        ) from e

    new_job = Job(
        **payload.model_dump(), predicted_salary=salary, owner_id=current_user.id
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return {
        "status": "success",
        "job_id": new_job.id,
        "predicted_salary": round(salary, 2),
        "currency": "USD",
        "owner": current_user.username,
    }
