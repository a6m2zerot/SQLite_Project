import sqlite3

conn = sqlite3.connect("MyBooks.db")
cursor = conn.cursor()

cursor.execute("""                                                    
                  CREATE TABLE IF NOT EXISTS MyBooks(                               
                  books_id INTEGER PRIMARY KEY AUTOINCREMENT,                     
                  title VARCHAR(20),                                              
                  author VARCHAR(30),                                             
                  price DECIMAL(8,2),                                                      
                  amount INT);                                                                 
                """)
conn.commit()

cursor.execute("""SELECT * FROM MyBooks;""")
for elem in cursor.fetchall():
    print(elem)

