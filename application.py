
from flask import Flask,render_template,request,jsonify
from server_actions import addpost,getposts,updateLikes,getprofile,getposts_inorder,getprofile_inorder
from datetime import datetime
app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home', methods=['GET','POST'])
def home():
    if request.method== 'GET':
        posts =getposts()
        return render_template('home.html',posts=posts)

    name =request.form.get('name')

    content =request.form.get('content')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if(content):
        addpost(name=name,content=content,date1=dt_string)
   
    posts =getposts()
    return render_template('home.html',posts=posts,name=name)

@app.route('/likes',methods=['POST'])
def likes():
    resp = request.get_json()
    num=resp['num']
    id= resp['id']
    print(num)
    print(id)
    updateLikes(num,id)
    return 'Got it'

@app.route('/home/profiles/<variable>')
def individual(variable):
    
    posts = getprofile(variable)
    return render_template('profile.html',name=variable,posts= posts)

@app.route('/home/order',methods=['GET'])
def ordered():
    arrange_type = request.args.get('type')
    posts =getposts_inorder(arrange_type)
    return render_template('home.html',posts=posts)

@app.route('/home/profiles/<variable>/order')
def profile_ordered(variable):
    print(variable)
    arrange_type = request.args.get('type')
    posts = getprofile_inorder(type=arrange_type, name=variable)
    return render_template('profile.html',name=variable,posts= posts)


if __name__ =="__main__":
    app.run(debug=True)