import sqlite3


con = sqlite3.connect('mydatabase.db')
mycursor = con.cursor()
mycursor.execute("DROP TABLE posts;")
con.commit()
con.close()