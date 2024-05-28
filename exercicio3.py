def calcular_comissao(vendas, comissao):
    comissoes = []
    for i in range(len(vendas)):
        comissoes.append(vendas[i] * comissao[i] / 100)
    return comissoes

def receber_dados_vendedores():
    vendas = []
    comissoes = []
    nomes = []
    for i in range(10):
        nome = input("Digite o nome do vendedor {}: ".format(i+1))
        nomes.append(nome)
        venda = float(input("Digite o total de vendas do vendedor {}: ".format(nome)))
        vendas.append(venda)
        comissao = float(input("Digite o percentual de comissão do vendedor {} (%): ".format(nome)))
        comissoes.append(comissao)
    return vendas, comissoes, nomes

def main():
    vendas, comissoes, nomes = receber_dados_vendedores()
    comissoes_calculadas = calcular_comissao(vendas, comissoes)
    
    print("\nRelatório de Comissões:")
    total_vendas = sum(vendas)
    print("Total de vendas de todos os vendedores: R${}".format(total_vendas))
    
    maior_comissao = max(comissoes_calculadas)
    menor_comissao = min(comissoes_calculadas)
    maior_index = comissoes_calculadas.index(maior_comissao)
    menor_index = comissoes_calculadas.index(menor_comissao)
    
    print("Maior valor a receber: R${} (Vendedor: {})".format(maior_comissao, nomes[maior_index]))
    print("Menor valor a receber: R${} (Vendedor: {})".format(menor_comissao, nomes[menor_index]))
    
    print("\nRelatório de Vendedores e Valores a Receber:")
    for i in range(10):
        print("Vendedor: {}, Valor a Receber: R${}".format(nomes[i], comissoes_calculadas[i]))

if __name__ == "__main__":
    main()
