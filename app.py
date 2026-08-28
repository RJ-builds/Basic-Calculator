from flask import Flask, request, jsonify
import os
 
# Reuses your existing calculator() function directly —
# the if __name__ == "__main__" guard in calculator.py means
# importing it here does NOT trigger the terminal CLI loop
from basic_calculator import calculator
 
app = Flask(__name__, static_folder=os.getcwd(), static_url_path='')
 
 
@app.route('/')
def home():
    return app.send_static_file('index.html')
 
 
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
 
        choice = int(data['choice'])
        x = float(data['x'])
        y = float(data['y'])
 
        result = calculator(choice, x, y)
 
        # calculator() returns a string for invalid choice / divide-by-zero
        # instead of a number — treat that case as a handled error, not a crash
        if isinstance(result, str):
            return jsonify({'success': False, 'error': result})
 
        return jsonify({'success': True, 'result': result})
 
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400
 
 
if __name__ == '__main__':
    app.run(debug=True)