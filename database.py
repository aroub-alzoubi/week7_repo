from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text

engine = create_engine("sqlite:///Recommendation.db", echo=True)

metadata = MetaData()

courses = Table(
   "courses",
   metadata,
   Column("id", Integer, primary_key=True),
   Column("title", String(100), nullable=False),
   Column("description", Text, nullable=False),
   Column("skills", Text, nullable=False),
)

def create_database():
   metadata.create_all(engine)