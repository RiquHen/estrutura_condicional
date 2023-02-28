produto1 = float(input("Informe o preço do 1º produto: "))
produto2 = float(input("Informe o preço do 2º produto: "))
produto3 = float(input("Informe o preço do 3º produto: "))

if produto1 > produto2:
    if produto2 > produto3:
        menor = produto3
        p = "produto3"
    else:
        menor = produto2
        p = "produto2"
else:
    if produto1 > produto3:
        menor = produto3
        p = "produto3"
    else:
        menor = produto1
        p = "produto1"
print(20*"*")
print(f"Valor do primeiro produto: R$ {produto1}")
print(f"Valor do segundo produto:  R$ {produto2}")
print(f"Valor do terceiro produto: R$ {produto3}")
print(20*"*")
print(f"O produto mais barato é o {p} no valor de R$ {menor:.2f}")
