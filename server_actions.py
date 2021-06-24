from datetime import date
import sqlite3



def addpost(name,content,date1):
    con = sqlite3.connect("mydatabase.db")
    mycursor = con.cursor()
    mycursor.execute("INSERT INTO posts(name,content,post_date) VALUES (?,?,?);",(name ,content,date1))
    con.commit()
    con.close()

def getposts():
    con = sqlite3.connect("mydatabase.db")
    mycursor = con.cursor()
    mycursor.execute("select * from posts")
    posts =mycursor.fetchall()
    con.commit()
    con.close()
    return posts



