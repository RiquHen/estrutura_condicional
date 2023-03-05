"""   Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
 As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais
e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
◦ Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
uma nota de 5 e uma nota de 1;
◦ Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1."""
print(30 * "==")
prog =  "*** Caixa eletrônico ***"
print(f"{prog:>40}")
print(30 * "==")
ce = ci = de = cin = um = 0
sac = float(input("Valor da retirada: "))

notas = str("")
while sac >= 100:
    ce += 1
    sac -= 100

while sac >= 50:
    ci += 1
    sac -= 50
while sac >= 10:
    de += 1
    sac -= 10
while sac >= 5:
    cin += 1
    sac -= 5
while sac >= 1:
    um += 1
    sac -= 1
if ce == 1:
    notas = f"{ce} cédula de 100"
elif ce > 1:
    notas = f"{ce} cédulas de 100"
if ci == 1:
    notas += f"\n{ci} cédula de 50"
elif ci > 1:
    notas += f"\n{ci} cédulas de 50"
if de == 1:
    notas += f"\n{de} cédula de 10"
elif de > 1:
    notas += f"\n{de} cédulas de 10"
if cin == 1:
    notas += f"\n{cin} cédula de 5"
elif cin > 1:
    notas += f"\n{cin} cédulas de 5"
if um == 1:
    notas += f"\n{um} cédula de 1"
elif um > 1:
    notas += f"\n{um} cédulas de 1"
print(notas)