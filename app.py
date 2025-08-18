from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store for tasks
tasks = [
    {"id": 1, "title": "Learn Docker", "done": False},
    {"id": 2, "title": "Build CI/CD Pipeline", "done": False}
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Flask TODO API 🚀"})

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["done"] = data.get("done", task["done"])
    return jsonify(task)

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": f"Task {task_id} deleted"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

