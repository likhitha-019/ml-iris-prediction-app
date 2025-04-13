import requests

url = "http://127.0.0.1:5000/predict"

# Test inputs
inputs = [
    {"features": [5.1, 3.5, 1.4, 0.2]},  # Expected output: {"prediction": 0}
    {"features": [6.7, 3.1, 4.7, 1.5]},  # Expected output: {"prediction": 1}
    {"features": [5.9, 3.0, 5.1, 1.8]}   # Expected output: {"prediction": 2}
]

for input_data in inputs:
    response = requests.post(url, json=input_data)
    print(f"Input: {input_data['features']} -> Response: {response.json()}")