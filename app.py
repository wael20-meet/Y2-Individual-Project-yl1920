from flask import Flask, render_template,request
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
        return render_template("feedback.html")

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/login' , methods=['GET' ,'POST'])
def Login():
    if request.method == 'GET':
        return render_template('login.html')
    else:    
        msg = Message('Hello', sender = 'yoyo20meet@gmail.com', recipients = ['ron12harel@gmail.com'])
        msg.body = request.form['message'] +"\n"+request.form["login.html"]
        mail.send(msg)
        return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
