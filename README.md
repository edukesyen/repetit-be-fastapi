# repetit-be-fastapi

## Initial Setup

1. clone repository `git clone https://github.com/edukesyen/repetit-be-fastapi.git`

2. navigate to the project's directory `cd repetit-be-fastapi`

3. install all dependencies `pdm install`

4. create and setup environment variable on file `.env`

5. activate python virtual env `source .venv/bin/activate` (on linux)

6. create alembic version table if it doesn't exist `alembic ensure_version`

7. upgrade migration to latest version `alembic upgrade head`

8. run the development server `uvicorn app.main:app --reload`
