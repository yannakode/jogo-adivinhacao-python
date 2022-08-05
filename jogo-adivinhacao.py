import random
erros=0
jogador=int(input('Digite um número: '))
sorteado=random.randrange(0,10)
while(jogador!=sorteado):
 if (jogador>sorteado):
  print('Errou! o número é menor')
 else:
  print('Errou! o número é menor')
 erros+=1
 jogador=int(input('Digite um número: '))

print('acerrou! O número sorteado era: ',sorteado, 'vc acertou depois de ',erros)
  
