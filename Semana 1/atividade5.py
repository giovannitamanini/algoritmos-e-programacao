# Algoritmo para as áreas do triângulo, trapézio, quadrado, retângulo e losango sendo:
# A = base do triângulo, base menor do trapézio, lado do quadrado, um dos lados do retângulo, diagonal maior do losango
# B = altura do triângulo, base maior do trapézio, um dos lados do retângulo, diagonal menor do losango
# C = altura do trapézio

# Entradas
A = float(input("Qual é a medida de A em centímetros? "))
B = float(input("Qual é a medida de B em centímetros? "))
C = float(input("Qual é a medida de C em centímetros? "))

# Cálculos
area_do_triangulo = (A*B)/2
area_do_trapezio = ((A*B)*C)/2
area_do_quadrado = A*A
area_do_retangulo = A*B
area_do_losango = (A*B)/2

# Saídas
print("Área do triângulo:",area_do_triangulo,"cm²")
print("Área do trapézio:",area_do_trapezio,"cm²")
print("Área do quadrado:",area_do_quadrado,"cm²")
print("Área do retângulo:",area_do_retangulo,"cm²")
print("Área do losango:",area_do_losango,"cm²")