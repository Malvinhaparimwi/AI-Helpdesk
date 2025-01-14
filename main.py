import requests

API_ENDPOINT="http://0.0.0.0:5000/v1/transcriptions"
API_KEY="dummy_api_key"
CHUNK_SIZE = 5_242_880 

params = {
    "file": "havard.wav",
}
headers = {
    "authorization": API_KEY,
    "content-type": "application/json"
}

r = requests.post(API_ENDPOINT, params=params, headers=headers)

print(r)
print(r.text)