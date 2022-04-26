from flask import Flask
from app import app
from handler.user import User

@app.route('/register', methods =['GET', 'POST'])
def register():
    return User().signup()