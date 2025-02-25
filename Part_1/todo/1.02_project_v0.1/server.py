from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hey? Is there anyone alive?'

if __name__ == '__main__':
    port = os.getenv('PORT', 5000)
    print(f'Server started in port {port}')
    app.run('0.0.0.0', port)


