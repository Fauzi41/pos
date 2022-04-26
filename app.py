from flask import Flask, render_template, request, jsonify, redirect, url_for
import pymongo
import uuid
# from flask_mail import Mail, Message
# from handler import routes


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
client = pymongo.MongoClient('localhost', 27017)
db = client.flaskapp
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'email@xxxxxxx.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)

@app.route('/')
def index():
    return render_template('signup.html')
  
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/register', methods =['GET', 'POST'])
def register():
    user = {
      "id": uuid.uuid4().hex,
      "email": request.form.get('email'),
      "password": request.form.get('password'),
      "token":uuid.uuid4().hex,
      "verified":False
    }
    
    if db.shopper.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.shopper.insert_one(user):
      # email = request.form.get('email')
      # subject = request.form.get('subject')
      # body_message = request.form.get('message')
      # print(email)
      # print(subject)
      # print(body_message)
      
      # msg = Message(subject=subject, sender = email, recipients = ['codionapp@gmail.com'])
      # msg.body = str(msg) + body_message
      # print(msg)
      # mail.send(msg)
      return redirect(url_for("profile"))

    return jsonify({ "error": "Signup failed" }), 400

@app.route('/verify/<token>')
def verify(token):
  if db.shopper.find_one({ "token": token }):
    myquery = { "verified":False }
    newvalues = { "$set": { "verified":True } }
    db.shopper.update_one(myquery, newvalues)
  print(token)
  return redirect(url_for("profile"))

if __name__ == "__main__":
    
    app.run(debug=True)