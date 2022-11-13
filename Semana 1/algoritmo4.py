# Cálculo das raízes de equação do segundo grau

# Imports
import math

# Informações iniciais ao usuário
print("Considerando a equação de segundo grau na forma Ax² + Bx + C = 0, calcula-se as raízes x1 e x2 por Bhaskara\n")

# Dados de entrada
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

# Cálculos e saídas
delta = pow(B,2) - 4*A*C
if (delta < 0) :
    print("Não existe solução real para a equação dada!")
else :
    x_1 = round((-B + math.sqrt(delta))/(2*A),2)
    x_2 = round((-B - math.sqrt(delta))/(2*A),2)
    print("A raiz x1 é igual a",x_1)
    print("A raiz x2 é igual a",x_2)