from flask import Flask, render_template, request, jsonify, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "firstflaskapp"  

def get_db():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tasks")
def tasks_page():
    if "user" not in session:
        return redirect("/")

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    all_tasks = cur.fetchall()
    conn.close()

    return render_template("tasks.html", tasks=all_tasks)


@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data.get("title", "").strip()

    if title == "":
        return jsonify({"error": "Empty task not allowed"}), 400

    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title, status) VALUES (?, 'Pending')", (title,))
    conn.commit()

    return jsonify({"title": title, "status": "Pending"})


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "1234":
        session["user"] = username
        return redirect("/tasks")
    else:
        return "Invalid Login"


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")
