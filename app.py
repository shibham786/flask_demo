
from flask_restful import abort
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify,request
from flask_cors import cross_origin

app = Flask(__name__)

DB_URL = 'postgresql://postgres:123456@localhost/mydb'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True, nullable=False)
  content = db.Column(db.String(120), unique=True, nullable=False)

  def __init__(self, title, content):
    self.title = title
    self.content = content

@cross_origin()
@app.route("/")
def welcome():
    return jsonify({'message':'hello admin'})

@cross_origin()
@app.route("/item",methods=['POST'])
def additem():
    item_data = request.json
    title = item_data['title']
    content = item_data['content']

    item = Item(title=title,content=content)
    db.session.add(item)
    db.session.commit()
    return jsonify({"success": True,"response":"item added"})

@cross_origin()
@app.route("/getitem",methods=['GET'])
def getitem():
    all_items = []
    items = Item.query.all()
    for item in items:
        result={
            "id":item.id,
            "title":item.title,
            "content":item.content,
        }
        all_items.append(result)

    return jsonify({
        "success":True,
        "items":all_items,
    }) 


@cross_origin()
@app.route("/updateitem/<int:id>",methods=['PATCH'])
def updateitem(id):
    item = Item.query.get(id)
    
    if item is None:
        abort(404)
    else:

        item.title = request.json['title']
        db.session.add(item)
        db.session.commit()
        return jsonify({
            "Success":True,
            "Item":"Item Detail Updated",
        })


@cross_origin()
@app.route("/deleteitem/<int:id>",methods=['DELETE'])
def deleteitem(id):
    item = Item.query.get(id)
    if item is None:
        abort(404)
    else:
        db.session.delete(item)
        db.session.commit()
        return jsonify({
            "Success":True,
            "message":"Item Deleted success"
        })

if __name__ == '__main__':
  app.run(debug=True)