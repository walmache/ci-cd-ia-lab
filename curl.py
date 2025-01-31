import numpy as np
import json
import subprocess

# Generar una matriz aleatoria de 28x28 con valores entre 0 y 1
data = np.random.rand(28, 28).tolist()

# Agregar una dimensión extra para que tenga la forma (1, 28, 28)
data_with_batch = [data]  # Esto convierte (28,28) en (1,28,28)

# Convertir los datos en un JSON válido
payload = json.dumps({"data": data_with_batch})

# URL de la API en Cloud Run
url = "https://ci-cd-ia-416965750887.us-central1.run.app/predict"

# Crear el comando `curl`
curl_command = f'curl -X POST -H "Content-Type: application/json" -d \'{payload}\' {url}'

# Imprimir la `curl` generada (por si quieres ejecutarla manualmente)
print("\n🚀 Ejecutando el siguiente comando `curl`:\n")
print(curl_command, "\n")

# Ejecutar el `curl` en la terminal y obtener la respuesta
process = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

# Mostrar la respuesta de la API
print("\n📌 **Respuesta de la API:**")
print(process.stdout)
