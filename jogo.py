import palavras
import funcoes

COR_AZUL = '\033[94m'
COR_AMARELA = '\033[93m'
COR_CINZA = '\033[90m'
COR_RESET = '\033[0m'
COR_VERMELHA = '\033[91m'
COR_VERDE = '\033[92m'

def print_welcome_message():
    print((' '+("="*27))+"\n"+("|" + (' ')*27 +'|')+"\n"+("|" + " Bem-vindo ao Insper Termo "+"|")+"\n"+("|" + (' ')*27 +'|')+"\n"+(' '+("="*3)+(" Design de Software ") +("="*3)))
    print('\n'+'Comandos: Para sair do jogo digite "desisto"'+'\n')

def print_rules(qtde_letras, tentativas, azul, amarelo, cinza):
    print('\n'+"Regras:"+"\n"+'\n'+("- Você tem {0} tentativas para acertar uma palavra aleatória de {1} letras.".format(tentativas,qtde_letras)))
    print('- A cada tentativas, a palavra testada terá suas suas letras coloridas conforme:')
    print(' * {0}: a letra está na posição correta;'.format(azul))
    print(' * {0}: a palavra tem a letra, mas está na posição errada;'.format(amarelo))
    print(' * {0}: a palavra não tem a letra.'.format(cinza))
    print('- Os acentos são ignorados;'+'\n'+ '- As palavras podem possuir letras repetidas.' + '\n')

def print_congratulations(parabens):
    print('\n'+'{0}'.format(parabens))

def print_invalid_word(qtde_letras):
    quantidade_letras = COR_VERMELHA + str(qtde_letras) + COR_RESET
    print('\n'+"Palavra Inválida. Tente uma palavra de "+'{0}'.format(quantidade_letras)+" letras")

def print_word_not_tried():
    print('\n'+ "Você já tentou essa palavra. Tente uma nova!"+'\n')

def print_word_not_found(word):
    word = COR_VERMELHA + word + COR_RESET
    print('\n'+"Uma pena você ter desistido... A palavra era: {}".format(word))

def print_goodbye_message():
    obrigado = COR_VERDE + 'Muito obrigado por ter jogado! Até a próxima! :D' + COR_RESET
    print('\n'+ '{0}'.format(obrigado))