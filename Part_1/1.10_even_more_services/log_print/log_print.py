import hashlib
import sys
from flask import Flask

app = Flask(__name__)

def hash_gen(timestamp_path):
    timestamp = ''
    hash_hex = ''
    try:
        with open(timestamp_path, 'r') as f:
            timestamp = f.read()
            if timestamp:
                hash_object = hashlib.sha256(timestamp.encode()) # sha256 outputs a binary string
                hash_hex = hash_object.hexdigest() # this translates the hash into hexadecimal
                return timestamp, hash_hex
            else:
                return 'Error: No timestamp data is found.', ''
    except FileNotFoundError:
        return 'Error: No timestamp file is found.', ''

@app.route('/')
def log_print():
    if len(sys.argv) > 1:
        timestamp_path = sys.argv[1]
    else:
        return 'Usage: log_print timestamp_file'
    timestamp, file_hash = hash_gen(timestamp_path)
    return f'<p>Timestamp:\n{timestamp}</p><p>Timestamp file hash: {file_hash}</p>'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)