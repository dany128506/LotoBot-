import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# --- CONFIGURACIÓN DE GMAIL ---
GMAIL_USER = os.environ.get("GMAIL_USER")
GMAIL_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")
DESTINATARIO = "dany128506@gmail.com" # Tu correo de destino

def enviar_correo(asunto, cuerpo):
    if not GMAIL_USER or not GMAIL_PASSWORD:
        print("❌ ERROR: Faltan las claves GMAIL_USER o GMAIL_APP_PASSWORD en los Secrets.")
        return

    # 1. Preparamos la estructura del correo
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = DESTINATARIO
    msg['Subject'] = asunto

    # 2. Añadimos el texto al cuerpo del correo
    msg.attach(MIMEText(cuerpo, 'plain'))

    try:
        # 3. Conectamos con el servidor de Gmail
        print("🌐 Conectando al servidor de Gmail...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() # Activa la seguridad encriptada
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        
        # 4. Enviamos y cerramos
        server.send_message(msg)
        server.quit()
        print(f"✅ ¡Correo enviado con éxito a {DESTINATARIO}!")
        
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")

# --- INTELIGENCIA DEL ROBOT (Loterías) ---
def generar_euromillones():
    numeros = sorted(random.sample(range(1, 51), 5))
    estrellas = sorted(random.sample(range(1, 13), 2))
    return numeros, estrellas

def generar_primitiva():
    numeros = sorted(random.sample(range(1, 50), 6))
    return numeros

# --- EJECUCIÓN DEL ROBOT ---
if __name__ == "__main__":
    print("🤖 Despertando Robot de Lotería...")
    
    euro_nums, euro_stars = generar_euromillones()
    primi_nums = generar_primitiva()
    
    # Preparamos lo que va a decir el correo
    asunto_correo = "🤖 Tu Predicción Semanal de Lotería"
    cuerpo_correo = (
        "🤖 PREDICCIÓN SEMANAL DEL ROBOT 🤖\n\n"
        "🇪🇺 Euromillones\n"
        f"👉 Números: {euro_nums}\n"
        f"⭐ Estrellas: {euro_stars}\n\n"
        "🇪🇸 La Primitiva\n"
        f"👉 Números: {primi_nums}\n\n"
        "🍀 ¡Mucha suerte!"
    )
    
    enviar_correo(asunto_correo, cuerpo_correo)
    print("🏁 Proceso terminado.")
