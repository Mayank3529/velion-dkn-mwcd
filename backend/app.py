from flask import send_from_directory
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


DB_NAME = "database.db"

# ---------------------------
# Database Setup
# ---------------------------
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_account (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            token TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS knowledge_item (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            content_type TEXT,
            created_date TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            user_email TEXT,
            timestamp TEXT
        )
    """)

    # Seed user (only once)
    cur.execute("SELECT * FROM user_account")
    if not cur.fetchall():
        cur.execute("""
            INSERT INTO user_account (name, email, token)
            VALUES ('Alice Consultant', 'alice@velion.com', 'token123')
        """)

    conn.commit()
    conn.close()

# ---------------------------
# Authentication
# ---------------------------
def authenticate():
    token = request.headers.get("X-USER-TOKEN")
    if not token:
        return None

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_account WHERE token=?", (token,))
    user = cur.fetchone()
    conn.close()
    return user

# ---------------------------
# Audit Logging
# ---------------------------
def log_action(action, email):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO audit_log (action, user_email, timestamp)
        VALUES (?, ?, ?)
    """, (action, email, datetime.now()))
    conn.commit()
    conn.close()

# ---------------------------
# REST API
# ---------------------------
@app.route("/api/knowledge", methods=["POST"])
def upload_knowledge():
    user = authenticate()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO knowledge_item (title, description, content_type, created_date)
        VALUES (?, ?, ?, ?)
    """, (
        data["title"],
        data["description"],
        data["contentType"],
        datetime.now()
    ))

    conn.commit()
    conn.close()

    log_action("UPLOAD_KNOWLEDGE", user["email"])

    return jsonify({"message": "Knowledge uploaded successfully"})

@app.route("/api/knowledge", methods=["GET"])
def list_knowledge():
    user = authenticate()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    query = request.args.get("q", "")

    conn = get_db()
    cur = conn.cursor()

    if query:
        cur.execute("""
            SELECT * FROM knowledge_item
            WHERE title LIKE ?
        """, ('%' + query + '%',))
    else:
        cur.execute("SELECT * FROM knowledge_item")

    rows = cur.fetchall()
    conn.close()

    log_action("VIEW_KNOWLEDGE", user["email"])

    return jsonify([dict(row) for row in rows])

@app.route("/")
def index():
    return send_from_directory("../frontend", "index.html")

@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory("../frontend", filename)

# ---------------------------
# Run App
# ---------------------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
