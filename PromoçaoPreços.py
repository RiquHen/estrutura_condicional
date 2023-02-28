"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                    Acima de 5 Kg           Até 5 Kg
File Duplo      R$ 4,90 por kg          R$ 5,80 por kg
Alcatra         R$ 5,90 por kg          R$ 6,80 por kg
Picanha         R$ 6,90 por kg          R$ 7,80 por kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade
de carne,preço total, tipo de pagamento, valor do desconto e valor a pagar."""
print(f"{70*'-'}\n{'Tabela de Preços - Promoção de carnes':^55}\n{70*'='}")
print(f"{'Acima de 5 kg':>37} {'Até 5 kg':>17}")
print(f"[1] - File Duplo {'R$ 4,90 por Kg':>20} {'R$ 5,80 por Kg':>20}")
print(f"[2] - Alcatra {'R$ 5,90 por Kg':>23} {'R$ 6,80 por Kg':>20}")
print(f"[3] - Picanha {'R$ 6,90 por Kg':>23} {'R$ 7,80 por Kg':>20} \n{70*'-'}")
print(f"Comprando com o cartão Tabajara 5% de desconto no total da compra!\n{70*'-'}")
pagar = valor = 0
tipo = int(input("Código do tipo: "))
peso = float(input("Informe o quantidade(peso): "))
pag = int(input(f"{70*'-'}\nInforme a forma de pagamento[digite (1) para cartão]: "))

if peso > 5:
    p_file = 4.9
    p_alcatra = 5.9
    p_picanha = 6.9
elif peso < 0:
    print("Peso Inválido!!!")
elif peso <= 5:
    p_file = 5.8
    p_alcatra = 6.8
    p_picanha = 7.8

if tipo == 1:
    tipo = "Filé Duplo"
    valor = peso * p_file
elif tipo == 2:
    tipo = "Alcatra"
    valor = peso * p_alcatra
elif tipo == 3:
    tipo = "Picanha"
    valor = peso * p_picanha

if pag == 1:
    desc = 5
    pagar = valor - (valor * desc / 100)
    pag = "Cartão"
else:
    desc = 0
    pag = "Dinheiro"
    pagar = valor

print(f"{30*'-'}\n{'CUPOM FISCAL':^35}\n{30*'='}")
print(f"Tipo: {tipo}.\nQuantidade: {peso} kG\nValor Total: R$ {valor:.2f}")
if desc != 0:
    desconto = (valor * desc / 100)
    print(f"Tipo de pagamento: {pag}\nDesconto: ({desc}%) - R$ {desconto:.2f}")
else:
    print(f"Tipo de pagamento: {pag}\nDesconto: ({desc}%) - R$ 0,00")
print(f"{30*'-'}\nTotal a pagar: R$ {pagar:.2f}\n{30*'='}")

