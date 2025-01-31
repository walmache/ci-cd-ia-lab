import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Cargar modelo entrenado
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])

def predict():
    data = request.json['data']
    prediction = np.argmax(model.predict([data]), axis=1)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)