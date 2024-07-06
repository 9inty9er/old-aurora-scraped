from flask import Flask, request, jsonify
from nlp import process_message
from system_monitor import get_system_status

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def message():
    data = request.json
    response = process_message(data['message'])
    return jsonify({'response': response})

@app.route('/status', methods=['GET'])
def status():
    return jsonify(get_system_status())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

