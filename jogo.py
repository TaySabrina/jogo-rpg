from random import randint
from time import sleep
computador = randint(0, 2)
print('---' * 20)
print('>>> \033[33mJOGO DE AVENTURA\033[m <<<')
print('---' * 10)
print('=== \033[31mMISSÃO\033[m ====')
print('''\033[1mObjetivo: Salvar o item precioso do Castelo Verde, para isso é necessário derrotar alguns mostros para chegar até lá! Boa sorte!!!\033[m''')
nome = str(input('\033[34mNome do Jogador:  \033[m')).strip()
print('INICIANDO JOGO...')
sleep(2)
print('{}, você está na frente do Castelo Verde...'.format(nome))
print('Um monstro se aproxima... Se prepare!!')
print('''OPCOES DE BATALHA
[ 0 ] lutar
[ 1 ] defender
[ 2 ] fugir ''')
opcoes = int(input('Escolha sua jogada:  '))
print('-=-' * 20)
if opcoes == 0:
    if computador == 0:
        print('\033[1m{} ataca, e ao mesmo tempo o monstro tenta de atacar também. Os dois levam 10 de dano!\033[m'.format(nome))
    elif computador  == 1:
        print('\033[1m{} ataca, mas o monstro se defende. Zero de dano.\033[m'.format(nome))
    elif computador == 2:
        print('\033[1m{} tenta atacar, mas monstro sai correndo e foge da luta!\033[m'.format(nome))
elif opcoes == 1:
    if computador == 0:
        print('\033[1mMonstro ataca, mas {} consegue se defender. Zero de dano!\033[m'.format(nome))
    elif computador == 1:
        print('\033[1mTanto {} como o monstro se esquivam para se defender, mas ninguém acaba atacando!\033[m'.format(nome))
    elif computador == 2:
        print('\033[1m{} pensa em se defender, achando que o monstro irá atacar, mas ele corre e foge da batalha!\033[m'.format(nome))
elif opcoes == 2:
    if computador == 0:
        print('\033[1mMonstro se prepara para atacar, mas {} corre e consegue fugir com sucesso!\033[m'.format(nome))
    elif computador == 1:
        print('\033[1mMonstro estranha movimento e tenta se defender, e com isso não percebe que {} correu e conseguiu fugir da batalha!\033[m'.format(nome))
    elif computador == 2:
        print('\033[1mTanto {} como o monstro se assustam com seus próprios movimentos e fogem da batalha!\033[m'.format(nome))
print('-=-' * 20)
print('\033[31mFIM DA BATALHA!!\033[m')
print('\033[1;33mJOGO EM CONSTRUÇÃO!\033[m')