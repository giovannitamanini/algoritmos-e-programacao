# Programa para calcular idade em dias de uma pessoa

# Constantes
DIAS_POR_ANO = 365
DIAS_POR_MES = 30

# Dados de entrada
idade_anos = int(input("Digite quantos anos de vida você tem: "))
idade_meses = int(input("Digite os meses sobressalentes da idade: "))
idade_dias = int(input("Digite os dias sobressalentes da idade: "))

# Saída com cálculo
print("A idade total em dias é de " + str((idade_anos*DIAS_POR_ANO)+(idade_meses*DIAS_POR_MES)+idade_dias) + " dias.")