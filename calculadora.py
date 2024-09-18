# -*- coding: utf-8 -*-
"""projeto1EBAC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RiLzJGiz_utgankunZ0W6hRx3A2ZQp3d
"""

while True:
  try:
    option = int(input ('Bem vindo! Escolha a operação desejada!\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n'))

    if option < 1 or option >4:
      raise ValueError('Opção inválida! Escolha um número de 1 a 4!')

  except ValueError:
    print ('Opção inválida! Tente novamente!')

  else:
    break


match int(option):

  case 1:
    while True:
      try:
        num1 = int(input ('Insira o primeiro número! '))
      except ValueError:
          print ('Por favor, insira um número!')
      else:
          break
    while True:
      try:
        num2 = int(input ('Agora, insira o segundo número! '))
      except ValueError:
          print ('Por favor, insira um número!')
      else:
          break

    soma = num1 + num2
    print ('A soma dos números inseridos é:', soma)

  case 2:
    while True:
      try:
        sub1 = int(input ('Insira o primeiro número!'))
      except ValueError:
          print ('Por favor, insira um número!')
      else:
          break
    while True:
      try:
        sub2 = int(input ('Agora, insira o segundo número! '))
      except ValueError:
          print ('Por favor, insira um número!')
      else:
          break

    subtracao = sub1 - sub2
    print ('A diferença dos números inseridos é:', subtracao)

  case 3:
    while True:
      try:
        div1 = float(input ('Insira o primeiro número! '))
      except ValueError:
          print ('Por favor, insira um número!')
      else:
          break
    while True:
      try:
        div2 = float(input ('Agora, insira o segundo número! '))
      except ValueError:
          print ('Por favor, insira um número!')
      else:
          break
    divisao = div1 / div2
    print ('O quociente dos números inseridos é:', divisao)

  case 4:
    while True:
      try:
        multi1 = int(input ('Insira o primeiro número! '))
      except ValueError:
          print ('Por favor, insira um número!')
      else:
          break
    while True:
      try:
        multi2 = int(input ('Agora, insira o segundo número! '))
      except ValueError:
          print ('Por favor, insira um número!')
      else:
          break

    multiplica = multi1 * multi2
    print ('O produto dos números inseridos é:', multiplica)