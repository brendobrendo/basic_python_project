from flask_app import app
from flask_app.models.model_friend import Friend
from flask import render_template, request, redirect, session

@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends=friends)

@app.route('/create_friend', methods=['POST'])
def create_friend():
    print("Got post ")
    print(request.form)
    data = {**request.form}
    Friend.create_one(data)
    return redirect('/')