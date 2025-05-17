from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow WebSocket connections

# Serve the HTML page
@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_message(msg):
    print(f"Received: {msg}")
    socketio.send(msg)  # Broadcast the message

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
