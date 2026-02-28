import os
import requests
import random

# --- CONFIGURACIÓN DE TELEGRAM ---
# Usamos .get() para que si falta la clave, no se estrelle el programa de golpe, 
# sino que nos avise con un mensaje de error más claro.
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def enviar_mensaje_telegram(texto):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ ERROR: Faltan las claves de Telegram en los 'Secrets' de GitHub.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID, 
        "text": texto, 
        "parse_mode": "Markdown" # Permite poner negritas en Telegram
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Mensaje enviado a Telegram correctamente.")
        else:
            print(f"⚠️ Error de Telegram: {response.text}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

# --- INTELIGENCIA DEL ROBOT (Loterías) ---
def generar_euromillones():
    # 5 números (del 1 al 50) y 2 estrellas (del 1 al 12)
    numeros = sorted(random.sample(range(1, 51), 5))
    estrellas = sorted(random.sample(range(1, 13), 2))
    return numeros, estrellas

def generar_primitiva():
    # 6 números (del 1 al 49)
    numeros = sorted(random.sample(range(1, 50), 6))
    return numeros

# --- EJECUCIÓN DEL ROBOT ---
if __name__ == "__main__":
    print("🤖 Despertando Robot de Lotería...")
    
    # 1. Generar combinaciones
    euro_nums, euro_stars = generar_euromillones()
    primi_nums = generar_primitiva()
    
    # 2. Preparar el mensaje visual
    mensaje = (
        "🤖 *PREDICCIÓN SEMANAL DEL ROBOT* 🤖\n\n"
        "🇪🇺 *Euromillones*\n"
        f"👉 Números: `{euro_nums}`\n"
        f"⭐ Estrellas: `{euro_stars}`\n\n"
        "🇪🇸 *La Primitiva*\n"
        f"👉 Números: `{primi_nums}`\n\n"
        "🍀 ¡Mucha suerte!"
    )
    
    # 3. Enviar al móvil
    enviar_mensaje_telegram(mensaje)
    print("🏁 Proceso terminado.")
