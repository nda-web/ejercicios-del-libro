import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
HEADERS = {"Authorization": "Bearer TU_HUGGINGFACE_TOKEN"}

def get_ai_response(message):
    response = requests.post(API_URL, json={"inputs": message}, headers=HEADERS)
    return response.json()[0]["generated_text"] if response.status_code == 200 else "Error al obtener respuesta"
