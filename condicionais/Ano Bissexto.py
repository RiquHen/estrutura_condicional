""" Faça um Programa que peça um número correspondente a um determinado ano
 e em seguida informe se este ano é ou não bissexto. """

ano = int(input("Informe o ano desejado: "))
if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 == 0:
        print("O ano é bissexto, tem 366 dias")
        exit()
    print("O ano é bissexto, tem 366 dias")
else:
    print("O ano não é ano bissexto! Tem 365 dias")

