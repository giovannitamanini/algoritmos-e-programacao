nome = input("Digite o nome: ")
altura = float(input("Digite a altura: "))
peso = int(input("Digite o peso: "))

imc = peso / (altura * altura)

print("IMC: " + str(imc))
