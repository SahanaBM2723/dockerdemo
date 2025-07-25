
from flask import Flask, request, jsonify
from utils import calculate_average

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Complex Flask API!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if 'numbers' not in data:
        return jsonify({"error": "Missing 'numbers' in JSON"}), 400

    result = calculate_average(data['numbers'])
    return jsonify({"average": result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

