"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""
from random import randint
from time import sleep
megasena = []
print('-=-'*8, 'MEGASENA', '-=-'*8)
print('Seja bem vindo! Vou te ajudar a preencher sua Mega Sena!')
jogos = int(input('Números de jogos que deseja: '))
for n in range(jogos):
    quant = []
    while len(quant) < 6:
        r = randint(1, 60)
        if r not in quant:
            quant.append(r)
    quant.sort()
    megasena.append(quant[:])
print('PROCESSANDO....')
for m in megasena:
    sleep(0.5)
    print(f'{m}')
sleep(0.2)
print('-=-'*8, 'BOA SORTE', '-=-'*8)
