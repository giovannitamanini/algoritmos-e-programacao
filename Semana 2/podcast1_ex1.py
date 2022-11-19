# Cálculo do IMC

peso = int(input("Digite o seu peso em [kg]: "))
altura = round(float(input("Digite a sua altura em [m]: ")), 2)

imc = peso/(pow(altura,2))

if imc < 18.5 :
    print("Peso baixo")
elif imc >= 18.5 and imc < 25 :
    print("Peso ideal")
elif imc >= 25 and imc < 30 :
    print("Sobrepeso")
elif imc >= 30 and imc < 40 :
    print("Obesidade")
else :
    print("Obesidade alta")