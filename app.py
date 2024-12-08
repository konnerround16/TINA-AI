import tensorflow as tf
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions

app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def home():
    return "Hello, Flask is working!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'input_data' not in data:
            return jsonify({'error': 'No input_data provided'}), 400
        prediction = data['input_data']  # Replace with your model prediction logic
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
