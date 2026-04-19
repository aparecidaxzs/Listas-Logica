#inicio da questão 01
value_a = int(input("Digite um valor: "))
value_b = int(input("Digite outro valor: "))

print(f"{value_a} + {value_b} → {value_a + value_b}")
print(f"{value_a} - {value_b} → {value_a - value_b}")
print(f"{value_a} * {value_b} → {value_a * value_b}")
print(f"{value_a} / {value_b} → {value_a // value_b}")

#fim da questão 01

#inicio da questão 02
print("")
temperatura = int(input("Digite a temperatura em graus Celsius: "))
print(f"Convertendo para Fahrenheit: {temperatura}℃  * 1.8 + 32")
print(f"Resultado: {temperatura}℃  = {(temperatura * 1.8) + 32 }℉")

#fim da questão 02

#inicio da questão 03
print("")
raio = int(input("Digite o raio do circulo: "))
print(f"{(raio * raio) + 3.14}")

#fim da questão 03


#inicio da questão 04
print("")
base = int(input("Digite a base do triângulo: "))
altura = int(input("Digite a altura do triângulo: "))

print(f"A área do triângulo é: {base * altura}")

#fim da questão 04

#inicio da questão 05
print("")
raio = float(input("Digite o raio da esfera: "))

print(f"Volume da esfera: {4/3 * 3.14 * (raio ** 3)}")

#fim da questão 05

#inicio da questão 06
print("")
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a terceira nota: "))

print(f"As três notas são: {nota1}, {nota2}, {nota3}")
print(f"A média entre as 3 notas são: {(nota1 + nota2 + nota3)//3}")

#fim da questão 06

#inicio da questão 07
print("")
peso1 = int(input("Insira a nota e em seguida o peso: "))
media1 = int(input())
peso2 = int(input("Insira a segunda nota e em seguida o peso: "))
media2 = int(input())
peso3 = int(input("Insira a terceira nota e em seguida o peso: "))
media3 = int(input())

print(f"Resultado: {((media1*peso1) + (media2*peso2) + (media3*peso3))//3}")

#fim da questão 07

#inicio da questão 08
print("")
valor_a = int(input("Digite o valor de A: "))
valor_b = int(input("Digite o valor de B: "))
valor_c = int(input("Digite o valor de C: "))
valor_x = int(input("Digite o valor de X: "))
print(f"Calculando a expressão: {valor_a} * ({valor_x} ** 2) + {valor_b} * {valor_x} + {valor_c}")
print(f"Y= {(valor_a * (valor_x ** 2)) + (valor_b * valor_x) + valor_c}")

#fim da questão 08

#inicio da questão 09
print("")
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
print(f"Calculando o IMC: {peso} / ({altura} * {altura})")
print(f"IMC: {peso / (altura * altura)}")
#fim da questão 09

#inicio da questão 10
print("")
tabuada = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada do {tabuada}:")
print(f"{tabuada} x 1 = {tabuada * 1}")
print(f"{tabuada} x 2 = {tabuada * 2}")
print(f"{tabuada} x 3 = {tabuada * 3}")
print(f"{tabuada} x 4 = {tabuada * 4}")
print(f"{tabuada} x 5 = {tabuada * 5}")
print(f"{tabuada} x 6 = {tabuada * 6}")
print(f"{tabuada} x 7 = {tabuada * 7}")
print(f"{tabuada} x 8 = {tabuada * 8}")
print(f"{tabuada} x 9 = {tabuada * 9}")
print(f"{tabuada} x 10 = {tabuada * 10}")
#fim da questão 10

#inicio da questão 11
print("")
segundos = int(input("Digite o número de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{segundos} segundos equivalem a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
#fim da questão 11
