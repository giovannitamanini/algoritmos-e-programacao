# A partir de tempo em segundos, devolver tempo em horas, minutos e segundos

# Constantes
SEGUNDOS_POR_HORA = 3600
SEGUNDOS_POR_MINUTO = 60

# Dados de entrada
tempo_em_segundos = int(input("Digite o tempo do evento em segundos: "))

# Cálculos
tempo_em_horas = tempo_em_segundos / SEGUNDOS_POR_HORA
tempo_em_minutos = (tempo_em_segundos % SEGUNDOS_POR_HORA) / SEGUNDOS_POR_MINUTO
tempo_em_segundos = (tempo_em_segundos % SEGUNDOS_POR_HORA) % SEGUNDOS_POR_MINUTO

# Saída
print("O tempo total do evento é de " + str(int(tempo_em_horas)) + " horas, " + str(int(tempo_em_minutos)) + " minutos e " + str(int(tempo_em_segundos)) + " segundos.")