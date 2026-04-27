from flask import Flask, request, render_template, jsonify
from database import create_database
from recommender import recommend_courses

app = Flask(__name__)

create_database()


@app.route("/", methods=["GET", "POST"])
def home():
   recommendations = []

   if request.method == "POST":
       user_input = request.form.get("skills")
       recommendations = recommend_courses(user_input)

   return render_template("index.html", recommendations=recommendations)


@app.route("/api/recommend", methods=["POST"])
def api_recommend():
   data = request.get_json()

   user_input = data.get("text", "")

   results = recommend_courses(user_input)

   return jsonify({
       "input": user_input,
       "recommended_courses": results
   })


if __name__ == "__main__":
   app.run(debug=True)