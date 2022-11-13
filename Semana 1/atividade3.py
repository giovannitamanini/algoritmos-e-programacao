# Escreva um algoritmo que receba como entrada valores de DOIS pontos no plano cartesiano (x1,y1) e
# (x2,y2) e calcule a distância entre esses pontos.

#Imports
import math

# Entradas
x_1 = float(input("Coordenada x1: "))
y_1 = float(input("Coordenada y1: "))
x_2 = float(input("Coordenada x2: "))
y_2 = float(input("Coordenada y2: "))

# Cálculo
distancia_entre_os_dois_pontos = math.sqrt(pow(y_2-y_1, 2) + pow(x_2-x_1, 2))

# Saída
print("A distância entre os dois pontos é de ",distancia_entre_os_dois_pontos)