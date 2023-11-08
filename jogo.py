import palavras
import funcoes

print(' '+("="*27))
print("|" + (' ')*27 +'|')
print("|" + " Bem-vindo ao Insper Termo "+"|")
print("|" + (' ')*27 +'|')
print(' '+("="*3)+(" Design de Software ") +("="*3))
print('\n')

while True:
    qtde = int(input("Deseja jogar com uma palavra de quantas letras?"))
    lista_jogo = funcoes.filtra(palavras.PALAVRAS, qtde)
    if lista_jogo == []:
        print("Quantidade inválida! Tente um número menor de letras")
    else:
        break

print(lista_jogo)
print('Comandos: desisto') ##########################

print("a")