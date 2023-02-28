"""    10. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        ◦ o produto do dobro do primeiro com metade do segundo .
        ◦ a soma do triplo do primeiro com o terceiro.
        ◦ o terceiro elevado ao cubo."""

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))
num3 = float(input("Digite um numero real: "))

op1 = (2 * num1) * (num2 / 2)
op2 = (3 * num1) + num3
op3 = num3 ** 3
print(f"numero 1: {num1} - numero 2: {num2} - numero 3: {num3}")

print(f"\nproduto do primeiro com metade do segundo: {op1}.")
print(f"Soma do triplo do primeiro com metade do segundo: {op2}")
print(f"O terceiro elevado ao cubo: {op3}")
