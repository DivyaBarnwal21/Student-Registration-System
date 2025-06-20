import mysql.connector

db_config = {
    'host': '127.0.0.1',
    'user': 'root',     
    'password': 'Divya.21', 
    'database': 'student_results'
}

def get_connection():
    return mysql.connector.connect(**db_config)

def verify_login(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def add_student(student_id, name, email, address, mobile):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO students (student_id, name, email, address, mobile) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (student_id, name, email, address, mobile))
    conn.commit()
    conn.close()

def add_exam(exam_id, exam_name, subject,date):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO exams (exam_id, exam_name, subject, date) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (exam_id, exam_name, subject,date))
    conn.commit()
    conn.close()

def save_result(student_id, exam_id, marks):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO results (student_id, exam_id, marks) VALUES (%s, %s, %s)"
    cursor.execute(query, (student_id, exam_id, marks))
    conn.commit()
    conn.close()

def get_result(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT r.result_id, e.exam_name, e.subject, r.marks
        FROM results r
        JOIN exams e ON r.exam_id = e.exam_id
        WHERE r.student_id = %s
    """
    cursor.execute(query, (student_id,))
    results = cursor.fetchall()
    conn.close()
    return results