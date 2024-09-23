# go to exec of web app and run the below migration commands 

alembic revision --autogenerate -m "New Migration"
alembic upgrade head

docker compose up --build