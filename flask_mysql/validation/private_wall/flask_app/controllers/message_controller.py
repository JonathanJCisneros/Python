from flask import session, redirect, request
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.message_model import Message

@app.route('/post_message',methods=['POST'])
def post_message():

    data = {
        "sender_id":  request.form['sender_id'],
        "receiver_id" : request.form['receiver_id'],
        "content": request.form['content']
    }
    Message.save(data)
    return redirect('/dashboard')

@app.route('/destroy/message/<int:id>')
def destroy_message(id):
    data = {
        "id": id
    }
    Message.destroy(data)
    return redirect('/dashboard')