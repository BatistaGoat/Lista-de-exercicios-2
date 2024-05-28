def calcular_quantidade_preco_inferior(preco_produtos):
    quantidade = 0
    for preco in preco_produtos:
        if preco < 50:
            quantidade += 1
    return quantidade

def encontrar_produtos_entre_precos(produtos, preco_produtos, preco_min, preco_max):
    produtos_entre_precos = []
    for i in range(len(produtos)):
        if preco_min <= preco_produtos[i] <= preco_max:
            produtos_entre_precos.append(produtos[i])
    return produtos_entre_precos

def calcular_media_preco_superior(preco_produtos):
    produtos_preco_superior = [preco for preco in preco_produtos if preco > 100]
    if produtos_preco_superior:
        media = sum(produtos_preco_superior) / len(produtos_preco_superior)
        return media
    else:
        return 0

def main():
    produtos = []
    preco_produtos = []

    for i in range(5):
        produto = input("Digite o nome do produto {}: ".format(i+1))
        preco = float(input("Digite o preço do produto {}: ".format(i+1)))
        produtos.append(produto)
        preco_produtos.append(preco)

    quantidade_preco_inferior_50 = calcular_quantidade_preco_inferior(preco_produtos)
    produtos_entre_50_e_100 = encontrar_produtos_entre_precos(produtos, preco_produtos, 50, 100)
    media_preco_superior_100 = calcular_media_preco_superior(preco_produtos)

    print("\nQuantidade de produtos com preço inferior a R$ 50,00:", quantidade_preco_inferior_50)
    print("Produtos com preço entre R$ 50,00 e R$ 100,00:", produtos_entre_50_e_100)
    print("Média dos preços dos produtos com preço superior a R$ 100,00: R$", media_preco_superior_100)

if __name__ == "__main__":
    main()
