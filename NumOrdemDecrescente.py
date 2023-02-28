n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))

if n1 < n2:
    if n1 < n3:
        if n3 < n2:
            print(f"{n1} - {n3} - {n2}")
        else:
            print(f"{n1} - {n2} - {n3}")
    else:
        print(f"{n3} - {n1} - {n2}")
else:
    if n2 > n3:
        print(f"{n1} - {n2} - {n3}")
    else:
        print(f"{n2} - {n3} - {n1}")
