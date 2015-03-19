from flask import Flask, request, send_from_directory
import os

# document base path
SERVER_BASE_PATH = os.path.dirname(os.path.realpath(__file__))

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path=SERVER_BASE_PATH)

@app.route('/')
def send_index():
    return send_from_directory('app', 'index.html')


@app.route('/<path:filename>')
def send_page(filename):
    return send_from_directory('app', filename)

if __name__ == "__main__":
    app.run(debug={{DEBUG}}, host="{{SERVER_HOST}}", port=12200)