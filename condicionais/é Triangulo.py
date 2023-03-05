"""Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
◦ Dicas:
◦ Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
◦ Triângulo Equilátero: três lados iguais;
◦ Triângulo Isósceles: quaisquer dois lados iguais;
◦ Triângulo Escaleno: três lados diferentes;"""
print(30 * "==", "\nVerificar se numeros digitados formam um triângulo\n" + 30 * "==")
lado_1 = float(input("Informe o lado 1: "))
lado_2 = float(input("Informe o lado 2: "))
lado_3 = float(input("Informe o lado 3: "))
if lado_1 + lado_2 > lado_3 and lado_2 + lado_3 > lado_1 and lado_1 + lado_3 > lado_2:
    status = "é"
    if lado_1 == lado_2 and lado_2 == lado_3:
        t = "equilátero"
    elif lado_1 == lado_2 and lado_2 != lado_3 or lado_1 == lado_3 and lado_1 != lado_2 or lado_2 == lado_3 and lado_3 != lado_1:
        t = "isósceles"
    else:
        t = "escaleno"
    print(f"Os lados {lado_1}, {lado_2} e {lado_3} formam um triângulo {t}.")
else:
    print(
        f"Os lados {lado_1}, {lado_2} e {lado_3} não podem formar um triângulo.")
