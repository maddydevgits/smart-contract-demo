from flask import Flask,render_template

frontend=Flask(__name__)

@frontend.route('/')
def homePage():
    return render_template('index.html')

@frontend.route('/vote/<id>')
def castVote(id):
    id=int(id)
    if id==1:
        return render_template('index.html',result='You have polled for BJP Party')
    elif id==2:
        return render_template('index.html',result='You have polled for JSP Party')
    elif id==3:
        return render_template('index.html',result='You have polled for YSRCP Party')

if __name__=="__main__":
    frontend.run(host='0.0.0.0',debug=True,port=5001)