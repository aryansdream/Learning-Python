# =========================================
# 📂 ADVANCED FILE HANDLING IN PYTHON
# =========================================

import json
import os


# =========================================
# 1. SAFE FILE READ
# =========================================
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "❌ File not found"
    except Exception as e:
        return f"Error: {e}"


# =========================================
# 2. SAFE FILE WRITE (OVERWRITE)
# =========================================
def write_file(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
        return "✅ File written successfully"
    except Exception as e:
        return f"Error: {e}"


# =========================================
# 3. SAFE FILE APPEND
# =========================================
def append_file(filename, content):
    try:
        with open(filename, "a") as file:
            file.write(content + "\n")
        return "✅ Data appended"
    except Exception as e:
        return f"Error: {e}"


# =========================================
# 4. READ FILE LINE BY LINE
# =========================================
def read_lines(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except:
        return []


# =========================================
# 5. COUNT LINES / WORDS / CHARACTERS
# =========================================
def file_stats(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            lines = content.split("\n")
            words = content.split()
            chars = len(content)

            return {
                "lines": len(lines),
                "words": len(words),
                "characters": chars
            }
    except:
        return {}


# =========================================
# 6. CHECK FILE EXISTS
# =========================================
def file_exists(filename):
    return os.path.exists(filename)


# =========================================
# 7. DELETE FILE
# =========================================
def delete_file(filename):
    if file_exists(filename):
        os.remove(filename)
        return "🗑️ File deleted"
    return "File does not exist"


# =========================================
# 8. JSON HANDLING (IMPORTANT)
# =========================================

def save_json(filename, data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        return "✅ JSON saved"
    except Exception as e:
        return f"Error: {e}"


def load_json(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except:
        return []


# =========================================
# 9. MINI PROJECT: USER MANAGEMENT SYSTEM
# =========================================

DATA_FILE = "users.json"


def add_user(name, age):
    users = load_json(DATA_FILE)
    users.append({"name": name, "age": age})
    save_json(DATA_FILE, users)
    print("✅ User added")


def view_users():
    users = load_json(DATA_FILE)
    if not users:
        print("No users found")
        return

    for i, user in enumerate(users, start=1):
        print(f"{i}. {user['name']} - {user['age']}")


def search_user(name):
    users = load_json(DATA_FILE)
    for user in users:
        if user["name"].lower() == name.lower():
            return user
    return "User not found"


# =========================================
# 10. TEST AREA (RUN THIS)
# =========================================

if __name__ == "__main__":

    # Basic file operations
    print(write_file("sample.txt", "Hello World"))
    print(append_file("sample.txt", "New line added"))
    print(read_file("sample.txt"))

    # File stats
    print(file_stats("sample.txt"))

    # JSON + Mini Project
    add_user("Aryan", 20)
    add_user("Rahul", 22)

    view_users()

    print(search_user("Aryan"))