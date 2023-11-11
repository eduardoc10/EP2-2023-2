import palavras
import funcoes

COR_AZUL = '\033[94m'
COR_AMARELA = '\033[93m'
COR_CINZA = '\033[90m'
COR_RESET = '\033[0m'
COR_VERMELHA = '\033[91m'
COR_VERDE = '\033[92m'

print(' '+("="*27))
print("|" + (' ')*27 +'|')
print("|" + " Bem-vindo ao Insper Termo "+"|")
print("|" + (' ')*27 +'|')
print(' '+("="*3)+(" Design de Software ") +("="*3))
print('\n')
print('Comandos: desisto') ##########################

while True:
    ktde = int(input("Kuantidade de palavras kue você deseja jogar: "))
    lista_jogo = funcoes.filtra(palavras.PALAVRAS,ktde)
    if lista_jogo == []:
        print("Kuantidade Inválida! Tente uma Kuantidade menor de letras!")
    else:
        break