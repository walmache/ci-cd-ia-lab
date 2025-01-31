import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Cargar modelo entrenado
#with open('model/model.pkl', 'rb') as f:
#    model = pickle.load(f)

def load_model():
    with open('model/model.pkl', 'rb') as f:
        return pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    # data = request.json['data']
    # prediction = np.argmax(model.predict([data]), axis=1)
    # return jsonify({'prediction': int(prediction[0])})
    #model = load_model()  # Se carga solo cuando se necesita
    #data = request.json['data']
    #prediction = np.argmax(model.predict([data]), axis=1)
    #return jsonify({'prediction': int(prediction[0])})
    try:
        print("Cargando modelo...")
        model = load_model()
        print("Modelo cargado correctamente.")

        data = request.json['data']
        print(f"Datos recibidos: {data}")
        
        if data is None:
            return jsonify({'error': 'Sin datos'}), 400

        # Convertir a numpy array
        np_data = np.array(data, dtype=np.float32)

        # Asegurar que la forma del array es correcta
        if np_data.ndim == 1:
            np_data = np_data.reshape(1, -1)

        prediction = np.argmax(model.predict(np_data), axis=1)
        print(f"Predicción generada: {prediction}")

        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        print(f"Error en la predicción: {e}")
        return jsonify({'error': str(e)}), 500
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)