import sqlite3

# Connect to SQLite (in-memory for demo; use a filename for persistence)
conn = sqlite3.connect("test.db")  # Change to ":memory:" for in-memory database
cursor = conn.cursor()

# --- Create Tables ---
cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
''')

cursor.execute('''
CREATE TABLE courses (
    course_id TEXT PRIMARY KEY,
    course_name TEXT NOT NULL,
    credit INTEGER
)
''')

cursor.execute('''
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id TEXT,
    semester TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
''')

# --- Insert Data ---
students = [
    ('Alice', 21, 'Computer Science'),
    ('Bob', 22, 'Information Technology'),
    ('Charlie', 23, 'Computer Science')
]
cursor.executemany("INSERT INTO students (name, age, department) VALUES (?, ?, ?)", students)

courses = [
    ('CSE101', 'Introduction to Programming', 3),
    ('CSE102', 'Database Systems', 4),
    ('CSE103', 'Operating Systems', 3)
]
cursor.executemany("INSERT INTO courses (course_id, course_name, credit) VALUES (?, ?, ?)", courses)

enrollments = [
    (1, 'CSE101', 'Spring 2025'),
    (2, 'CSE102', 'Spring 2025'),
    (3, 'CSE103', 'Spring 2025'),
    (1, 'CSE102', 'Spring 2025')
]
cursor.executemany("INSERT INTO enrollments (student_id, course_id, semester) VALUES (?, ?, ?)", enrollments)

conn.commit()

# --- Example Queries ---

print("All Students:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

print("\nComputer Science Students:")
for row in cursor.execute("SELECT name FROM students WHERE department = 'Computer Science'"):
    print(row)

print("\nCourses with more than 3 credits:")
for row in cursor.execute("SELECT * FROM courses WHERE credit > 3"):
    print(row)

print("\nStudent Enrollments with Course Names:")
query = '''
SELECT s.name, c.course_name, e.semester
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.course_id
'''
for row in cursor.execute(query):
    print(row)

print("\nNumber of Students per Department:")
for row in cursor.execute("SELECT department, COUNT(*) FROM students GROUP BY department"):
    print(row)

print("\nEnrollment Count per Course:")
for row in cursor.execute("SELECT course_id, COUNT(*) FROM enrollments GROUP BY course_id"):
    print(row)

# Close the connection
conn.close()
