from server_actions import addpost
from flask import Flask,render_template,request
from server_actions import addpost,getposts
app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home', methods=['POST'])
def home():
    name =request.form.get('name')
    content =request.form.get('content')
    addpost(name=name,content=content)
    posts =getposts()
    return render_template('home.html',posts=posts)

if __name__ =="__main__":
    app.run(debug=True)
