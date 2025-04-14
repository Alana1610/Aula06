resp= "sim"
while resp=="sim":
    nota1= int(input("Digite a primeria nota:"))
    while nota1 >10 or nota1 <0:
        nota1 = int(input("Digite novamente a primeira nota:"))

    nota2= int(input("Digite a segunda nota:"))
    while nota2 >10 or nota2 <0:
        nota2 = int(input("Digite novamente a segunda nota:"))
    media= (nota1+nota2)/2
    print(f"A media sera {media}")
    resposta= input("Deseja repetir o calculo?")