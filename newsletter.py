# tech-info_page
En este repositorio se trabajará todo el código relacionado a la página de información de tecnología.
"""
importamos las libraries utiles el smtplib sirve para sincronizar con el gmail y enviar mensajes
los demas son para personalizar el mensaje y para ponerles fechas y tiempos al programa
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
# poner los correo que participan en este proceso como el sender(envia) y el receiver (recibe) la contraseña es parte del smtp de gmail
sender_email = "xtomura31@gmail.com"
sender_pasword = "qeqk yjrn cbkd gzjx"
receiver_email = "stephanoherrera4444@gmail.com"
# perzonaliacion del mensaje subject el tema o asunto del mensaje y body el cuerpo del mensaje
subject = "test del email"
body = "este email es una prueba del codigo de python sin tiempo programado "
# enviara el mensaje a cierta hora todos los dias 
def enviar_mensaje():
  msg = MIMEMultipart()
  # ponemos los valores a los respectivos de la clase 
  msg["From"] = sender_email
  msg["To"] = receiver_email
  msg["Subject"] = subject
  # este es el mensaje mismo plain es como se quiere el mensaje 
  msg.attach(MIMEText(body , 'plain'))
# envia mensaje de confirmacion si es que se pudo o no enviar el mensaje 
  try:
# sincroniza el codigo con el smtp del usuario que envia el mensaje  
      server = smtplib.SMTP("smtp.gmail.com" , 587)
      server.starttls()
      server.login(sender_email, sender_pasword)
      text = msg.as_string()
# envia el mensaje y manda confirmacion ala terminal      
      server.sendmail(sender_email, receiver_email, text)
     print("EMAIL sent succesfully")
except:
# manda error a la terminal si no se pudo enviar el mensaje (error en el codigo) 
    print("Error: unable to send email")
# agenda la funcion para todos los dias a una cierta hora mientras se ejecuta el codigo
schedule.every().day.at("12:00").do(enviar_mensaje)
# loop para enviar constantemente la funcion a revision para cuando sea la hora se ejecute debidamente
while True:
    schedule.run_pending()
# descanso entre loop y loop para no sobre exigir a la RAM    
    time.sleep(1)
