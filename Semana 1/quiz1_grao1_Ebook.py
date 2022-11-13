# Algoritmo que calcula a área, perímetro e diâmetro de uma circunferência a partir
# do raio

# Dados do problema
PI = 3.1416

# Input do raio pelo usuário
raio = int(input("Raio da circunferência (valor inteiro): "))

# Cálculos
area = PI * pow(raio, 2)
perimetro = 2 * PI * raio
diametro = 2 * raio

# Resultados na tela
print("Área:",area)
print("Perímetro:",perimetro)
print("Diâmetro:",diametro)