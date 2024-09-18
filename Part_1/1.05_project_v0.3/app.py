from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='./')

@app.route('/')
def message():
    return render_template('./index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f'Server has started on port {port}...')
    app.run(host='0.0.0.0', port=port)