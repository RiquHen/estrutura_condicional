

""" Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
◦ "Telefonou para a vítima?"    ◦ "Esteve no local do crime?"
◦ "Mora perto da vítima?"       ◦ "Devia para a vítima?"    ◦ "Já trabalhou com a vítima?
"O programa deve no final emitir uma classificação
 sobre a participação da pessoa no crime. Se a pessoa responder positivamente
 a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
 e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

tel = str(input("Telefonou para vítima? ")).strip().upper()
loc = str(input("Esteve no local do crime? ")).strip().upper()
mora = str(input("Mora perto da vítima? ")).strip().upper()
deve = str(input("Devia dinheiro a vítima? ")).strip().upper()
trab = str(input("Já trabalhou com a vítima? ")).strip().upper()
c = 0
if tel == "SIM" or tel == "S":
    c += 1
if loc == "SIM" or loc == "S":
    c += 1
if mora == "SIM" or mora == "S":
    c += 1
if deve == "SIM" or deve =="S":
    c += 1
if trab == "SIM" or trab == "S":
    c += 1

if c == 2:
    print ("Pessoa suspeita!")
elif c == 3 or c == 4:
    print("Provável Cúmplice!")
elif c == 5:
    print("Culpado")
