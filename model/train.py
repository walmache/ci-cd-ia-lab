import tensorflow as tf
from tensorflow import keras
import pickle

# Cargar dataset MNIST
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Definir modelo
model = keras.Sequential([keras.layers.Flatten(input_shape=(28, 28)),
                          keras.layers.Dense(128, activation='relu'),
                          keras.layers.Dense(10, activation='softmax')
                          ])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar modelo
model.fit(x_train, y_train, epochs=5)
# Guardar modelo
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Modelo entrenado y guardado en model.pkl")