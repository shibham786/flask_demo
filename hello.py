from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/user/<name>")
def hello(name):
    if name == 'admin':

        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('welcome_user',name=name))

@app.route("/admin")
def hello_admin():
    return 'Hello admin '

@app.route("/<int:id>")
def Id(id):
    return 'Hello %d'% id

@app.route("/<name>")
def welcome_user(name):
    return 'Hello %s' %name

if __name__ == '__main__':
    app.run(debug=True)