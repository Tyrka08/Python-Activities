#Exercício 1: Saudação Simples - Crie um programa que peça ao usuário para inserir seu nome e, em seguida, exiba uma saudação personalizada.

nome = input("insira seu nome: ")
print("olá " + nome + "!")

#Exercício 2: Calculadora de Idade - Peça ao usuário para inserir seu ano denascimento e, em seguida, calcule e exiba a idade atual.

data = int(input("insira sua data de nascimento: "))
print(f'voce tem {2023 - data} anos')

#Exercício 3: Troca de Variáveis - Crie um programa que troque os valores de duasvariáveis. Por exemplo, se a for 5 e b for 10, o programa deve fazer com que a seja 10 e b seja 5.

a = 5
b = 10

print("Valores originais: a =", a, "b =", b)

temp = a
a = b
b = temp

print("Valores trocados: a =", a, "b =", b)

#Exercício 4: Verificador de Par ou Ímpar - Peça ao usuário para inserir um número e, em seguida, determine se é par ou ímpar.
  
valor = int(input("insira o valor: "))
if valor %2 == 0:
  print( valor , "é par")
else:
  print( valor , "é impar")

#Exercício 5: Calculadora de Área de Retângulo - Peça ao usuário para inserir a largura e a altura de um retângulo e, em seguida, calcule e exiba a área

base = float(input('Digite o valor da largura: '))
altura = float(input('Digite o valor da altura: '))
area = base * altura
print(f'A área do retangulo é: {area:.2f} metros² ')


#Exercício 6: Conversor de Moeda - Crie um programa que converta um valor em reais para dólares. Peça ao usuário para inserir o valor em reais e, em seguida, exiba o valor equivalente em dólares (considere uma taxa de conversão fixa).

valorreal = float(input('Digite o valor em real: '))
valorconversão = 4.97
valordolar = valorreal / valorconversão
print(f'O valor da conversão de reais pra dolar é: {valordolar:.2f}')

#Exercício 7: Contador de Dígitos - Peça ao usuário para inserir um número inteiro e conte quantos dígitos ele possui.

numero = int(input('Digite um numero inteiro: '))
contador = 0
print(len(numero))
while numero != 0:
 numero //= 10
 contador += 1
print(contador)

#Exercício 8: Média de Notas - Peça ao usuário para inserir três notas e, em seguida, calcule e exiba a média dessas notas

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))

media = (nota1 + nota2 + nota3)/3

if media >= 6:
  print(f'você passou por {media:.2f}')
else:
  print(f'você não passou, a média é de 6 e você tirou {media:.2f}')

#Exercício 9: Verificador de Vogal - Peça ao usuário para inserir uma letra e determine se é uma vogal ou não.

letra = str(input('qual a letra que ocê deseja? '))

if letra.upper() in "AEIOU":
  print(f'{letra} é uma vogal')
else:
  print(f'{letra} é uma consoante')

#Exercício 10: Calculadora de IMC - Peça ao usuário para inserir sua altura (em metros) e peso (em kg) e, em seguida, calcule e exiba o Índice de Massa Corporal (IMC).

peso = float(input('digite seu peso em quilos: '))
altura = float(input('digite sua altura em metros: '))

IMC = peso / (altura**2)

if IMC<17:
  print(f'seu IMC é {IMC:.2f} e muito abaixo do peso')

elif 17<=IMC<18.49:
  print(f'seu IMC é {IMC:.2f} e abaixo do peso')

elif 18.50<=IMC<24.99:
  print(f'seu IMC é {IMC:.2f} e peso normal')

elif 25<=IMC<29.99:
  print(f'seu IMC é {IMC:.2f} e acima do peso')

elif 30<=IMC<34.99:
  print(f'seu IMC é {IMC:.2f} e obesidase I')

elif 35<=IMC<=39.99:
  print(f'seu IMC é {IMC:.2f} e obesidade II')

elif IMC>=40:
  print(f'seu IMC é {IMC:.2f} e obesidade III')
  
  
  
  
  





