pin=123456
tentativa= 1
mensagem="Senha bloqueada"
while tentativa <=3:
    senha=int(input("Digite a senha:"))
    if senha == pin:
        mensagem = "Acertou mizeravi"
        break
    tentativa+=1
    print(mensagem)