# insecure_app.py
# Intentionally vulnerable example – this SHOULD fail SAST tools like HCL AppScan

import os
import sqlite3
import pickle


DB_PATH = "app.db"
SECRET_KEY = "hardcoded_super_secret_key_123"  # Hardcoded secret


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "username TEXT, "
        "password TEXT)"
    )
    conn.commit()
    conn.close()


def add_user(username, password):
    # ❌ SQL Injection vulnerability (string formatting)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    cur.execute(query)
    conn.commit()
    conn.close()


def get_user(username):
    # ❌ SQL Injection vulnerability
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cur.execute(query)
    result = cur.fetchone()
    conn.close()
    return result


def run_system_command(user_input):
    # ❌ Command Injection vulnerability
    os.system("echo " + user_input)


def unsafe_deserialize(data):
    # ❌ Insecure deserialization
    return pickle.loads(data)


if __name__ == "__main__":
    init_db()
    username = input("Enter username: ")
    password = input("Enter password: ")
    add_user(username, password)
    print(get_user(username))
    run_system_command(username)