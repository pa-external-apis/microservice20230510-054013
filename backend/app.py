
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_data', methods=['GET'])
def process_data():
    input_data = request.args.get('input_data')
    # Add business logic here to process the input data
    output_data = input_data.upper()
    return jsonify({'output_data': output_data})

if __name__ == '__main__':
    app.run(port=5001)
