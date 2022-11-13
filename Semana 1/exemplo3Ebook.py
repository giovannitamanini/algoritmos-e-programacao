# Algoritmo em Python que mostra a soma dos números pares entre 1 e 50

soma = 0

for num in range(51) :
    if num % 2 == 0 :
        soma += num

print("Soma = ",soma)