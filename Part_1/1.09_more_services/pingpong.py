from flask import Flask

app = Flask(__name__)

@app.route('/pingpong')
def pong():
    global ping
    response = ping
    ping += 1
    return f'<p>pong {response}</p>'

if __name__ == '__main__':
    ping = 0
    app.run('0.0.0.0', 5000)