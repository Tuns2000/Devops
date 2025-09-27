import random
import time
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate_number():
    number = random.randint(1, 100)
    return jsonify({"number": number, "timestamp": time.time(), "service": "generator"})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "service": "generator"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))
