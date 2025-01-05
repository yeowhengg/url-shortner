# url-shortner

simple url shortener for a side project

steps to run:

1. populate RENAME_TO_BLANK.env to your own domain and port, rename it to .env

2. with docker compose, run docker compose up --build
    2.1 subsequent runs can be run with the command docker compose up
    2.2 if you do not want to run with docker compose,
        cd app followed by uvicorn main:app --host localhost --port 8000 --reload

3. check waypoints in localhost:8000/docs