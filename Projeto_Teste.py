# Fatorial de um número
numero = 1
while numero >= 0:
  numero = int(input('Digite um numero para saber o seu fatorial: '))
  if numero > 0:
    fatorial = 1
    for item in range(1,numero +1):
      fatorial = fatorial * item
    print('O Fatorial de ',numero,'!: ',fatorial)
  elif numero == 0:
    fatorial  = 1
    print('O Fatorial de ',numero,'!: ',fatorial)
  elif numero == 1:
    fatorial  = 1
    print('O Fatorial de ',numero,'!: ',fatorial)
  else:
    print('Não existe Fatorial de número negativo')
