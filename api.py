from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello admin '


# @app.route('/myapi', methods = ['GET', 'POST'])
# def home():
#     if(request.method == 'GET'):
  
#         data = "hello world"
#         return jsonify({'data': data})


if __name__ == "__main__":
    app.run(port=8000,debug=True)