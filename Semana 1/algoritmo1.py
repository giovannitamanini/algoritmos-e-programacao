# Imports
import math

# Entrada dos dados
x_1 = float(input("Valor da coordenada x1: "))
y_1 = float(input("Valor da coordenada y1: "))
x_2 = float(input("Valor da coordenada x2: "))
y_2 = float(input("Valor da coordenada y2: "))

# Cálculo
distancia_entre_os_pontos = math.sqrt(pow(y_2 - y_1, 2)+pow(x_2 - x_1, 2))

# Saída
print("A distância entre os dois pontos no plano cartesiano é de: ",distancia_entre_os_pontos)

print(11%3)