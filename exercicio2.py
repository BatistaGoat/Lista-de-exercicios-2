def encontrar_elemento(vetor, elemento):
    posicoes = []
    for i in range(len(vetor)):
        if vetor[i] == elemento:
            posicoes.append(i)
    return posicoes

def verificar_elemento_igual_30(vetor):
    elementos_igual_30 = encontrar_elemento(vetor, 30)
    if elementos_igual_30:
        print("Elemento 30 encontrado nas posições:", elementos_igual_30)
    else:
        print("Nenhum elemento igual a 30 encontrado no vetor.")

def main():
    vetor = [10, 20, 30, 40, 50, 30, 60, 70, 80, 30, 90, 30, 100, 110, 30]
    verificar_elemento_igual_30(vetor)

if __name__ == "__main__":
    main()
