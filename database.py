from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:a1234@localhost:5432/recommendation_db"

engine = create_engine(DATABASE_URL, echo=True)