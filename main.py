from email.message import EmailMessage
import smtplib

#SIGA NOSSO INSTAGRAM PYTHON_BRASIL A MELHOR COMUNIDADE DE PYTHON

EMAIL = 'seu_email@gmail.com'
SENHA = 'sua_senha'

msg = EmailMessage()
msg['Subject'] = 'ENVIO DE E-MAIL COM SMTPLIB'
msg['From'] = EMAIL
msg['To'] = 'destinatario@gmail.com'
msg.set_content('HELLOW WORLD')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL, SENHA)
    smtp.send_message(msg)
