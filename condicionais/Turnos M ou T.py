"""Faça um Programa que pergunte em que turno você estuda.
 Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
 Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

print(30*"=" + "\nM - Matutino\nV - Vespertino\nN - Noturno\n"+ 30*"=")
turno = str(input("Em que turno você estuda?: ")).strip().upper()

if turno == "M":
    print("Bom Dia!!!")
elif turno == "V":
    print("Boa Tarde!!!")
elif turno == "N":
    print("Boa Noite!!!")
else:
    print("Valor inválido!!!")