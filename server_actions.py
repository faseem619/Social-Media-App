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

def updateLikes(num,id):
    con = sqlite3.connect("mydatabase.db")
    mycursor = con.cursor()
    ## stuff goes here
    mycursor.execute("UPDATE posts SET likes= ? WHERE post_date= ?;",(num,id))
    con.commit()
    con.close()

def getprofile(name):
    con = sqlite3.connect("mydatabase.db")
    mycursor = con.cursor()
    ## stuff goes here
    mycursor.execute(" SELECT * FROM posts WHERE name = ?",(name,))
    posts =mycursor.fetchall()
    con.commit()
    con.close()
    return posts

def getposts_inorder(type):
    con = sqlite3.connect("mydatabase.db")
    mycursor = con.cursor()
    if type == 'New':
        mycursor.execute("select * from posts order by post_date desc")
        posts =mycursor.fetchall()
        con.commit()
        con.close()
        return posts
    if type == 'Old':
        mycursor.execute("select * from posts order by post_date asc")
        posts =mycursor.fetchall()
        con.commit()
        con.close()
        return posts
    if type == 'Popular':
        mycursor.execute("select * from posts order by likes desc")
        posts =mycursor.fetchall()
        con.commit()
        con.close()
        return posts
    

    

def getprofile_inorder(type,name):
    con = sqlite3.connect("mydatabase.db")
    mycursor = con.cursor()
    if type == 'New':
        mycursor.execute("select * from posts WHERE name = ?  order by post_date desc",(name,))
        posts =mycursor.fetchall()
        con.commit()
        con.close()
        return posts
    if type == 'Old':
        mycursor.execute("select * from posts WHERE name = ? order by post_date asc",(name,))
        posts =mycursor.fetchall()
        con.commit()
        con.close()
        return posts
    if type == 'Popular':
        mycursor.execute("select * from posts WHERE name = ? order by likes desc",(name,))
        posts =mycursor.fetchall()
        con.commit()
        con.close()
        return posts
    