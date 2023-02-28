"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

sexo =  str(input("Informe a letra inicial do seu sexo: "))
if (sexo == 'F') or (sexo == 'f'):
    print("Sexo Feminino!")
elif(sexo == "M") or (sexo == 'm'):
    print(" Sexo Masculino!")
else:
    print("Sexo inválido!!!")