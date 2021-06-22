import sqlite3



def addpost(name,content):
    con = sqlite3.connect("mydatabase.db")
    mycursor = con.cursor()
    mycursor.execute("INSERT INTO posts(name,content) VALUES (?,?);",(name ,content))
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



