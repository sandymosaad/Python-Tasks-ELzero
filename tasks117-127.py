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
conn.commit()
conn.close()
