"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 Kg)
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável
peso(peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e
na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""

peso_regulamentado = 50
multa_kg = 4

pesodepeixes = float(input("Informe o peso de peixe: "))
if pesodepeixes <= peso_regulamentado:
    print("Hoje não houve peso alem do limite regulamentado\nNenhuma multa  a ser paga!")
else:
    excesso = pesodepeixes - peso_regulamentado
    print(f"Peso acima do limite: {excesso:.2f} kg")
    print(f"Valor da multa a ser paga: R$ {excesso*multa_kg:.2f}")
