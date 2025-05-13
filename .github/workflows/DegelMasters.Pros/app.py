from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')
CORS(app)

posts = []  # כאן נשמרים הפוסטים בזיכרון (אפשר גם לעשות עם קובץ בעתיד)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/posts', methods=['POST'])
def add_post():
    data = request.json
    if not data:
        return jsonify({'error': 'Missing data'}), 400

    post = {
        "text": data.get('text', ''),
        "image": data.get('image', '')
    }

    posts.insert(0, post)  # מוסיף את הפוסט הראשון למעלה
    return jsonify({'message': 'Post added'}), 200

@app.route('/posts/<int:index>', methods=['DELETE'])
def delete_post(index):
    if 0 <= index < len(posts):
        posts.pop(index)
        return jsonify({'message': 'Post deleted'}), 200
    return jsonify({'error': 'Invalid index'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
