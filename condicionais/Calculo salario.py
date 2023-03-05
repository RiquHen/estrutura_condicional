hora = float(input("Valor recebido por hora: "))
num_hora = int(input("Quantidade de horas trabalhadas(mensal):"))
salario_bruto = num_hora * hora
ir= salario_bruto * 0.11  # imposto de renda
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = ir+inss+sindicato
print("="*30)
print(f"Salário Bruto: R$ {salario_bruto:.2f}.")
print("="*30)
print("DESCONTOS")
print(f"Imposto de Renda: R$ {ir:.2f}.")
print(f"Contribuição INSS: R$ {inss:.2f}.")
print(f"Sindicato: R% {sindicato:.2f}.")
print("="*30)
print(f"O desconto total: R$ {descontos:.2f}.")
print("="*30)
print(f"Salário líquido: R$ {salario_bruto - (descontos):.2f}")
