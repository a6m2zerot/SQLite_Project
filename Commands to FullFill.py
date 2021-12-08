import sqlite3
conn = sqlite3.connect("MyBooks.db")
cursor = conn.cursor()


cursor.execute("""                                  
                INSERT INTO MyBooks(title, author, price, amount)  
                VALUES('Мастер и Маргарита', 'Булгаков М.А.', 100.90, 10);
               """)
conn.commit()

book = ('Белая Гвардия', 'Булгаков М. А.', 540.50,  5)

cursor.execute("""INSERT INTO MyBooks(title, author, price, amount)
                VALUES(?, ?, ?, ?)""", book)
conn.commit()

more_books = [('Идиот', 'Достоевский', 400.90, 120), ('Лирика', 'Гумилев', 1050.90, 107)]

cursor.executemany("""INSERT INTO MyBooks(title, author, price, amount)
                    VALUES(?, ?, ?, ?)""", more_books)
conn.commit()

#  Delete all from MyBooks
#  cursor.execute("""DELETE FROM MyBooks
                  #  WHERE title LIKE "%_"; """)
#  conn.commit()
