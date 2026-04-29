from database import engine

from models import courses 
 

sample_courses = [
   {
       "title": "Introduction to Artificial Intelligence",
       "description": "Learn AI basics, machine learning, neural networks, and intelligent systems.",
       "skills": "ai, artificial intelligence, machine learning, neural networks"
   },
   {
       "title": "Backend Development with Flask",
       "description": "Learn backend development using Python Flask, APIs, routes, and databases.",
       "skills": "backend, flask, python, api"
   },
   {
       "title": "Database Fundamentals",
       "description": "Learn SQL, database design, tables, relationships, and queries.",
       "skills": "database, sql, tables"
   },
   {
       "title": "Data Analysis with Python",
       "description": "Analyze data using Python, pandas, charts, and data cleaning.",
       "skills": "data analysis, python, pandas"
   },
   {
       "title": "Web Development Basics",
       "description": "Learn HTML, CSS, JavaScript, and frontend web development.",
       "skills": "html, css, javascript, frontend"
   },
   {
       "title": "Machine Learning Course",
       "description": "Build machine learning models using supervised and unsupervised learning.",
       "skills": "machine learning, ai, models"
   },
   {
       "title": "Cyber Security Fundamentals",
       "description": "Learn cyber security basics, network security, threats, attacks, encryption, and protection.",
       "skills": "cyber security, cybersecurity, security, network security, attacks, encryption"
   },
   {
       "title": "Ethical Hacking Basics",
       "description": "Learn ethical hacking, penetration testing, vulnerabilities, and security tools.",
       "skills": "ethical hacking, penetration testing, vulnerabilities, security, cyber security"
   },
   {
       "title": "Network Security",
       "description": "Learn how to secure networks, firewalls, protocols, and detect attacks.",
       "skills": "network security, firewall, protocols, cyber security"
   },
]

with engine.connect() as conn:
   conn.execute(courses.delete())
   conn.execute(courses.insert(), sample_courses)
   conn.commit()

print("Database created and courses inserted successfully.")