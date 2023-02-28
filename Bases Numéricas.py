numero = int(input("Informe um número inteiro: "))
print("[1] Conversão para Binário\n[2] Conversão para Octal\n[3] Conversão para Hexadecimal")
opcao = int(input("Escolha a base desejada para conversão: "))
if(opcao == 1):
    print(f"O número {numero} em binário é igual a {bin(numero)[2:]}")
elif opcao ==2:
  print(f"O número {numero} em Octal é igual a {oct(numero)[2:]}")
elif(opcao == 3):
    print(f"O número {numero} em Hexadecimal é igual a {hex(numero)[2:]}")
else:
    print("Opção Invalida!!!")
