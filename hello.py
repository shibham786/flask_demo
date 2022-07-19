from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return 'Hello world'

@app.route("/<name>")
def hello_name(name):
    return 'Hello %s'% name

@app.route("/<int:id>")
def Id(id):
    return 'Hello %d'% id

@app.route("/<float:revNo>")
def Revision(revNo):
    return 'Hello %f' %revNo

if __name__ == '__main__':
    app.run(debug=True)