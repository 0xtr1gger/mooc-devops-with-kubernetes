import uuid
import string
import time
from datetime import datetime

def uuid_gen():
    return str(uuid.uuid4())

def timestamp_gen():
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_timestamp

if __name__ == '__main__':
    print("Random UUID string generator.")
    uuid_string = uuid_gen()
    timestamp = timestamp_gen()
    sleep_seconds = 5
    try:
        while True:
            print(f'{timestamp}: {uuid_string}')
            time.sleep(sleep_seconds)
    except KeyboardInterrupt:
        print("\nApplication stopped.")
