import sqlite3


con = sqlite3.connect('mydatabase.db')
mycursor = con.cursor()
mycursor.execute("CREATE TABLE posts(id INTEGER PRIMARY KEY autoincrement, name text NOT NULL,content text NOT NULL);")
con.commit()
con.close()