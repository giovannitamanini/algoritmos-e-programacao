# Algoritmo da fazenda

# Constantes
DIAS_POR_SEMANA = 7
MEDIA_DE_SEMANAS_POR_MES = 4.2857
FERRADURAS_POR_CAVALO = 4

# Dados de entrada
numero_de_cavalos = int(input("Quantos cavalos tem na fazenda? "))
numero_de_vacas = int(input("Quantas vacas tem na fazenda? "))
numero_de_ovelhas = int(input("Quantas ovelhas tem na fazenda? "))
producao_diaria_de_leite_por_vaca = 3.2
producao_tosquia_de_la_por_ovelha = 2.3

# Cálculos
volume_leite_diario = numero_de_vacas * producao_diaria_de_leite_por_vaca
volume_leite_semanal = volume_leite_diario * DIAS_POR_SEMANA
volume_leite_mensal = volume_leite_semanal * MEDIA_DE_SEMANAS_POR_MES
volume_la_tosquilha = producao_tosquia_de_la_por_ovelha * numero_de_ovelhas
ferraduras_necessarias = numero_de_cavalos * FERRADURAS_POR_CAVALO

# Saídas
print("Produção de lete diário:",volume_leite_diario,"litros/dia")
print("Produção de leite semanal:",volume_leite_semanal,"litros/semana")
print("Produção média de leite mensal:",volume_leite_mensal,"litros/mês")
print("Produção de lã a cada tosquilha:",volume_la_tosquilha,"kg/tosquilha")
print("Ferraduras necessárias para os cavalos:",ferraduras_necessarias)