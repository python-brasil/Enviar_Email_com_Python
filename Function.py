from email.message import EmailMessage
import smtplib

def center(janela, largura, altura):
    janela = janela
    largura = largura
    altura = altura
    largura_screen = janela.winfo_screenwidth()
    altura_screen = janela.winfo_screenheight()
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    centro = '%dx%d+%d+%d' % (largura, altura, posx, posy)
    return centro

def enviar_email(remetende, senha, destinatario, assunto, mensagem):
    
# EMAIL = 'pythonbrasil821@gmail.com'
# SENHA = 'niqnsawgguoublvy'

    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = remetende
    msg['To'] = destinatario
    msg.set_content(mensagem)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(remetende, senha)
        smtp.send_message(msg)