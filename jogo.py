import palavras
import funcoes

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