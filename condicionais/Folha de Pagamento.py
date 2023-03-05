"""Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
◦ Desconto do IR:
◦ Salário Bruto até 900 (inclusive) - isento
◦ Salário Bruto até 1500 (inclusive) - desconto de 5%
◦ Salário Bruto até 2500 (inclusive) - desconto de 10%
◦ Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220."""
import os

sin = 3
inss = 10
fgts = 11
hora = float(input("Informe o valor da hora: "))
qhora = float(input("Indique a quantidade de horas trabalhadas: "))

print(20 * "==")
print(
    f"Valor da hora trabalhada: R$ {hora:.2f}\nQuantidade de Horas trabalhadas: {qhora:.0f}" + " horas")
print(20 * "==")
sbruto = hora * qhora
if sbruto <= 900:
    ir = 0
elif sbruto <= 1500:
    ir = 5
elif sbruto <= 2500:
    ir = 10
else:
    ir = 20
dir = sbruto * ir / 100
dinss = sbruto * inss / 100
vfgts = sbruto * fgts / 100
os.system('cls')
print(f"{'-'*40}\n{'CÁLCULO DE FOLHA DE PAGAMENTO':^40}")
print(f"{'-'*40}\n{'Salário bruto::':<20} R$ {sbruto:>7.2f}")
print(f"{'(-) IR ('}{ir}{'%):':<10} R$ {dir:>7.2f}")
print(f"{'(-) INSS ('}{inss}{'%):':<8} R$ {dinss:>7.2f}")
print(f"{'FGTS ('}{fgts}{'%):':<12} R$ {vfgts:>7.2f}")
desc = dinss + dir
print(f"{'Total de descontos:':<20} R$ {desc:>7.2f}")
print(f"{'Salario líquido:':<20} R$ {sbruto - desc:>7.2f}")
print(20 * "==")
