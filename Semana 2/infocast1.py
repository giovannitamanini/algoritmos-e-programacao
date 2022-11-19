import math

a = int(input("Coeficiente a: "))
b = int(input("Coeficiente b: "))
c = int(input("Coeficiente c: "))

if a == 0 :
    print("Só existe uma raiz real para a equação!")
    print("A raiz é igual a",round(-c/b,2))
else :
    delta = pow(b, 2) - 4 * a * c
    if delta < 0 :
        print("Não existe raiz real para o problema!")
    else :
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"As raízes de Báscara para os coeficientes informados são {raiz1} e {raiz2}")