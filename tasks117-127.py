'''
problem 01:
Write at least 5 different data types that can be used in a database (Database Data Types).
'''
# Your Answer Here
'''
1. INT          → Used to store integer numbers (e.g., 10, 200, -5)
2. VARCHAR      → Used to store text with a limited length (e.g., "Sandy")
3. TEXT         → Used to store long text (e.g., a description or article)
4. DATE         → Used to store dates (e.g., 2025-10-05)
5. BOOLEAN      → Used to store logical values (True / False)
'''
#----------------------- Task 01 Done ----------------------------------
#-----------------------------------------------------------------------
'''
problem 02:
Create a directory named Python.

Inside that directory, create a file named index.py.

In the same directory, create a database named elzero.db using SQLite.

Inside the database, create a table named users that contains the following fields:

id → integer, auto-increment, primary key, and not null

name → text, unique, and not null

email → text, unique, and not null

birthdate → date, not null

Make sure the table is only created if it doesn’t already exist.

All fields must be unique, meaning duplicate data cannot be inserted.
'''
import os
import sqlite3

# Get current directory
current_dir = os.getcwd()

# Create folder "ELzero"
folder = os.path.join(current_dir, 'ELzero')
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder created")

# Create file "index.py" inside the folder
file_path = os.path.join(folder, 'index.py')
if not os.path.exists(file_path):
    open(file_path, 'a').close()  
    print('File created')

# Create database "elzero.db" inside the folder
db_path = os.path.join(folder, "elzero.db")
conn = sqlite3.connect(db_path)
print('Database created')

# Create a cursor
cur = conn.cursor()

# Create table if not exists
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        birthdate DATE NOT NULL
    )
''')
print('Table created')

# Commit changes and close connection
# conn.commit()
# conn.close()

#-----------------------------Task 02 Done ------------------------
#------------------------------------------------------------------
'''
problem 03:
Continue from the previous assignment where you created the Python folder on the Desktop and the SQLite database elzero.db with a users table.
Write a Python script that:
Connects to the existing SQLite database elzero.db in the Python folder on the Desktop.
Inserts any random data (5 different records) for 5 users into the users table.
Each user record must include: name, email, and birthdate (use appropriate data formats).
Ensures that the script is safe to run multiple times:
Because the name and email columns are declared UNIQUE, running the script again will normally raise sqlite3.IntegrityError for duplicates.
Your script must ignore these duplicate-entry errors so that repeated runs do not stop the program or show an unhandled exception.
You may use one of these approaches (choice is up to you):
Use a parameterized query with error handling (try/except) and skip duplicates, or
Use an SQL statement that ignores duplicates (e.g., INSERT OR IGNORE or ON CONFLICT), or
Check existence first then insert.
Commit the transaction and close the database connection.
Optionally print a friendly message showing which users were inserted and which were skipped due to uniqueness (or simply print a final success message).
'''
# Insert 5 users
users = [
    ('Sandy', 'sandy@gmail.com', '2001-04-22'),
    ('Mina', 'mina@gmail.com', '1999-08-10'),
    ('John', 'john@example.com', '1995-12-05'),
    ('Lina', 'lina@yahoo.com', '2003-03-17'),
    ('Mark', 'mark@hotmail.com', '2000-06-09')
]

for user in users:
    try:
        cur.execute('INSERT INTO users (name, email, birthdate) VALUES (?,?,?)', user)
        print(f'User {user[0]} added')
    except sqlite3.IntegrityError as e:
        print(f'Error adding user {user[0]}: {e}')

        
conn.commit()
conn.close()
#----------------------------- Task 03 Done ----------------------------
#-----------------------------------------------------------------------
