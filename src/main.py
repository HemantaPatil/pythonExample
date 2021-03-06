from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room
import socketio
app = Flask(__name__)
app.secret_key = "sfdjkafnk"
socketio = SocketIO(app)

@app.route('/home')
def home():
    return render_template("index.html")

@app.route("/")
def index():
    return("Chimmu welcome to my 1st Python web application, deployed on Heroku Cloud Platform")
    
@app.route('/chat')
def chat():
    username = request.args.get("username")
    room = request.args.get("room")

    if username and room:
        return render_template('chat.html', username=username, room=room)
    else:
        return redirect(url_for('home'))

@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info("{} has jooined the room".format(data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data)

@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} {}".format(data['username'], data['message']))
    socketio.emit('receive_message', data, room=data['room'])


if __name__ == '__main__':
    socketio.run(app, debug=True)