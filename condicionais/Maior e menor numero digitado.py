num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))

if(num1 > num2):
    if(num1 > num3):
        maior = num1
        menor = num3
    else:
        maior = num3
        menor = num2
else:
    if num2 > num3:
        maior = num2
        menor = num3
    else:
        maior = num3
        menor = num1

print(f"Maior Número: {maior}")
print(f"Menor Número: {menor}")
