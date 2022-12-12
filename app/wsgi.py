from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Host name: {socket.gethostname()}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
