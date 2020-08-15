while True:
    senha = "2002"
    password = int(input())
    if str(password) != senha:
        print("Senha Invalida")
    
    if str(password) == senha:
        print("Acesso Permitido")
        break