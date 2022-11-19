# Mostrar idade de pessoa em anos, meses e dias, a partir da idade expressa em dias

# Constantes
DIAS_POR_ANO = 365
DIAS_POR_MES = 30

# Dados de entrada
idade_em_dias = int(input("Digite a sua idade em dias: "))

# Cálculos

idade_em_anos = int(idade_em_dias / DIAS_POR_ANO)
idade_em_meses = int((idade_em_dias % DIAS_POR_ANO) / DIAS_POR_MES)
idade_em_dias = int((idade_em_dias % DIAS_POR_ANO) % DIAS_POR_MES)

print("Você tem " + str(idade_em_anos) + " anos, " + str(idade_em_meses) + " meses e " + str(idade_em_dias) + " dias.")

print(4/5)

print(int(1453/132))

print(1453//132)