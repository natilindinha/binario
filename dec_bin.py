def transformando_em_binario():
  import math
  #define uma variavel 
  par = ''
  x = float(input('digite um número: '))#pede o numero a ser transformado
  #estrutura de repeticao para ate que o numero seja maior que 0
  while x > 0:
    #estrutura para definir se o proximo numero em binario eh 0 ou 1
    if x % 2 == 0:
      par = '0' + str(par)#salva o 0 na variavel, depois dos numeros ja existentes ali
      x = x / 2 #transorma o x em seu proximo numero para ser calculado
    else:
      par = '1' + str(par)#salva o 1 na variavel, depois dos numeros ja existentes ali
      x = x / 2#transorma o x em seu proximo numero para ser calculado
      x = math.trunc(x)#faz ser inteiro, aredonda.
  print(par)
transformando_em_binario()
