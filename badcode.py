import os
import sqlite3
import hashlib
import pickle
import subprocess
import tempfile


API_KEY = "12345-SECRET-KEY"


def insecure_login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()
    return result


def weak_hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def run_system_command(user_input):
    command = f"echo {user_input}"
    return subprocess.call(command, shell=True)


def unsafe_deserialization(serialized_data):
    return pickle.loads(serialized_data)


def insecure_temp_file():
    filename = tempfile.mktemp()
    with open(filename, "w") as f:
        f.write("temporary sensitive data")
    return filename


def dangerous_eval(expression):
    return eval(expression)


def check_admin(is_admin):
    assert is_admin == True
    return "Access granted"


if __name__ == "__main__":
    print("Weak hash:", weak_hash_password("mypassword"))
    print("Eval result:", dangerous_eval("2 + 2"))