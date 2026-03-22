import hashlib
import os
import json

user_file = "users.txt"
task_folder = "tasks"
if not os.path.exists(task_folder):
    os.makedirs(task_folder)

current_user = None

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    users = {}
    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            for line in f:
                username, hashed = line.strip().split(":")
                users[username] = hashed
    return users

def save_user(username, hashed_password):
    with open(user_file, "a") as f:
        f.write(f"{username}:{hashed_password}\n")

def register():
    users = load_users()
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter new password: ")
    hashed = hash_password(password)
    save_user(username, hashed)
    print("Registration successful.")

def login():
    global current_user
    users = load_users()
    username = input("Username: ")
    password = input("Password: ")
    hashed = hash_password(password)
    if users.get(username) == hashed:
        current_user = username
        print("Login successful.")
    else:
        print("Invalid credentials.")

def get_tasks_file():
    return os.path.join(task_folder, f"{current_user}_tasks.json")

def load_tasks():
    tasks_file = get_tasks_file()
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    tasks_file = get_tasks_file()
    with open(tasks_file, "w") as f:
        json.dump(tasks, f)

def add_task():
    tasks = load_tasks()
    desc = input("Task description: ")
    task_id = 1 + max([t["id"] for t in tasks], default=0)
    task = {"id": task_id, "desc": desc, "status": "Pending"}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added with ID {task_id}.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    for t in tasks:
        print(f"ID: {t['id']} | {t['desc']} | {t['status']}")

def mark_completed():
    tasks = load_tasks()
    tid = int(input("Enter task ID to mark as completed: "))
    for t in tasks:
        if t["id"] == tid:
            t["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed.")
            return
    print("Task ID not found.")

def delete_task():
    tasks = load_tasks()
    tid = int(input("Enter task ID to delete: "))
    new_tasks = [t for t in tasks if t["id"] != tid]
    if len(new_tasks) == len(tasks):
        print("Task ID not found.")
    else:
        save_tasks(new_tasks)
        print("Task deleted.")

def logout():
    global current_user
    print(f"User '{current_user}' logged out.")
    current_user = None

if __name__ == "__main__":
    while True:
        print("\n--- Task Manager ---")
        if not current_user:
            print("1. Register 2. Login 3. Exit")
            c = input("Choice: ")
            if c == "1":
                register()
            elif c == "2":
                login()
            elif c == "3":
                break
            else:
                print("Invalid choice.")
        else:
            print("1. Add Task 2. View Tasks 3. Mark Completed 4. Delete Task 5. Logout 6. Exit")
            c = input("Choice: ")
            if c == "1":
                add_task()
            elif c == "2":
                view_tasks()
            elif c == "3":
                mark_completed()
            elif c == "4":
                delete_task()
            elif c == "5":
                logout()
            elif c == "6":
                break
            else:
                print("Invalid choice.")