# Backend Developer Assignment

## Tech Stack

Backend:
- :contentReference[oaicite:0]{index=0}
- :contentReference[oaicite:1]{index=1}
- :contentReference[oaicite:2]{index=2}
- SQLite

Frontend:
- :contentReference[oaicite:3]{index=3}
- :contentReference[oaicite:4]{index=4}

## Features

- JWT Authentication
- Password Hashing
- Role Based Access
- Protected CRUD APIs
- Swagger Documentation

## Run Backend

```bash
cd backend
uvicorn app.main:app --reload
```

## Run Frontend

```bash
cd frontend
npm install
npm run dev
```

## API Docs

http://127.0.0.1:8000/docs

## Scalability Notes

Future improvements:

- :contentReference[oaicite:5]{index=5} caching
- Load balancing
- Microservices
- Containerization with Docker