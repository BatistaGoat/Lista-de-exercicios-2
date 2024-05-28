pares=[]
impares=[]
numerosPares=0
numerosImpares=0

for i in range(1,7):
    numero=int(input(f"Digite o {i}º número:"))
    if(numero % 2 == 0):
        numerosPares += 1
        pares.append(numero)
    else:
        numerosImpares += 1
        impares.append(numero)
        
print("São", numerosPares, " numero pares: ", pares, ".")
print("São", numerosImpares, " numeros impares: ", impares, ".")