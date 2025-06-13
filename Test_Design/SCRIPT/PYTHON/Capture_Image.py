import requests
from datetime import datetime

# Endereço IP fornecido pelo IP Webcam no celular
CAMERA_IP = "http://192.168.1.100:8080"

# Endpoint para capturar imagem
IMAGE_URL = f"{CAMERA_IP}/shot.jpg"

def capture_and_save_image():
    try:
        response = requests.get(IMAGE_URL, stream=True)
        if response.status_code == 200:
            # Nome do arquivo com timestamp
            filename = f"foto_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"📷 Foto salva como: {filename}")
        else:
            print(f"Erro ao capturar imagem: status {response.status_code}")
    except Exception as e:
        print(f"Erro: {e}")

capture_and_save_image()
