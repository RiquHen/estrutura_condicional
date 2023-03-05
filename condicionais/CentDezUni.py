"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade
 de centenas, dezenas e unidades do mesmo.
◦ Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
◦ 326 = 3 centenas, 2 dezenas e 6 unidades
◦ 12 = 1 dezena e 2 unidade
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""
nteste = [326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 , 16]
for i in range(0,18):
    u = nteste[i] % 10
    d = ((nteste[i] - u) /10) % 10
    c = (nteste[i] - (d*10+u)) / 100
    if c == 0:
        if d == 0:
            if u == 0:
                print(f"{nteste[i]} = {u} unidade")
            else:
                print(f"{nteste[i]} = {u} unidades")
        else:
            if d ==1:
                if u == 1:
                    print(f"{nteste[i]} = {d:.0f} dezena e {u} unidade")
                elif u == 0:
                    print(f"{nteste[i]} = {d:.0f} dezena")
                else:
                    print(f"{nteste[i]} = {d:.0f} dezena e {u} unidades")

            else:
                if u == 0:
                    print(f"{nteste[i]} = {d:.0f} dezenas")
                elif u ==1:
                    print(f"{nteste[i]} = {d:.0f} dezenas e {u} unidade")
                else:
                    print(f"{nteste[i]} = {d:.0f} dezenas e {u} unidades")
    else:
        if c == 1:
            if d == 0:
                if u == 0:
                    print(f"{nteste[i]} = {c:.0f} centena" )
                elif u == 1:
                    print(f"{nteste[i]} = {c:.0f} centena e {u} unidade")
                else:
                    print(f"{nteste[i]} = {c:.0f} centena ")

            elif d == 1:
                if u == 0:
                    print(f"{nteste[i]} = {c:.0f} centena, {d:.0f} dezena e {u} unidade")
                else:
                    print(f"{nteste[i]} = {c:.0f} centena, {d:.0f} dezena e {u} unidades")
            else:
                if u == 1:
                    print(f"{nteste[i]} = {c:.0f} centena, {d:.0f} dezenas, {u} unidade")
                else:
                    print(f"{nteste[i]} = {c:.0f} centena, {d:.0f} dezenas, {u} unidades")
        elif u > 1:
            if d == 0:
                if u == 0:
                    print(f"{nteste[i]} = {c:.0f} centena e {d:.0f} dezena")
                elif u == 1:
                    print(f"{nteste[i]} = {c:.0f} centena e {u} unidade")
                else:
                    print(f"{nteste[i]} = {c:.0f} centena e {u} unidades")

            elif d == 1:
                if u == 0:
                    print(f"{nteste[i]} = {c:.0f} centena e {d:.0f} dezena" )
                elif u ==1:
                    print(f"{nteste[i]} = {c:.0f} centena, {d:.0f} dezenas, {u} unidade")
                else:
                    print(f"{nteste[i]} = {c:.0f} centena, {d:.0f} dezena e {u} unidades")
            elif d > 1:
                if u == 0:
                    print(f"{nteste[i]} = {c:.0f} centena e {d:.0f} dezenas")
                elif u == 1:
                    print(f"{nteste[i]} = {c:.0f} centena, {d:.0f} dezenass, {u} unidade")
                else:
                    print(f"{nteste[i]} = {c:.0f} centena, {d:.0f} dezena e {u} unidades")