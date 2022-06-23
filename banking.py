from operator import length_hint
from tkinter import *
import os

from turtle import left, right, update
from PIL import ImageTk, Image

#tela
master = Tk()
master.title('Banking App')
master.geometry("280x350")

#funcoes
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    opc = temp_opc.get()
    opc2 =temp_opc2.get()
    all_accounts = os.listdir()
    print(all_accounts)

    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red", text="Todos os dados precisam ser preenchidos!! ")
        return
    if len(password) < 5 :
        notif.config(fg="red", text="Senha tem que ter entre 5 e 7 caracteres!!")
        return
    if len(password) > 7 :
        notif.config(fg="red", text="Senha tem que ter entre 5 e 7 caracteres!! ")
        return
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="A conta já existe!")
            return   
        else:
            new_file = open(name, "w")   
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(opc+'\n')
            new_file.write(opc2+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green", text="A conta foi criada.")

def register():
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    global temp_opc
    global temp_opc2
    temp_name = StringVar()    
    temp_age = StringVar() 
    temp_gender = StringVar() 
    temp_password = StringVar() 
    temp_opc = StringVar()
    temp_opc2 = StringVar()

    register_screen = Toplevel(master)
    register_screen.title('Registro') 
    register_screen.geometry=("270x400") 
    
   
    Label(register_screen, text="Por favor, insira seus dados para o cadastro:", fg="purple", font=('Calibri',12)).grid(row=0, sticky=N, pady=10)
    Label(register_screen, text="Nome", fg="purple", font=('Calibri',12)).grid(row=1, sticky=W)
    Label(register_screen, text="Idade", fg="purple", font=('Calibri',12)).grid(row=2, sticky=W)
    Label(register_screen, text="Gênero",fg="purple", font=('Calibri',12)).grid(row=3, sticky=W)
    Label(register_screen, text="Senha", fg="purple", font=('Calibri',12)).grid(row=4, sticky=W)
    Label(register_screen, text="Opção de conta: ", fg="purple", font=('Calibri',12)).grid(row=6, sticky=W)


  
    
    Checkbutton(register_screen, text="Conta Poupanca", fg="purple", variable=temp_opc).grid(row=7, padx=(0,0))
    
    
    Checkbutton(register_screen, text="Conta Corrente", fg="purple", variable=temp_opc2).grid(row=8, padx=(0,0))
    

    notif = Label(register_screen, font=('Calibri',12))
    notif.grid(row=6, sticky=N, pady=10)

    Entry (register_screen, textvariable=temp_name).grid(row=1, column=0)
    Entry (register_screen, textvariable=temp_age).grid(row=2, column=0)
    Entry (register_screen, textvariable=temp_gender).grid(row=3, column=0)
    Entry (register_screen, textvariable=temp_password, show="*").grid(row=4, column=0)
    


    #butoes
    Button(register_screen, text="Registro", fg="purple", command= finish_reg, font=('Calibri', 12)).grid(row=9, sticky=N, pady=10)
    

def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            
            #dashboard da conta
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Dashboard')

                #Label
                Label(account_dashboard, text="Dashboard de conta",fg="purple", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
                Label(account_dashboard, text="Olá " + name + " seja muito bem-vindo!", fg="purple", font=('Calibri', 12)).grid(row=1, sticky=N, pady=5)
                #butoes
                Button(account_dashboard, text="Dados pessoais", fg="purple",font=('Calibri',12),width=30, command=dados_pessoais).grid(row=2,sticky=N, padx=10)
                Button(account_dashboard, text="Depósito",fg="purple", font=('Calibri', 12),width=30, command = deposito).grid(row=3,sticky=N, padx=10)
                Button(account_dashboard, text="Saque", fg="purple", font=('Calibri', 12),width=30, command = saque).grid(row=4,sticky=N, padx=10)
                Label(account_dashboard).grid(row=5, sticky=N, pady=10)
                return
            else:
                login_notif.config(fg="red", text="Senha incorreta!")    
                return
  
    login_notif.config(fg="red", text="Nenhuma conta encontrada!")  

def login_funcionario():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        
        if name == login_name:
            file = open(name, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            if len(password) > 6:
                #dashboard da conta
                if login_password == password:
                    login_screen.destroy()
                    account_dashboard = Toplevel(master)
                    account_dashboard.title('Dashboard')

                    #Label
                    Label(account_dashboard, text="Dashboard de conta: ", fg="purple", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
                    Label(account_dashboard, text="Olá " + name + " seja muito bem-vindo!", fg="purple", font=('Calibri', 12)).grid(row=1, sticky=N, pady=5)
                    #butoes
                    Button(account_dashboard, text="Dados pessoais ", fg="purple", font=('Calibri',12),width=30, command=dados_pessoais).grid(row=2,sticky=N, padx=10)
                    Button(account_dashboard, text="Criar nova conta",fg="purple", font=('Calibri', 12),width=30, command = register).grid(row=3,sticky=N, padx=10)
                    Button(account_dashboard, text="Buscar conta", fg="purple", font=('Calibri', 12),width=30, command = login).grid(row=4,sticky=N, padx=10)
                    Label(account_dashboard).grid(row=5, sticky=N, pady=10)
                    return
            else:
                login_notif.config(fg="red", text="Senha incorreta!")    
                return
  
    login_notif.config(fg="red", text="Nenhuma conta encontrada!")  
def deposito():
    #vars
    global amount
    global deposito_notif
    global current_balance_label
    amount = StringVar()
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]

    #tela de deposito
    deposito_screen = Toplevel(master)
    deposito_screen.title('Deposito')

    #Label
    Label(deposito_screen, text="Deposito:", fg="purple", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(deposito_screen, text="Saldo atual: £"  +details_balance,fg="purple", font=('Calibri', 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(deposito_screen, text="Valor: ", fg="purple", font=('Calibri', 12)).grid(row=2, sticky=W)
    deposito_notif = Label(deposito_screen, font=('Calibri',12))
    deposito_notif.grid(row=4, sticky=N, pady=5)

    #entrada
    Entry(deposito_screen, textvariable=amount).grid(row=2, column=1)

    #butao
    Button(deposito_screen, text="Finalisar", fg="purple", font=('Calibri', 12), command=finish_deposito).grid(row=3, sticky=W, pady=5)

def finish_deposito():
    if amount.get() == "":
        deposito_notif.config(text='O valor é necessário!', fg="red")
        return
    if float(amount.get()) <=0:
        deposito_notif.config(text='Valor sugerido é inválido!', fg='red')    
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')    
    current_balance = details[6]
    update_balance = current_balance
    update_balance = float(update_balance) + float(amount.get())
    file_data = file_data.replace(current_balance, str(update_balance))
    file.seek(0)
    file.truncate()
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Saldo: £"+str(update_balance), fg="green")
    deposito_notif.config(text='Saldo atualizado.', fg='green')

def saque():
    #vars
    global saque_amount
    global saque_notif
    global current_balance_label
    saque_amount = StringVar()
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]

    #tela de saque
    saque_screen = Toplevel(master)
    saque_screen.title('Saque')

    #Label
    Label(saque_screen, text="Saque:", fg="purple", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(saque_screen, text="Saldo atual: £" +details_balance, fg="purple", font=('Calibri', 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(saque_screen, text="Valor: ", fg="purple",font=('Calibri', 12)).grid(row=2, sticky=W)
    saque_notif = Label(saque_screen, font=('Calibri',12))
    saque_notif.grid(row=4, sticky=N, pady=5)

    #entrada
    Entry(saque_screen, textvariable=saque_amount).grid(row=2, column=1)

    #butao
    Button(saque_screen, text="Finalisar", fg="purple", font=('Calibri', 12), command=finish_saque).grid(row=3, sticky=W, pady=5)

def finish_saque():
    if saque_amount.get() == "":
        saque_notif.config(text='O valor é necessário!', fg="red")
        return
    if float(saque_amount.get()) <=0:
        saque_notif.config(text='Valor inserido não é aceito!', fg='red')    
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')    
    current_balance = details[6]

    if float(saque_amount.get()) > float(current_balance):
        saque_notif.config(text='Fundo insuficiente!', fg='red')
        return



    update_balance = current_balance
    update_balance = float(update_balance) - float(saque_amount.get())
    file_data = file_data.replace(current_balance, str(update_balance))
    file.seek(0)
    file.truncate()
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Saldo: £"+str(update_balance), fg="green")
    saque_notif.config(text='Saldo atualizado.', fg='green')

def dados_pessoais():
    #vars
    file = open(login_name, 'r')
    file_data = file.read()
    user_dados = file_data.split('\n')
    dados_nome = user_dados[0]
    dados_age = user_dados[2]
    dados_gender = user_dados[3]
    dados_temp_opc = user_dados [4]
    dados_temp_opc2 = user_dados[5]
    
    
    dados_balance = user_dados[6]

    #dados pessoais
    dados_pessoais_screen = Toplevel(master)
    dados_pessoais_screen.title('Dados Pessoais')
    dados_pessoais_screen.geometry=("1200x100")

    #Label
    Label(dados_pessoais_screen, text="Dados pessoais", fg="purple",font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(dados_pessoais_screen, text="Nome : " + dados_nome, fg="purple", font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(dados_pessoais_screen, text="Age : " + dados_age, fg="purple",font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(dados_pessoais_screen, text="Gender : " + dados_gender,fg="purple", font=('Calibri', 12)).grid(row=3, sticky=W)
    Label(dados_pessoais_screen, text="Conta Poupanca :" + dados_temp_opc, fg="purple", font=('Calibri', 12)).grid(row=4, sticky=W)
    Label(dados_pessoais_screen, text="Conta Corrente :" + dados_temp_opc2, fg="purple", font=('Calibri', 12)).grid(row=5, sticky=W)
    Label(dados_pessoais_screen, text="Balance : £ " + dados_balance, fg="purple", font=('Calibri', 12)).grid(row=6, sticky=W)
    
def login():
    #vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name =StringVar()
    temp_login_password =StringVar()
    login_screen = Toplevel(master)
    login_screen.title('Login')

    #label
    Label(login_screen, text="Login para sua conta", fg="purple", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Usuário", fg="purple", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(login_screen, text="Senha", fg="purple", font=('Calibri',12)).grid(row=2,sticky=W)
    login_notif = Label(login_screen, font=('Calibri',12))
    login_notif.grid(row=4,sticky=N)

    #Entrada
    Entry(login_screen, textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_password, show="*").grid(row=2,column=1,padx=5)

    #butoes
    Button(login_screen, text="Login", command=login_session, width=15, fg="purple",font=('Calibri',12)).grid(row=3,sticky=W,pady=5,padx=5)
    Button(login_screen, text="Login funcionario", command=login_funcionario, width=15, fg="purple",font=('Calibri',12)).grid(row=6,sticky=W,pady=5,padx=5)

#importar imagens
img = Image.open('images.jpg')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

Label(master, text="Custom Banking Beta", fg="purple", font=('Calibri', 12)).grid(row=1, sticky=N, pady=10)    
Label(master, text="O banco mais simples que você já usou.", fg="purple", font=('Calibri', 12)).grid(row=2, sticky=N) 
Label(master, image=img).grid(row=3, sticky=N, pady=10)

#butoes
Button(master, text="Registro", fg="purple", font=('Calibri',12), width=20, command=register).grid(row=4, sticky=N)
Button(master, text="Login", fg="purple",font=('Calibri',12), width=20, command=login).grid(row=5, sticky=N, pady=10)

master.mainloop()