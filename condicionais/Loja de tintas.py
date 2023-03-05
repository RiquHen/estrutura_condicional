"""O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    ◦ Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    ◦ comprar apenas latas de 18 litros;
    ◦ comprar apenas galões de 3,6 litros;
    ◦ misturar latas e galões, de forma que o desperdício de tinta seja menor.Acrescente 10% de folga e
    sempre arredonde os valores para cima, isto é, considere latas cheias."""
import math

litro = 6  # 6 metros quadrados
lata = 18  # 18 litros
galao = 3.6  # litros
valorlata = 80  # reais
valorgalao = 25  # reais

alata = lata * litro
agalao = galao * litro

area = float(input("Informe a area a ser pintada[em metros]: "))
nlata = math.ceil(area/alata)
ngalao = math.ceil(area/agalao)
# Se comprado apenas latas de 18 litros
print(f"Será necessario {nlata:.0f} latas, no valor de R$ {nlata * valorlata:.2f} para pintar {area:.2f} m²")
# Se comprar apenas galóes de 3,6 litros
print(f"Será necessário {ngalao:.0f} galóes, no valor de R$ {ngalao * valorgalao:.2f} para pintar {area:.2f} m²")

area = area + (area * 0.1)
nlata = ngalao = 0
if area % alata != 1:
    nlata = int(area/ alata)
area = area - (nlata * alata)
ngalao = math.ceil(area/agalao)
# caso mesclar a compra, entre galões e latas
print(f"Será necessário {nlata} latas e {ngalao:.0f} galoes")
print(f"Sendo o valor total: R$ {((nlata * valorlata) +(ngalao * valorgalao)):.2f}")
