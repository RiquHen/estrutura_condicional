"""Faça um Programa que peça uma data no formato dd/mm/aaaa e
determine se a mesma é uma data válida"""
d = int(input("Informe o dia: "))
if d > 31:
    print("Data Inválida!")
    exit()
m = int(input("Informe o mes: "))
if m > 12:
        print("Data Inválida!")
        exit()
elif m == 2 and d > 29:
    print("Data inválida")
    exit()
else:
    a = int(input("Informe o ano: "))
print(f"Data Válida: {d}/{m}/{a} ")