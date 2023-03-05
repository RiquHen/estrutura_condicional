"""    12. Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
        ◦ Para homens: (72.7*h) - 58        ◦ Para mulheres: (62.1*h) - 44.7"""

print("*" * 30 + "\n Cálculo do peso ideal")

while True:
    opcao = str(input("*" * 30 + "\nDeseja calcular seu peso ideal? (S/N): ")).strip().upper()[0]
    if opcao == "S":
        altura = int(input("Informe a sua altura(em cm): "))
        altura /=100
        sexo = str(input("Informe seu sexo(m ou f): ")).strip().upper()[0]
        if sexo == "F":
            peso_ideal = (62.1 * altura) - 44.7
            print("*" * 30 + f"\nSeu peso ideal é: {peso_ideal:.2f} Kg")
        elif sexo == "M":
            peso_ideal = (72.7 * altura) - 58
            print("*" * 30 + f"\nSeu peso ideal é: {peso_ideal:.2f} Kg")
        else:
            print("Sexo informado é invalido")
            sexo = str(input("Informe seu sexo: ")).strip().upper()[0]
    else:
        print("Obrigado por utilizar a calculadora de peso ideal!!!")
        break
