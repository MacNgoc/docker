import requests


URL = 'http://127.0.0.1:5001/predict'

data = '5'
result = requests.post(URL, data)

print(f'Result={result}')