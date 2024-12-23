from flask import Flask, jsonify, request

app = Flask(__name__)

data = {
    "message": "Hello, World!",
    "status": "success"
}

@app.route('/')
def home():
    return jsonify(data)

@app.route('/echo', methods=['POST'])
def echo():
    content = request.json
    return jsonify(content)

if __name__ == '__main__':
    app.run(debug=True)
