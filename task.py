



import sqlite3

def create_tables():
    conn = sqlite3.connect("plan.db")
    curr = conn.cursor()

    # Users jadvali
    curr.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER  UNIQUE,
            username TEXT
        )
    """)
# created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    # Tasks jadvali
    curr.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            description TEXT,
            day TEXT,
            time TEXT NOT NULL,
            status TEXT CHECK(status IN ('pending', 'done')) DEFAULT 'pending'
        )
    """)

    conn.commit()
    conn.close()


def insert_table(user_id,description,day,time,status="pending"):
    conn = sqlite3.connect("plan.db")
    curr = conn.cursor()
    query = "INSERT INTO tasks(user_id,description,day,time,status) VALUES (?,?,?,?,?)"
    curr.execute(query,(user_id,description,day,time,status))
    task_id = curr.lastrowid
    conn.commit()
    conn.close()
    return task_id



def insert_user(user_id, username):
    conn = sqlite3.connect("plan.db")
    curr = conn.cursor()
    query = "INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)"
    curr.execute(query, (user_id, username))
    conn.commit()
    conn.close()


def select_task(user_id,status):
    conn = sqlite3.connect("plan.db")
    curr = conn.cursor()
    query = "SELECT * FROM tasks WHERE user_id = ? AND status = ?"
    curr.execute(query, (user_id,status))
    rows = curr.fetchall()
    conn.close()
    return rows

def update_task(task_id,status):
    conn = sqlite3.connect("plan.db")
    curr = conn.cursor()
    query = "UPDATE tasks SET status = ? WHERE id = ?"
    curr.execute(query,(status,task_id))
    conn.commit()
    conn.close()