import uuid
import string
import time
from datetime import datetime
from flask import Flask

app = Flask(__name__)

def uuid_gen():
    return str(uuid.uuid4())

def timestamp_gen():
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_timestamp

uuid_string = uuid_gen()

@app.route('/')
def status():
    timestamp = timestamp_gen()
    return f'<p>{timestamp}</p><p>{uuid_string}</p>'

if __name__ == '__main__':
    print("Random UUID string generator.")
    app.run('0.0.0.0', 5000)