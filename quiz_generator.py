import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample quiz data (you can replace this with your own data)
quiz_data = {
    "history": [
        {"question": "What was the capital of the Roman Empire?", "answer": "Rome"},
        {"question": "Who was the first president of the United States?", "answer": "George Washington"},
        {"question": "What was the name of the famous ship that sank in 1912?", "answer": "Titanic"}
    ],
    "science": [
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "What is the process by which water moves through a plant?", "answer": "Transpiration"},
        {"question": "What is the smallest unit of life?", "answer": "Cell"}
    ],
    "sports": [
        {"question": "Which team won the Super Bowl in 2020?", "answer": "Kansas City Chiefs"},
        {"question": "Who is the all-time leading scorer in the NBA?", "answer": "Kareem Abdul-Jabbar"},
        {"question": "What is the fastest land animal?", "answer": "Cheetah"}
    ]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_quiz", methods=["POST"])
def generate_quiz():
    topic = request.form["topic"]
    num_questions = int(request.form["num_questions"])
    quiz = []
    for i in range(num_questions):
        question = random.choice(quiz_data[topic])
        quiz.append(question)
        quiz_data[topic].remove(question)  # remove the question from the list to avoid duplicates
    return jsonify({"quiz": quiz})

if __name__ == "__main__":
    app.run(debug=True)
