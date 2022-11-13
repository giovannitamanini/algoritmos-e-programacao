# Algoritmo que calcula preço de automóvel ao consumidor sabendo da porcentagem para o distribuidor e impostos

# Dados de entrada
porcentagem_do_distribuidor = 28/100
impostos = 45/100
custo_de_fabrica = float(input("Digite o custo de fábrica do veículo: R$"))

# Cálculo
custo_ao_consumidor = custo_de_fabrica + custo_de_fabrica * (porcentagem_do_distribuidor + impostos)

# Saída
print("O custo ao consumidor será de R$",round(custo_ao_consumidor,2))