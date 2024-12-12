import sqlite3

# Path to your database file
DATABASE = 'db.db'

# Path to your schema file
SCHEMA = 'schema.sql'

def init_db():
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect(DATABASE)
    with open(SCHEMA, 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database initialized with schema.")

if __name__ == '__main__':
    init_db()
