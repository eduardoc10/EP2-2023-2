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

