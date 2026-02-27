FROM python:3.11-slim

WORKDIR /code

COPY pyproject.toml uv.lock ./
RUN pip install uv
RUN uv sync --frozen

COPY ./app /code/app
COPY ./ml /code/ml 

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
