import sqlite3

# CRUD - Create, Read, Update, Delete

# Create

def create_comment(content, author):
    connection = sqlite3.connect("./comments.db")
    cursor = connection.cursor()

    cursor.execute(f"""
        INSERT INTO comments (content, author)
        VALUES ('{content}', '{author}');
    """)
    
    connection.commit()

# Read

def read_all():
    connection = sqlite3.connect("./comments.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM comments;
    """)
    
    return cursor.fetchall()

def read_one(id):
    connection = sqlite3.connect("./comments.db")
    cursor = connection.cursor()
    
    cursor.execute(f"""
        SELECT * FROM comments WHERE id = {id};
    """)
    
    return cursor.fetchone()

# Update

def update_comment(id, content, author):
    connection = sqlite3.connect("./comments.db")
    cursor = connection.cursor()
    
    cursor.execute(f"""
        UPDATE comments 
        SET content = '{content}', author = '{author}'
        WHERE id = {id};
    """)
    
    connection.commit()
    
# Delete
    
def delete_comment(id):
    connection = sqlite3.connect("./comments.db")
    cursor = connection.cursor()
    
    cursor.execute(f"""
        DELETE FROM comments
        WHERE id = {id};
    """)
    
    connection.commit()

def init():
    connection = sqlite3.connect("./comments.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY,
            content TEXT NOT NULL,
            author TEXT NOT NULL
        );
    """)
