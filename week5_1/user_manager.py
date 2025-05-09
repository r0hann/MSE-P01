from database import create_connection
import sqlite3

def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("��️ User deleted.")

def advanced_search(user_id=None, name=None):
    conn = create_connection()
    cursor = conn.cursor()
    
    if user_id is not None and name:
        cursor.execute("SELECT * FROM users WHERE id = ? AND name LIKE ?", (user_id, '%' + name + '%'))
    elif user_id is not None:
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    elif name:
        cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    else:
        return []
        
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_course(name, unit):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO courses (name, unit) VALUES (?, ?)", (name, unit))
        conn.commit()
        print("Course added successfully.")
    except sqlite3.IntegrityError:
        print("Error adding course.")
    conn.close()

def search_course_by_id_and_user(course_id, user_name):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT c.course_id, c.name, c.unit, u.name as user_name
        FROM courses c
        JOIN user_courses uc ON c.course_id = uc.course_id
        JOIN users u ON uc.user_id = u.id
        WHERE c.course_id = ? AND u.name LIKE ?
    """, (course_id, '%' + user_name + '%'))
    
    rows = cursor.fetchall()
    conn.close()
    return rows

def enroll_user_in_course(user_id, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO user_courses (user_id, course_id) VALUES (?, ?)", (user_id, course_id))
        conn.commit()
        print("User enrolled in course successfully.")
    except sqlite3.IntegrityError:
        print("User is already enrolled in this course or invalid user/course ID.")
    conn.close()
