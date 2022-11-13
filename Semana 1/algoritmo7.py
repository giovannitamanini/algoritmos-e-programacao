# Programa que calcula média das 3 notas ponderada de aluno (pesos 2, 3 e 5 respectivamente)

# Dados de entrada
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

# Cálculo e saída
print("A média final ponderada do aluno é de " + str(round((((nota_1*2)+(nota_2*3)+(nota_3*5))/10),2)))