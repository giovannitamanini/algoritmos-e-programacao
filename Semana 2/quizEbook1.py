# Treinando condicionais

numero_1 = int(input("Digite o número 1: "))
numero_2 = int(input("Digite o número 2: "))

if numero_1%2 == 0 :
    print("Número 1 é PAR")

if numero_1 >= 0 :
    print("Número 1 é Positivo")
else :
    print("Número 1 é Negativo")

if numero_1 > numero_2 :
    print("Número 1 é maior")
elif numero_1 < numero_2 :
    print("Número 2 é maior")
else :
    print("Número 1 e número 2 são iguais")