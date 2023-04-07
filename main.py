from Function import *
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import os



class Email_bot ():
    def __init__(self):
        
        #Variaveis//////////////////
        self.color1 = '#f6f8fc' #Fundo
        self.color2 = '#444746' #Destaque
        self.color3 = '#d3e3fd' #Inputs
        self.color4 = '#d3e3fd' #Purple Detals
        self.color5 = '#4285f4' #blue Detals 
        
        

        
        self.window()
        
    def window(self):
        self.root = Tk()
        self.root.geometry(center(self.root,600,650))
        self.root.config(bg=self.color1)
        self.root.title('E-MAIL BOT')
        # self.root.resizable(False,False)
        self.containers()
        self.itens_container1()
        self.itens_container2()
        
        self.root.mainloop()
        
    def containers(self):
        self.img_logo = PhotoImage(file=f'img\LOGO.png')
        self.lb_title = Label(
            self.root,
            image= self.img_logo,
            fg= self.color4,
            bg=self.color1
        )
        
        self.fr_container01 = Frame(
            self.root,
            width=310,
            height= 230,
            bg=self.color1
        )
        
        self.fr_container02 = Frame(
            self.root,
            width=550,
            height= 300,
            bg=self.color1
        )
        
        self.fr_container01.propagate(0)
        self.fr_container02.propagate(0)
        self.lb_title.pack()
        self.fr_container01.pack()
        self.fr_container02.pack()
        
    def itens_container1(self):
        
        #Variaveis para o Check_Button
        self.chkValue = BooleanVar() 
        self.chkValue.set(True)
        
        self.lb_email = Label(
            self.fr_container01,
            text="E-mail",
            bg=self.color1,
            fg= self.color2,
        )
        
        self.en_email = Entry(
            self.fr_container01,
            bg=self.color3,
            width=35,
            font='15',
            fg= self.color2,
            bd=0
        )
        
        self.lb_senha = Label(
            self.fr_container01,
            text="Senha",
            bg=self.color1,
            fg= self.color2,
        )
         
        self.en_senha = Entry(
            self.fr_container01,
            bg=self.color3,
            width=35,
            font='15',
            show="*",
            fg= self.color2,
            bd=0
        )
        
        self.lb_remetende = Label(
            self.fr_container01,
            text="Remetende",
            bg=self.color1,
            fg= self.color2,
        )
        
        self.en_remetende = Entry(
            self.fr_container01,
            bg=self.color3,
            width=35,
            font='15',
            fg= self.color2,
            bd=0
        )
        
        self.lb_assunto = Label(
            self.fr_container01,
            text="Assunto",
            bg=self.color1,
            fg= self.color2,
        )
        
        self.en_assunto = Entry(
            self.fr_container01,
            bg=self.color3,
            width=35,
            font='15',
            fg= self.color2,
            bd=0
        )
        self.contaier_relembrar = Frame(
            self.fr_container01,
            bg=self.color1,
            width=35
        )
        self.lb_relembrar = Label(
            self.contaier_relembrar,
            text="Lembrar dados",
            bg=self.color1,
            fg= self.color2,
        )
        self.ck_relembrar = Checkbutton(
            self.contaier_relembrar,
            bg=self.color1,
            bd=0,
            activebackground=self.color1,
            fg=self.color2,
            var = self.chkValue
        )
        
        self.btn_enviar = Button(
            self.fr_container01,
            bg=self.color5,
            fg= 'white',
            text="ENVIAR >",
            command= self.enviar,
            activebackground='#3684ff',
            width=50
        )
        
        
        # Lendo o arquivo para 
        if os.path.exists('info_salvas.txt'):
            #Lendo o arquivo
            arquivo = open('info_salvas.txt','r')
            info_login = []
            for i in arquivo:
                i.replace('\n', '')
                info_login.append(i)
            arquivo.close()
            
            # Removendo dados antes de colocar novos
            self.en_email.delete(0, END)
            self.en_senha.delete(0, END)
            self.en_remetende.delete(0, END)
            self.en_assunto.delete(0, END)
            
            # Colocando os valores salvos
            self.en_email.insert(0, info_login[0])
            self.en_senha.insert(0, info_login[1])
            self.en_remetende.insert(0, info_login[2])
            self.en_assunto.insert(0, info_login[3])
            
        self.lb_email.pack(anchor=W)
        self.en_email.pack(anchor=W)
        self.lb_senha.pack(anchor=W)
        self.en_senha.pack(anchor=W)
        self.lb_remetende.pack(anchor=W)
        self.en_remetende.pack(anchor=W)
        self.lb_assunto.pack(anchor=W)
        self.en_assunto.pack(anchor=W)
        self.contaier_relembrar.pack(anchor=E)
        self.lb_relembrar.grid(row=0,column=0)
        self.ck_relembrar.grid(row=0, column=1)
        self.btn_enviar.pack(pady=5)
          
    def itens_container2(self):
        self.lb_mensagem = Label(
            self.fr_container02,
            text='Mensagem:',
            bg=self.color1,
            fg= self.color2,
        )
        self.tx_mensagem = Text(
            self.fr_container02,
            bg=self.color3,
            width=550,
            height=15,
            font='15',
            fg= self.color2,
            bd=2
        )
        
        self.lb_mensagem.pack(anchor=W)
        self.tx_mensagem.pack()
         
    def enviar(self):
        remetende = self.en_email.get().replace('\n','')
        senha = self.en_senha.get().replace('\n','')
        destinatario = self.en_remetende.get().replace('\n','')
        assunto = self.en_assunto.get().replace('\n','')
        mensagem = self.tx_mensagem.get('1.0','end-1c')
        if (remetende == '')|(senha == '')|(destinatario == '')|(assunto == ''):
            messagebox.showwarning("CAMPOS VAZIOS", "Existem campos obrigatórios vazios")
        else: 
            #Validar se o usuário deseja salvar as informações
            if self.chkValue.get() == True:
                #Sobrescreve o arquivo sempre que a checkbox estiver selecionada
                arquivo = open('info_salvas.txt','w')
                arquivo.write(f"{remetende}")
                arquivo.write(f"\n{senha}")
                arquivo.write(f"\n{destinatario}")
                arquivo.write(f"\n{assunto}")
            else:
                print('USUÁRIO DESEJOU NÃO SALVAR AS INFORMAÇÕES')
            
            try:    
                enviar_email(remetende, senha, destinatario, assunto, mensagem)
                messagebox.showinfo("SUCESSO", "A mensagem foi enviada com sucesso")
                
            except smtplib.SMTPAuthenticationError:
                messagebox.showwarning("ERROR", "Não foi possível enviar o e-mail\nVerifique se o e-mail ou senha está correto")
            except smtplib.SMTPRecipientsRefused:
                messagebox.showwarning("ERROR", "Não foi possível enviar o e-mail\nVerifique se o e-mail do destinatário está correto")
            
        
Email_bot ()