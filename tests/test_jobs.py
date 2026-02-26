import pytest


@pytest.fixture
def logged_in_client(client):
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "jobtester",
            "email": "job@test.com",
            "password": "password123",
        },
    )

    login_response = client.post(
        "/api/v1/auth/login",
        data={"username": "jobtester", "password": "password123"},
    )

    assert login_response.status_code == 200

    cookie_header = login_response.headers.get("set-cookie")
    if not cookie_header:
        pytest.fail("Login succeeded but no Set-Cookie header was found!")

    token_part = cookie_header.split(";")[0]

    client.headers.update({"Cookie": token_part})

    return client


def test_predict_and_save_salary(logged_in_client):
    payload = {
        "revenue": 5000000,
        "years_exp": 3,
        "location": "NY",
        "ownership": "Private",
        "sector": "Information Technology",
        "job_description_text": "Looking for a Python developer with XGBoost skills",
    }

    response = logged_in_client.post("/api/v1/jobs/salary_prediction", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "success"
    assert "predicted_salary" in data


def test_get_user_jobs(logged_in_client):
    logged_in_client.post(
        "/api/v1/jobs/salary_prediction",
        json={
            "revenue": 1000,
            "years_exp": 1,
            "location": "Remote",
            "ownership": "Startup",
            "sector": "Tech",
            "job_description_text": "Test",
        },
    )

    response = logged_in_client.get("/api/v1/jobs/")
    assert response.status_code == 200
    assert len(response.json()["data"]) >= 1


def test_search_jobs_by_skill(logged_in_client):
    logged_in_client.post(
        "/api/v1/jobs/salary_prediction",
        json={
            "revenue": 1,
            "years_exp": 1,
            "location": "A",
            "ownership": "B",
            "sector": "C",
            "job_description_text": "Expert in Java",
        },
    )
    logged_in_client.post(
        "/api/v1/jobs/salary_prediction",
        json={
            "revenue": 1,
            "years_exp": 1,
            "location": "A",
            "ownership": "B",
            "sector": "C",
            "job_description_text": "Expert in Python",
        },
    )

    response = logged_in_client.get("/api/v1/jobs/search?skill=Python")
    assert response.status_code == 200
    results = response.json()["data"]
    assert len(results) == 1
    assert "Python" in results[0]["job_description_text"]
