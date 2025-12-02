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
            "analogy": "A stack of books, all placed one above the other. You remove the last book you placed",
            "data": stack
        })
    if topic == "queue":
        return jsonify({
            "title": "Queue",
            "definition": "A data structure where the first item added is the first one removed. (FIFO)",
            "analogy": "A queue at a ticket counter — the first person in line is served first.",
            "data": queue
        })

@app.route("/push", methods=["POST"])
def push():
    value = request.json["value"]
    stack.append(value)
    return jsonify({"data": stack})

@app.route("/pop", methods=["POST"])
def pop():
    if stack:
        stack.pop()
    return jsonify({"data": stack})

@app.route("/enqueue", methods=["POST"])
def enqueue():
    value = request.json["value"]
    queue.append(value)
    return jsonify({"data": queue})

@app.route("/dequeue", methods=["POST"])
def dequeue():
    if queue:
        queue.pop(0)
    return jsonify({"data": queue})

if __name__ == "__main__":
    print("="*50)
    print("Server is starting...")
    print(f"Open http://127.0.0.1:5000 in your web browser.")
    print("="*50)
    app.run(debug=True)
