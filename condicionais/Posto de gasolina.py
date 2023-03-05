"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
◦ Álcool:       ◦ até 20 litros, desconto de 3% por litro
◦ acima de 20 litros, desconto de 5% por litro
◦ Gasolina:     ◦ até 20 litros, desconto de 4% por litro
◦ acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos,o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor
a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50
o preço do litro do álcool é R$ 1,90."""

litro_alcool: float = 2.5
litro_gasolina = 1.9
valor = desc = 0
print(20*"==" +
      "\nInforme o tipo de combustível \n\t[A] - Álcool \n\t[G] - Gasolina\n"+20*"==")
tipo = str(input("Qual o tipo de combustível? ")).strip().upper()
quantia = int(input("Informe a quantidade adquirida: "))
if tipo == "A":
    total = quantia * litro_alcool
    tipo = "álcool"
    if quantia >= 20:
        desc = total * 0.03
        valor = total - desc
    else:
        desc = total * 0.05
        valor = total - desc
    print(40 * "=")
    print(
        f"Quantidade: {quantia} litros.\nCombustivel: {tipo}\nTotal: R$ {total:.2f}  \nDesconto:R$ {desc:.2f}")
    print(40 * "=")
    print(
        f"O valor a ser pago por {quantia} litros de {tipo} é: R$ {valor:.2f}")
elif tipo == "G":
    total = quantia * litro_gasolina
    tipo = "gasolina"
    if quantia < 20:
        desc = total * 0.04
        valor = total - desc
    else:
        desc = total * 0.06
        valor = total - desc
    print(40*"=")
    print(
        f"Quantidade: {quantia} litros.\nCombustivel: {tipo}\nTotal: R$ {total:.2f} \nDesconto:R$ {desc:.2f}")
    print(40*"=")
    print(
        f"O valor a ser pago por {quantia} litros de {tipo} é: R$ {valor:.2f}")
