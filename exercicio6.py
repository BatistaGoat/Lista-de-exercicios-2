def soma_entre_numeros(N):
    soma = 0
    for i in range(1, N + 1):
        soma += i
    return soma

# Exemplo de uso da função
def main():
    numero = int(input("Digite um número inteiro e positivo: "))
    if numero > 0:
        resultado = soma_entre_numeros(numero)
        print("A soma dos N números inteiros entre 1 e", numero, "é:", resultado)
    else:
        print("Por favor, digite um número inteiro e positivo.")

if __name__ == "__main__":
    main()
