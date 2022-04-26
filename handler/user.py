from flask import Flask, render_template, request, jsonify
import pymongo
import uuid
from app import db

class User:

  def signup(self):
    user = {
      "_id": uuid.uuid4().hex,
      "email": request.form.get('email'),
      "password": request.form.get('password')
    }
    
    if db.shopper.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.shopper.insert_one(user):
      return render_template('profile.html')

    return jsonify({ "error": "Signup failed" }), 400
  