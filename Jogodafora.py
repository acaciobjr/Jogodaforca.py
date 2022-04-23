# Jogodaforca.py
Jogo desenvolvido para fim acadêmico.

import random
import time
palavras = ['ceu','oceano','surf','bola','protetor','praia','cachorro','onda','coqueiro']
palavra_secreta = random.choice(palavras).lower()
letras_escolhidas_pela_pessoa = []
tentativas = 7

def display_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


print('#'*20)
print("JOGO DA FORCA!")
print('#'*20)
print("Olá, somos os seus carrascos. Você chegou até aqui por vontade própria! Quer mesmo continuar?")
jogar = str(input("Sim ou Não: ")).strip().upper()

if jogar in 'SIM':
    print("Voce tem 7 chances para acertar a palavra! Se não acertar, esse será o seu fim!")
    print("\033[31mPensando em palavra...")
    time.sleep(3)
    print("\033[34mPalavra escolhida com sucesso! tudo você pode encontrar na praia.")


else:
    print("Te pegaremos na próxima!")
    exit()



# gera a lista de underlines, com o tamanho da palavra escolhida
palpites = ['_'] * len(palavra_secreta)
print(" A palavra tem {} letras".format(len(palavra_secreta)))
print(' '.join(palpites)) # mostra os underlines separados por espaço

while True:
    print("Qual letra voce acha que a palavra tem? ")
    while True:
        letra = input("Letra:").lower()
        if len(letra) != 1:
            print('Digite apenas uma letra')
        else:
            if letra in letras_escolhidas_pela_pessoa:
                print('A letra {} já foi escolhida'.format(letra))
            else:
                break

    letras_escolhidas_pela_pessoa.append(letra)
    print('letras tentadas: {}'.format((' ').join(letras_escolhidas_pela_pessoa)))

    if letra in palavra_secreta: #apartir dessa linha
        posicoes = []
        # verifica todas as posições que tem a letra
        for i, c in enumerate(palavra_secreta):
            if letra == c:
                palpites[i] = c
                posicoes.append(i) #ate essa linha
        print("Voce acertou uma letra nas posições {}".format(', '.join(map(str, posicoes))))
        print(' '.join(palpites))
        if palavra_secreta == ''.join(palpites):
            print('Parabens voce ganhou!')
            break
    else:
        print("Voce errou uma letra >:)")        
        tentativas -= 1
        print(display_hangman(tentativas))
        if tentativas <= 0:
            print("FORCA! vc perdeu ;)")
            print("A palavra era {}".format(palavra_secreta))
            print("A corda foi curta!")
            break
        print("Tente novamente.\nAgora você tem {} chances".format(tentativas))
