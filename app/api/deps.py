from app import  models
from app.core.db import engine

models.Base.metadata.create_all(bind=engine)

# Dependency
from app.core.db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()