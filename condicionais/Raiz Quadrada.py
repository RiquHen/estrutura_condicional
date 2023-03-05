"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
◦ Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
o programa não deve fazer pedir os demais valores, sendo encerrado;
◦ Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
◦ Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
◦ Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""
a= int(input("Informe o valor de a(com sinal): "))
if a ==0:
    print("O equação não é do segundo grau.")
    exit()
else:
    b= int(input("Informe o valor de b(com sinal): "))
    c= int(input("Informe o valor de c(com sinal): "))
delta = b**2 - 4 * a * c
if delta < 0:
    print(f"A equação [{a}x²{b}x {c}=0] não possui raizes reais")
elif delta ==0:
    print("A equação possui apenas uma raiz real")
else:
    print("A equação possui duas raiz reais")
print(f"{delta}")