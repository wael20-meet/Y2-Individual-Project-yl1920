from flask import Flask, render_template,request

from databases import *
app = Flask(__name__)
 
@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/first_aid')
def Firstaid():
    return render_template('first_aid.html')

@app.route('/vet')
def Vet():
    return render_template('vet.html')

@app.route('/signup', methods=['GET' ,'POST'])
def Signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:    
        name = request.form['username']
        password = request.form['password']
        add(name, password)        

        return render_template("feedback.html")

@app.route('/feedback', methods=["GET","POST"])
def feedback():
    if request.method =="GET":
        return render_template('feedback.html')
    else:
        return render_template('index.html')

@app.route('/login' , methods=['GET' ,'POST'])
def Login():
    if request.method == 'GET':
        return render_template('login.html')
    else:    
        name = request.form['username']
        password = request.form['password']
        done = check(name,password)
        if done:
            return render_template("feedback.html")
        else:
            return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
