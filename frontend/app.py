
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_data = request.form.get('input_data')
        response = requests.get('http://localhost:5001/process_data', params={'input_data': input_data})
        output_data = response.json()['output_data']
        return render_template('home.html', output_data=output_data)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
