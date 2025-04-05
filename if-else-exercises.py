# 1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print(f"{num1} é maior que {num2}") 
else:
    print(f"{num2} é maior que {num1}")

# 2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
producao = float(input("Informe o percentual de crescimento de produção da empresa: "))
if producao > 0:
    print("A porcentagem é positiva!")
else:
    print("A porcentagem é negativa!")

# 3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
letra = input("Digite uma letra: ").strip().lower()
if letra in "aeiou":
    print(f"{letra} é uma vogal.")
else:
    print(f"{letra} é uma consoante.")

# 4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
valorCarro = float(input("Informe o valor médio do carro no 1° ano: "))
valorCarro2 = float(input("Informe o valor médio do carro no 2° ano: "))
valorCarro3 = float(input("Informe o valor médio do carro no 3° ano: "))
if valorCarro < valorCarro2 and valorCarro < valorCarro3:
    print(f"O carro 1 é o mais barato entre todos: R${valorCarro:.2f}")
elif valorCarro2 < valorCarro and valorCarro2 < valorCarro3:
    print(f"O carro 2 é o mais barato entre todos: R${valorCarro2:.2f}")
else:
    print(f"O carro 3 é o mais barato entre todos: R${valorCarro3:.2f}")

# 5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
produto = float(input("Informe o valor do 1° produto: "))
produto2 = float(input("Informe o valor do 2° produto: "))
produto3 = float(input("Informe o valor do 3° produto: "))
if produto < produto2 and produto < produto3:
    print(f"O produto 1 é o mais barato entre todos: R${produto:.2f}")
elif produto2 < produto and produto2 < produto3:
    print(f"O produto 2 é o mais barato entre todos: R${produto2:.2f}")
else:
    print(f"O produto 3 é o mais barato entre todos: R${produto3:.2f}")

# 6) Escreva um programa que leia três números e os exiba em ordem decrescente.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
if (num1 != maior and num1 != menor):
   meio = num1
elif (num2 != maior and num2 != menor):
   meio = num2
else:
    meio = num3
print(f"Ordem decrescente: {maior}, {meio}, {menor}")

# 7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
turno = input("Informe o turno em que você estuda (manhã, tarde ou noite): ").strip().lower()
if turno == "manhã":
    print("Bom dia!")
elif turno == "tarde":
    print("Boa tarde!")
elif turno == "noite":
    print("Boa noite!")
else:
    print("Turno inválido!")

# 8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
numInt = int(input("Digite um número inteiro: "))
if numInt % 2 == 0:
    print(f"{numInt} é par.")
else:
    print(f"{numInt} é ímpar.")

# 9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
numero = float(input("Digite um número: "))
if numero.is_integer():
    print(f"{numero} é um número inteiro.")
else:
    print(f"{numero} é um número decimal.")

# 10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação desejada (+, -, *, /): ")
if op == "+":
    print(f"A soma de {n1} e {n2} é: {n1 + n2}")
elif op == "-":
    print(f"A subtração de {n1} e {n2} é: {n1 - n2}")
elif op == "*":
    print(f"A multiplicação de {n1} e {n2} é: {n1 * n2}")
elif op == "/":
    if n2 != 0:
        print(f"A divisão de {n1} e {n2} é: {n1 / n2}")
    else:
        print("Divisão por zero não é permitida.")

# 11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:
l1 = float(input("Digite o primeiro lado do triângulo: "))
l2 = float(input("Digite o segundo lado do triângulo: "))
l3 = float(input("Digite o terceiro lado do triângulo: "))
if l1 == l2 and l2 == l3:
    print("O triângulo é equilátero.")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")

# 12) Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:
# O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
# O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
diesel = 2.00
etanol = 1.70
qtdBrL = float(input("Informe a quantidade de litros de combustível: "))
combustivel = input("Informe o tipo de combustível (E para etanol ou D para diesel): ").strip().lower()
if combustivel == "e":
    if qtdBrL <= 15:
        desconto = 0.02
    else:
        desconto = 0.04
    valorTotal = (etanol * qtdBrL) - (etanol * qtdBrL * desconto)
    print(f"Valor a ser pago: R$ {valorTotal:.2f}")
elif combustivel == "d":
    if qtdBrL <= 15:
        desconto = 0.03
    else:
        desconto = 0.05
        valorTotal = (diesel * qtdBrL) - (diesel * qtdBrL * desconto)
    print(f"Valor a ser pago: R$ {valorTotal:.2f}")

# 13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:
# Para variação acima de 20%: bonificação para o time de vendas.
# Para variação entre 2% e 20%: pequena bonificação para time de vendas.
# Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
# Para bonificações abaixo de -10%: corte de gastos.
vendas2022 = float(input("Informe o valor das vendas de 2022: "))
vendas2023 = float(input("Informe o valor das vendas de 2023: "))
variacaoPercentual = ((vendas2023 - vendas2022) / vendas2022) * 100
if variacaoPercentual > 20:
    print("Haverá bonificação para o time de vendas!")
elif variacaoPercentual >= 2 and variacaoPercentual <= 20:
    print("Haverá uma pequena bonificação para time de vendas!")
elif variacaoPercentual <= 2 and variacaoPercentual <= -10:
    print("Haverá um planejamento de políticas de incentivo às vendas.")
elif variacaoPercentual < -10:
    print("Haverá corte de gastos.")