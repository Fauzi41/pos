from flask import Flask, render_template, request, jsonify
import pymongo
import uuid
# from handler import routes


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
client = pymongo.MongoClient('localhost', 27017)
db = client.flaskapp

@app.route('/')
def index():
    return render_template('signup.html')


@app.route('/register', methods =['GET', 'POST'])
def register():
    user = {
      "_id": uuid.uuid4().hex,
      "email": request.form.get('email'),
      "password": request.form.get('password')
    }
    
    if db.shopper.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.shopper.insert_one(user):
      return render_template('signup.html')

    return jsonify({ "error": "Signup failed" }), 400

if __name__ == "__main__":
    
    app.run(debug=True)