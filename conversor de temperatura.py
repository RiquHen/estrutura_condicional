""" Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
        ◦ C = 5 * ((F-32) / 9)."""

print("*"*10 + " Conversor de temperatura " + "*" *10)
while True:
    print("=" * 30 + "\n[1] Celsius para Fahrenheit \n[2] Fahrenheit para Celsius\n" + "*" * 45)
    opcao = int(input("Escolha a opção desejada[0 para sair]: "))
    temp = float(input("Escolha a temperatura(Celsius ou Fahrenheit): "))
    if opcao == 1:
        tc = temp
        tf = 9 * tc / 5 + 32
        print(f"Temperatura {tc} em Celsius equivale a {tf:.1f} graus Fahrenheit")
    elif opcao == 0:
        print("*"*45+"\nObrigado por usar o conversor de temperatura!!!")
        break
    elif opcao == 2:
        tf = temp
        tc = 5 * (tf-32)/9
        print(f"Temperatura {tf} em Fahrenheit equivale a {tc:.1f} Celsius ")
    else:
        print( "-="*30 + "\nOpção inválida. Informe novamente a temperatura!!!")
