from random import randint
from time import sleep
print('---' * 20)
print('>>> \033[33mJOGO DE AVENTURA\033[m <<<')
print('---' * 10)
print('=== \033[31mMISSÃO\033[m ====')
print('''\033[1mSalvar o item precioso do Castelo Verde, para isso é necessário derrotar alguns mostros para chegar até lá! Boa sorte!!!\033[m''')
nome = str(input('\033[34mNome do Jogador:  \033[m')).strip()
print('INICIANDO JOGO...')
sleep(2)
print(f'{nome} inicia com 20 HP')
print('{}, você está na frente do Castelo Verde...'.format(nome))
print('Um monstro se aproxima... Se prepare!!')
vida_heroi = 20
vida_monstro = 20
while (vida_heroi > 0) or (vida_monstro > 0):
    computador = randint(0, 2)
    print('''\033[1;35mOPCOES DE BATALHA\033[m
    \033[1m[ 0 ] lutar
    [ 1 ] defender
    [ 2 ] fugir \033[m''')
    opcoes = int(input('Escolha sua jogada:  '))
    print('-=-' * 20)
    if opcoes == 0:
        if computador == 0:
            print('Monstro tem 20 HP')
            print(f'\033[1m{nome} ataca, e ao mesmo tempo o monstro tenta atacar também. Os dois levam 10 de dano!\033[m')
        elif computador == 1:
            print(f'\033[1m{nome} ataca, mas o monstro se defende. Zero de dano.\033[m')
        elif computador == 2:
            print(f'\033[1m{nome} tenta atacar, mas monstro sai correndo e foge da luta!\033[m')
            break
    elif opcoes == 1:
        if computador == 0:
            print(f'\033[1mMonstro ataca, mas {nome} consegue se defender. Zero de dano!\033[m')
        elif computador == 1:
            print(f'\033[1mTanto {nome} como o monstro se esquivam para se defender, mas ninguém acaba atacando!\033[m')
        elif computador == 2:
            print(f'\033[1m{nome} pensa em se defender, achando que o monstro irá atacar, mas ele corre e foge da batalha!\033[m')
            break
    elif opcoes == 2:
        if computador == 0:
            print(f'\033[1mMonstro se prepara para atacar, mas {nome} corre e consegue fugir com sucesso!\033[m')
            break
        elif computador == 1:
            print(f'\033[1mMonstro estranha movimento e tenta se defender, e com isso não percebe que {nome} correu e conseguiu fugir da batalha!\033[m')
            break
        elif computador == 2:
            print(f'\033[1mTanto {nome} como o monstro se assustam com seus próprios movimentos e fogem da batalha!\033[m')
            break
print('-=-' * 20)
print('\033[31mFIM DA BATALHA!!\033[m')