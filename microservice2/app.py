import os
import statistics
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Хранение последних полученных чисел
numbers = []
MAX_NUMBERS = 10

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Processor service is running"})

@app.route('/process', methods=['GET'])
def process_data():
    generator_url = os.environ.get('GENERATOR_URL', 'http://microservice1:5001')
    
    try:
        response = requests.get(f"{generator_url}/generate")
        if response.status_code == 200:
            data = response.json()
            number = data.get('number')
            
            # Добавляем число в список и ограничиваем размер списка
            numbers.append(number)
            if len(numbers) > MAX_NUMBERS:
                numbers.pop(0)
                
            # Вычисляем статистику
            stats = {
                "received_number": number,
                "count": len(numbers),
                "mean": statistics.mean(numbers) if numbers else 0,
                "min": min(numbers) if numbers else 0,
                "max": max(numbers) if numbers else 0,
                "service": "processor"
            }
            return jsonify(stats)
        else:
            return jsonify({"error": f"Failed to get data from generator: {response.status_code}"}), 500
    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "service": "processor"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5002)))
