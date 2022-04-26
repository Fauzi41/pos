from flask import Flask, jsonify, request, session, redirect
from app import db
import uuid

class User:

  def signup(self):
    print(request.form)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "password": request.form.get('password')
    }

    # Check for existing email address
    if db.shopper.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.shopper.insert_one(user):
      return self.start_session(user)

    return jsonify({ "error": "Signup failed" }), 400
