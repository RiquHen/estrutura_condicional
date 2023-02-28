"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
 lhe contraram para desenvolver o programa que calculará os reajustes.
    ◦ Faça um programa que recebe o salário de um colaborador e
     o reajuste segundo o seguinte critério, baseado no salário atual:
    ◦ salários até R$ 280,00 (incluindo) : aumento de 20%
    ◦ salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    ◦ salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    ◦ salários de R$ 1500,00 em diante : aumento de 5%Após o aumento ser realizado, informe na tela:
    ◦ o salário antes do reajuste;
    ◦ o percentual de aumento aplicado;
    ◦ o valor do aumento;
    ◦ o novo salário, após o aumento."""
print(30 * "==")
print("Calculo do Aumento salário d um claborador de acordo comseu salário atual")
print(30 * "==")
st =float(input("Informe o salário atual do trabalhador: "))
if st < 280:
    reajuste = "20%"
    aumento = st * 0.2
    nst = st + aumento
elif 280 <= st < 700:
    reajuste = "15%"
    nst = st + (st * 0.15)
    aumento = st * 0.15
    nst = st + aumento
elif 700 <= st < 1500:
    reajuste = "10%"
    nst = st + (st * 0.1)
    aumento = st * 0.1
    nst = st + aumento
else:
    reajuste = "5%"
    nst = st + (st * 0.05)
    aumento = st * 0.05
    nst = st + aumento
print(30 * "==")
print(f"Salário Atual: R$ {st:.2f} \nReajuste: {reajuste} \nAumento: R$ {aumento:.2f} \nNovo Salário: R$ {nst:.2f}")
print(30 * "==")
