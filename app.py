from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

stack = []
queue = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lesson", methods=["POST"])
def lesson():
    topic = request.json["topic"]

    if topic == "stack":
        return jsonify({
            "title": "Stack",
            "definition": "A data structure where the last item added is the first one removed. (LIFO)",
            "analogy": "A stack of books, all placed one above the other. You first remove the last book you placed",
            "operations": ["push", "pop"],
            "data": stack
        })
    if topic == "queue":
        return jsonify({
            "title": "Queue",
            "definition": "A Queue is a data structure where the first item added is the first one removed. (FIFO)",
            "analogy": "A queue at a ticket counter — the first person in line is served first.",
            "operations": ["enqueue", "dequeue"],
            "data": queue
        })
