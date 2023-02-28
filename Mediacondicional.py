"""    14. Faça um programa que lê as duas notas parciais obtidas por um aluno
 numa disciplina ao longo de um semestre, e calcule a sua média.
  A atribuição de conceitos obedece à tabela abaixo:
◦ Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C"""
np1 = float(input("Primeira Nota: "))
np2 = float(input("Segunda Nota: "))
m = (np1 + np2) / 2
if m < 4:
    c = "E"
elif 4 <= m < 6:
    c = "D"
elif 6 <= m < 7.5:
    c = "C"
elif 7.5 <= m < 9:
    c = "B"
elif m >= 9:
    c = "A"

if c == "A" or c == "B" or c == "C":
    sit = "Aprovado!"
else:
    sit = "Reprovado!!!"
""" O algoritmo deve mostrar na tela as notas, a média, 
  o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou 
  “REPROVADO” se o conceito for D ou E."""
print(30 * "=")
print(f"1ª Nota: {np1}\n2ª Nota: {np2}")
print(30 * "=")
print(f"Média: {m:.1f}\nConceito: {c}\nSituação: {sit}")
