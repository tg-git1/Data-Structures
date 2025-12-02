from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

stack = []
queue = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lesson", methods=["POST"])
def start_lesson():
    topic = request.json["topic"]

    if topic == "stack":
        return jsonify({
            "title": "Stack",
            "definition": "A data structure where the last item added is the first one removed. (LIFO)",
            "analogy": "A stack of books, all placed one above the other. You first remove the last book you placed",
            "operations": ["push", "pop"],
            "data": stack
        })
