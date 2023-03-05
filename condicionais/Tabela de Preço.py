"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
◦                   Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)de maças adquiridas e escreva o valor a ser pago pelo cliente."""

print(f"{'Até 5 kg':>25}{'Acima de 5 kg':>25}")
print(f"Morango {'R$ 2.50 por kg':>19}{'R$ 2.20 por kg':>23}")
print(f"Maçã {'R$ 1,80 por Kg':>22}{'R$ 1,50 por Kg':>23}")
p_morango = p_maca = 0
morango_kg = float(input("Quantos quilos de morango? "))
maca_kg = float(input("Quantos quilos de maçã? "))
print(30*"=")
if morango_kg >= 5:
    p_morango = 2.5
elif morango_kg < 5:
    p_morango = 2.2
if maca_kg >= 5:
    p_maca = 1.8
elif maca_kg:
    p_maca = 1.5
peso_total = maca_kg + morango_kg
valor_compras = (morango_kg * p_morango) + (maca_kg * p_maca)
desconto = 0
print(f'Valor total: R$ {valor_compras:.2f}')
if peso_total > 8 or valor_compras > 25:
    desconto = 0.01
    valor_compras -= (valor_compras * desconto)
print(f"peso total: {peso_total} kg\ndesconto: R$ {desconto*valor_compras:.2f}\nTotal a pagar: R$ {valor_compras:.2f}")
