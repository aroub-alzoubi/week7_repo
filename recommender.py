from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from database import engine, courses


def extract_skills(user_input):
   if not user_input:
       return ""
   return user_input.lower().strip()


def get_all_courses():
   with engine.connect() as conn:
       result = conn.execute(courses.select()).fetchall()

   course_list = []

   for row in result:
       course_list.append({
           "title": row.title,
           "description": row.description,
           "skills": row.skills
       })

   return course_list


def recommend_courses(user_input):
   user_text = extract_skills(user_input)

   if not user_text:
       return []

   course_list = get_all_courses()

   if not course_list:
       return []

   course_texts = [
       course["skills"] + " " + course["description"]
       for course in course_list
   ]

   vectorizer = TfidfVectorizer()
   vectors = vectorizer.fit_transform(course_texts + [user_text])

   course_vectors = vectors[:-1]
   user_vector = vectors[-1]

   scores = cosine_similarity(user_vector, course_vectors)[0]

   recommendations = []
   threshold = 0.12

   for course, score in zip(course_list, scores):
       if score >= threshold:
           recommendations.append({
               "title": course["title"],
               "description": course["description"],
               "skills": course["skills"],
               "score": round(float(score), 3),
               "explanation": "Recommended because it matches your entered skills or interests."
           })

   recommendations = sorted(
       recommendations,
       key=lambda x: x["score"],
       reverse=True
   )

   return recommendations[:3]