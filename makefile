install:
	pip install -r requirements.txt

run:
	uvicorn main:app --reload

run-migrate:
	alembic upgrade head
