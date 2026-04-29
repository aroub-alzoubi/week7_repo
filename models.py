from sqlalchemy import MetaData, Table, Column, Integer, String, Text, ForeignKey, DateTime
from datetime import datetime

metadata = MetaData()

users = Table(
   "users",
   metadata,
   Column("id", Integer, primary_key=True),
   Column("name", String(100), nullable=False)
)

skills = Table(
   "skills",
   metadata,
   Column("id", Integer, primary_key=True),
   Column("name", String(100), nullable=False, unique=True)
)

courses = Table(
   "courses",
   metadata,
   Column("id", Integer, primary_key=True),
   Column("title", String(200), nullable=False),
   Column("description", Text, nullable=False),
   Column("skills", Text, nullable=True)
)

user_skills = Table(
   "user_skills",
   metadata,
   Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
   Column("skill_id", Integer, ForeignKey("skills.id"), primary_key=True)
)

recommendation_logs = Table(
   "recommendation_logs",
   metadata,
   Column("id", Integer, primary_key=True),
   Column("user_input", Text, nullable=False),
   Column("recommended_course", String(200), nullable=False),
   Column("created_at", DateTime, default=datetime.now)
)