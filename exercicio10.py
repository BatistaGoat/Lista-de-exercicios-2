def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, int(numero**0.5)+1):
            if numero % i == 0:
                return False
            return True
        


        def main():
            numero = int(input("Digite um número inteiro positivo: "))
            if numero > 0:
                if eh_primo(numero):
                    print("o núumero", numero, "é primo.")
                else:
                    print("O número", numero, "não é primo.")
                    

            else:
                print("Por favor, digite um número inteiro positivo maior que 0.")


        if __name__ == "__main__":
            main()