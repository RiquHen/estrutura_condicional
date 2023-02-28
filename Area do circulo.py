"""Faça um Programa que peça o raio de um círculo,
 calcule e mostre sua área."""

PI = 3.14
raio = float(input("Informe o raio do círculo(em cm): "))
area = PI * raio * raio # calculo da area do circulo
perimetro = 2 * PI * raio # calculo do perimetro
print(f"O circulo de raio {raio:.2f}cm tem o perimetro de {perimetro:.2f}cm")
print(f"O circulo de raio {raio}cm tem área igual a {area:.2f}cm²")