
# Importa los módulos necesarios
from dotenv import load_dotenv
import os
import flask
from twilio.twiml.messaging_response import MessagingResponse
import threading
import dotenv
import twilio.rest
from pathlib import Path
dotenv_path = Path('./credtwilio.env')
load_dotenv(dotenv_path=dotenv_path)#

# Accede a las variables de entorno
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

# Verifica los valores (o realiza otras operaciones)
print(f"Account SID: {account_sid}")
print(f"Auth Token: {auth_token}")

app = flask.Flask(__name__)

def process_message(msg):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = twilio.rest.Client(account_sid, auth_token)

    # Aquí puedes procesar el mensaje recibido de manera asincrónica.
    if msg == "QR":
        # Generar código QR usando la API de Twilio o una biblioteca externa
        qr_code = "código QR"  # generate_qr_code(msg)
        message = client.messages.create(
            to="+1234567890",  # Reemplaza con el número de teléfono del usuario
            from_="+1987654321",  # Reemplaza con tu número de teléfono de Twilio
            body=f"Tu código QR: {qr_code}"
        )
        if message.sid:
            return "Código QR generado y enviado."

        else:
            return "Error al generar o enviar el código QR."
    else:
        return "Mensaje no reconocido."

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    msg = flask.request.form.get('Body')
    resp = MessagingResponse()
    numero_remitente = request.headers.get('From')
    thread = threading.Thread(target=process_message, args=(msg,))
    thread.start()
    resp.message(numero_remitente + " Tu mensaje: "+ msg +  "está siendo procesado.")
    return str(resp)

#@app.route("/whatsapp", methods=['POST'])
#def process_message():
    # Obtén el contenido del mensaje de la solicitud
#   cuerpo_mensaje = request.form.get('Body')

    # Obtén el número de WhatsApp del remitente desde la cabecera 'From'
   

    # Procesa el mensaje y el número del remitente
    # ...

    # Crea un objeto MessagingResponse
#  resp = MessagingResponse()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

