def is_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def filtrar_primos(vetor):
    primos = []
    for num in vetor:
        if is_primo(num):
            primos.append(num)
    return primos

def main():
    vetor_original = []
    print("Digite os 15 números inteiros:")
    for i in range(15):
        numero = int(input("Digite o número {}: ".format(i+1)))
        vetor_original.append(numero)
    
    primos = filtrar_primos(vetor_original)
    
    print("\nNúmeros primos encontrados:")
    for primo in primos:
        print(primo, end=" ")

if __name__ == "__main__":
    main()
