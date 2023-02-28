"""Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
download do arquivo usando este link (em minutos)."""

tam = float(input("Informe o tamanho do arquivo(em MB): "))
veldown = float(input("informe a velocidade de download(em Mbps): "))
veldowmin = veldown * 60
tempo = tam / veldowmin

print(f"O tempo de download é: {tempo:.0f} minutos")
print (f"{tempo}")
