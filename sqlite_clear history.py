import sqlite3


con = sqlite3.connect('mydatabase.db')
mycursor = con.cursor()
mycursor.execute("DELETE FROM posts;")
con.commit()
con.close()