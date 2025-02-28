import uuid
import string
import time
from datetime import datetime

def generate_random_string():
	return str(uuid.uuid4())

random_string = generate_random_string()

def output_string_with_timestamp():
    while True:
        # get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # output the string with the timestamp
        print(f'{timestamp}: {random_string}')
        # wait for 5 seconds before outputting again
        time.sleep(5)

if __name__ == '__main__':
    print("Random string generator.")
    try:
        while True:
            output_string_with_timestamp()
    except KeyboardInterrupt:
        print("\nApplication stopped.")