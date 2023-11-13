import palavras
import funcoes

COR_AZUL = '\033[94m'
COR_AMARELA = '\033[93m'
COR_CINZA = '\033[90m'
COR_RESET = '\033[0m'
COR_VERMELHA = '\033[91m'
COR_VERDE = '\033[92m'

print((' '+("="*27))+"\n"+("|" + (' ')*27 +'|')+"\n"+("|" + " Bem-vindo ao Insper Termo "+"|")+"\n"+("|" + (' ')*27 +'|')+"\n"+(' '+("="*3)+(" Design de Software ") +("="*3)))
print('\n'+'Comandos: Para sair do jogo digite "desisto"'+'\n')

while True:

    while True:
        qtde = int(input("Digite a Quantidade de letras que você deseja jogar: "))
        print('\n'+"Carregando... Por favor, aguarde!")
        lista_jogo = funcoes.filtra(palavras.PALAVRAS,qtde)
        if lista_jogo == []:
            print("Quantidade Inválida! Tente uma quantidade de letras menor ou igual a 23!" + '\n')
        else: 
            break

    tentativas = COR_VERMELHA + str(qtde+1) + COR_RESET
    qtde_letras = COR_VERMELHA + str(qtde) + COR_RESET
    azul = COR_AZUL + 'Azul' + COR_RESET
    amarelo = COR_AMARELA + 'Amarelo' + COR_RESET
    cinza = COR_CINZA + 'Cinza' + COR_RESET

    print('\n'+"Regras:"+"\n"+'\n'+("- Você tem {0} tentativas para acertar uma palavra aleatória de {1} letras.".format(tentativas,qtde_letras)))
    print('- A cada tentativas, a palavra testada terá suas suas letras coloridas conforme:')
    print(' * {0}: a letra está na posição correta;'.format(azul))
    print(' * {0}: a palavra tem a letra, mas está na posição errada;'.format(amarelo))
    print(' * {0}: a palavra não tem a letra.'.format(cinza))
    print('- Os acentos são ignorados;'+'\n'+ '- As palavras podem possuir letras repetidas.' + '\n')

    sorteio_palavra = funcoes.inicializa(lista_jogo)
    palavra_sorteada = sorteio_palavra['sorteada']

    print('\n'+'Já tenho uma palavra! Tente adivinhá-la!')
    
    tentativas = ['desisto']
    matriz_letras = []
    i = qtde+1
    quit = ''
    while i>0:
        palavra_especulada_geral = input('\n'+'Você tem '+str(i)+' tentativa(s)'+'\n'+'Qual é o seu palpite? ')
        palavra_especulada = palavra_especulada_geral.lower()
        if palavra_especulada not in tentativas:
            tentativas.append(palavra_especulada)
            posicao_letras = funcoes.inidica_posicao(palavra_sorteada,palavra_especulada)
            if posicao_letras == [0]*len(palavra_sorteada):
                parabens = COR_AMARELA + 'PARABÉNS!! Você ganhou!!!'+COR_RESET
                print('\n'+'{0}'.format(parabens))
                break
            elif posicao_letras == []:
                quantidade_letras = COR_VERMELHA + str(qtde) + COR_RESET
                print('\n'+"Palavra Inválida. Tente uma palavra de "+'{0}'.format(quantidade_letras)+" letras")
            else:
                j = 0
                mostra_usuario = "| "
                for letra in palavra_especulada:
                    if posicao_letras[j] == 0:
                        letra = COR_AZUL + letra + COR_RESET
                        j+=1
                    elif posicao_letras[j] == 1:
                        letra = COR_AMARELA + letra + COR_RESET
                        j+=1
                    elif posicao_letras[j] == 2:
                        letra = COR_CINZA + letra + COR_RESET
                        j+=1
                    mostra_usuario = mostra_usuario+ letra + " | "
                matriz_letras.append(mostra_usuario)
                print('\n')
                for palavra in matriz_letras:
                    print((' '+'---')*len(palavra_especulada))                    
                    print(palavra)
                    print((' '+'---')*len(palavra_especulada))
                i-=1
        elif palavra_especulada == 'desisto':
            desistir = input('\n'+'Tem certeza que deseja desistir da rodada? [s/n] ')
            if desistir == 's':
                quit = 's'
                break
        else:
            print('\n'+ "Você já tentou essa palavra. Tente uma nova!"+'\n')
    
    word = COR_VERMELHA + palavra_sorteada + COR_RESET
    
    if i == 0:
        print('\n'+"Que pena... Não foi dessa vez! A palavra era: {0}".format(word) +'\n'+"Lembre-se! A pratica leva a perfeição!!")  
    
    if quit == 's':
        print('\n'+"Uma pena você ter desistido... A palavra era: {0}".format(word))
    
    again = input('\n'+'Deseja jogar novamente? [s/n] ')
    if again == 'n':
        obrigado = COR_VERDE + 'Muito obrigado por ter jogado! Até a próxima! :D' + COR_RESET
        print('\n'+ '{0}'.format(obrigado))
        break
    elif again != 's':
        print('\n'+"Digite um comando válido!")