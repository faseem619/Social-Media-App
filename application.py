from server_actions import addpost
from flask import Flask,render_template,request,jsonify
from server_actions import addpost,getposts
from datetime import datetime
app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home', methods=['POST'])
def home():
    name =request.form.get('name')
    content =request.form.get('content')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
   
    addpost(name=name,content=content,date1=dt_string)
    posts =getposts()
    return render_template('home.html',posts=posts)

if __name__ =="__main__":
    app.run(debug=True)
