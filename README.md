# Simple Todo App with FastAPI

## https://simple-todo-app-nu-seven.vercel.app/

### A minimal Todo web application that allows you to keep track of your chores.

![Screenshot 2025-11-11 at 16 30 13](https://github.com/user-attachments/assets/2f41101a-9173-460a-9ebd-8449ef440d61)

This project is a learning implementation that follows the truly wonderful Udemy course [FastAPI - The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/). The focus is server side development with Python's FastAPI. The frontend is intentionally minimal and template driven so the attention stays on the API, auth, data layer, and tests.

## Using the app
1. [Visit the URL](https://simple-todo-app-nu-seven.vercel.app/).
2. Register a new account.
3. Log in using your username and password. The login expects the username field, not email.
4. Create, edit, and delete todos.

## Tech stack
- FastAPI and Starlette
- SQLAlchemy 2.x and Alembic
- PostgreSQL on [Neon](https://neon.com/) with connection pooling
- Jinja2 templates
- Uvicorn for local development
- Auth with OAuth2PasswordBearer, JSON Web Tokens via python‑jose, password hashing with passlib bcrypt
- Bootstrap and a small amount of client side JavaScript
- Pytest for unit tests

## Run locally
The app reads the database URL from the environment variable `SQLALCHEMY_DATABASE_URL`. If you want to run this repo locally, you are going to have to put the path of your database (postgresql or otherwise) in the `.env` file at the root of your repo, like so:

```
SQLALCHEMY_DATABASE_URL=postgresql://neondb_owner:PASSWORD@DATABASE-pooler.gwc.azure.neon.tech:5432/neondb?sslmode=require&channel_binding=require
```

`TodoApp/database.py` calls `load_dotenv()` so the `.env` file is picked up automatically during local runs. Don't forget to add the`.env` file to `.gitignore`!

### Install requirements and run the repo:
```
python -m venv fastapienv
source fastapienv/bin/activate
pip install -r requirements.txt
uvicorn TodoApp.main:app --reload
```
Open http://127.0.0.1:8000

## Tests
Run the provided unit tests with
```
pytest -vv
```
The tests mock a dedicated SQLite database and dependency overrides, so your production database is not affected by the tests.


