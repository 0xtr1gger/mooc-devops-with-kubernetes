from flask import Flask, render_template
import os
import requests
import datetime
import time

IMAGE_DIR = './static'
IMAGE_PATH = os.path.join(IMAGE_DIR, 'cached_image.jpg')

app = Flask(__name__, template_folder='./')

if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

def fetch_image():
    response = requests.get('https://picsum.photos/1200')
    if response.status_code == 200:
        with open(IMAGE_PATH, 'wb') as f:
            f.write(response.content)
        image_time = time.ctime(os.path.getmtime(IMAGE_PATH))
        print(f'New image fetched.\nFetch time: {image_time}')


def is_image_stale():
    # if there is no image saved, mark it stale and fetch one.
    if not os.path.exists(IMAGE_PATH):
        return True

    stale_time = 60 # 60 minutes
    current_time = datetime.datetime.now()
    image_file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(IMAGE_PATH))
    delta = current_time - image_file_mtime

    if delta.total_seconds() > 60 * stale_time:
        return True # the image is stale

    return False # if, after all checks, the function hasn't return , then the image is not considered stale

@app.route('/')
def index():
    if is_image_stale():
        print('the image is stale; fetching a new one!')
        fetch_image() # if the image is stale, we update
    print('the image is not stale yet; let it stay the same.')
    # if it isn't, the image in the storage stays the same.
    return render_template('./index.html', image_path=IMAGE_PATH)

if __name__ == '__main__':
    port = os.getenv('PORT', 5000)
    print(f'Server started in port {port}')
    fetch_image()
    app.run('0.0.0.0', port)