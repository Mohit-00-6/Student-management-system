import sqlite3

# Connect to SQLite
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        roll INTEGER NOT NULL UNIQUE,
        course TEXT,
        marks INTEGER
    )
''')
conn.commit()

# Add student
def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    marks = input("Enter marks: ")
    try:
        cursor.execute("INSERT INTO students (name, roll, course, marks) VALUES (?, ?, ?, ?)",
                       (name, roll, course, marks))
        conn.commit()
        print("✅ Student added successfully.")
    except sqlite3.IntegrityError:
        print("❌ Roll number must be unique.")

# View all students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- All Students ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Roll: {row[2]}, Course: {row[3]}, Marks: {row[4]}")
    print("---------------------")

# Search student by name
def search_student():
    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    if rows:
        print("\n--- Search Results ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Roll: {row[2]}, Course: {row[3]}, Marks: {row[4]}")
    else:
        print("❌ No student found.")

# Update student
def update_student():
    roll = input("Enter roll number to update: ")
    cursor.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    row = cursor.fetchone()
    if row:
        name = input("New name: ")
        course = input("New course: ")
        marks = input("New marks: ")
        cursor.execute("UPDATE students SET name=?, course=?, marks=? WHERE roll=?",
                       (name, course, marks, roll))
        conn.commit()
        print("✅ Student record updated.")
    else:
        print("❌ Student not found.")

# Delete student
def delete_student():
    roll = input("Enter roll number to delete: ")
    cursor.execute("DELETE FROM students WHERE roll = ?", (roll,))
    conn.commit()
    print("✅ Student record deleted.")

# Main menu
def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            break
        else:
            print("❌ Invalid choice. Try again.")

    conn.close()

if __name__ == "__main__":
    main()