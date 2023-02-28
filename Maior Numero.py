#Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("insira um numero: "))
num2 = int(input("insira outro numero: "))

if num1 > num2:
    print(f"O primeiro numero é maior, pois {num1} > {num2}")
else:
    print(f"O segundo numero é maior, pois {num2} > {num1}")