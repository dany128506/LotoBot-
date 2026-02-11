import os
import requests
import random
from collections import Counter

# --- CONFIGURACIÓN TELEGRAM ---
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": texto}
    requests.post(url, json=payload)

# --- TU LÓGICA DE LOTERÍA (Simplificada para el ejemplo) ---
def generar_prediccion():
    # Aquí iría tu código de scraping real
    # Simulamos para el ejemplo:
    numeros = sorted([random.randint(1, 50) for _ in range(5)])
    estrellas = sorted([random.randint(1, 12) for _ in range(2)])
    return numeros, estrellas

# --- EJECUCIÓN PRINCIPAL ---
if __name__ == "__main__":
    try:
        nums, stars = generar_prediccion()
        
        mensaje = (
            "🤖 *NUEVA PREDICCIÓN DEL ROBOT* 🤖\n\n"
            "🇪🇺 **Euromillones**\n"
            f"Números: {nums}\n"
            f"Estrellas: {stars}\n\n"
            "🍀 ¡Buena suerte!"
        )
        
        print("Enviando a Telegram...")
        enviar_mensaje(mensaje)
        print("¡Enviado!")
        
    except Exception as e:
        enviar_mensaje(f"⚠️ Error en el robot: {e}")
