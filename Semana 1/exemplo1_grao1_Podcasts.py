# Problema: digite o primeiro termo de uma PA (a1), a razão (r) e o termo a ser calculado. 
# Após, calcule o n-ésimo termo da PA, a soma dos termos e o termo médio

a1 = int(input("a1: " ))
r = int(input("r: "))
n = int(input("n: "))

an = a1 + (n - 1) * r
soma_termos = ((a1 + an) * n) / 2
termo_medio = (a1 + an) / 2

print("n-ésimo termo: " , an)
print(f"Soma dos termos:  {soma_termos: .2f}")
print("Termo médio: " + str(termo_medio))