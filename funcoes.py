# Filtra Palavras
def filtra(lista,quantidade):
    lista_atualizada = []

    for palavra in lista:
        if (len(palavra) == quantidade):
            minuscula = palavra.lower()
            if minuscula not in lista_atualizada:
                lista_atualizada.append(minuscula)
    
    return lista_atualizada

# Inicializa Termo
def inicializa(lista_atualizada):
    import random
    termo = {}
    termo['n'] = len(lista_atualizada[0])
    termo['sorteada'] = random.choice(lista_atualizada)
    termo['especuladas'] = []
    termo['tentativas'] = len(lista_atualizada[0]) + 1
    return termo

# Indica Posição Correta
def inidica_posicao(sorteada,especulada):

    if len(sorteada) != len(especulada):
        return []

    letras_sorteada = []
    letras_especulada = []
    posicao = [0]*len(sorteada)
    i = 0

    for letra in sorteada:
        letras_sorteada.append(letra)

    for letra in especulada:
        letras_especulada.append(letra)

    for letra in letras_especulada:
        if letra not in letras_sorteada:
            posicao[i]=2
        elif letra in sorteada:
            if letras_especulada[i] == letras_sorteada[i]:
                posicao[i]=0
            else:
                posicao[i]=1
        i+=1
    return posicao