# Cálculo da média

nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
nota_3 = float(input("Digite sua terceira nota: "))

media = round((nota_1 + nota_2 + nota_3)/3, 2)

if media < 3 :
    print("Você está reprovado com média",media)
elif media >=3 and media < 6 :
    print("Você está em recuperação com média parcial",media)
    recuperacao = float(input("Digite sua nota de recuperação: "))
    media = round((media+recuperacao)/2, 2)
    if media < 6 :
        print("Você está reprovado com média",media)
    else :
        print("Você está aprovado com média",media)
else :
    print("Você está aprovado com média",media)