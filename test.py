from flask_pymongo import pymongo
from flask import Flask,jsonify, request, Response
import json
from bson.objectid import ObjectId
app = Flask(__name__)



url = "mongodb+srv://ajayvishnu:ajay2001@cluster0.sbfjv.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(url)

db=client.get_database('api')
user_collection = pymongo.collection.Collection(db, 'test')
mydb = client['api']
mycol = mydb['test']

@app.route('/')
def hm():
    return "Welcome to HomePage"

@app.route('/get', methods=['GET'])
def gsts():
    return "Get Method"

@app.route('/post',methods=['POST'])
def reg():
    req_body = request.json
    user_collection.insert_one(req_body)
    resp = "Success"
    return resp
@app.route('/del/<name>',methods=['DELETE'])
def dele(name):
    user_collection.delete_one({"name":(name)})
    return "del succes"

if __name__ == "__main__":
    app.run(debug=True)



