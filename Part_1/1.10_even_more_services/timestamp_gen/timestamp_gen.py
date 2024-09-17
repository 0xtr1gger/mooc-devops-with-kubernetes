import time
import sys
from datetime import datetime

def timestamp_gen():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        timestamp_path = sys.argv[1]
    else:
        print('Usage: log_print timestamp_file')
        exit()
    sleep_seconds = 5
    try:
        while True:
            timestamp = timestamp_gen()
            with open(timestamp_path, 'w') as f: # 'w' mode truncates the file
                f.write(f'{timestamp}\n')
            print(f'Written timestamp: {timestamp}') # log for debugging
            time.sleep(sleep_seconds)
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f'Error: {e}')