def ultimo_nome(nome_completo):
    partes_do_nome = nome_completo.split()
    return partes_do_nome[-1]

nome = "Matheus Batista de Miranda"
print(ultimo_nome(nome))
