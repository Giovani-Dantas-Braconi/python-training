import smtplib
import email.message
from decouple import config

def enviar_email():
    mensagem = email.message.Message()
    mensagem["subject"] = "email enviado com python"
    mensagem["from"] = "giovanieniac@gmail.com.br"
    mensagem["to"] = "giovanidbraconi@gmail.com"
    mensagem["cc"] = "015722020@eniac.edu.br"
    mensagem["Bcc"] = "giovanidbraconi+copia@gmail.com"

    corpo_email = "<p> Boa tarde a todos </p><p style='color: blue;margin: 400px;'>Esse email é foda </p>"

    corpo_email = corpo_email.encode("utf-8")

    mensagem.add_header("content-type", "text/html")
    mensagem.set_payload(corpo_email)

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(user = mensagem["from"], password = config("PASSWORD"))

enviar_email()