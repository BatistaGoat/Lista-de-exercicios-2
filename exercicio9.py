import math
def calcular_volume_esfera(raio):
    volume = (4/3) * math.pi * raio ** 3
    return volume


raio_esfera = float(input("Digite o raio da esfera: "))
volume_esfera = calcular_volume_esfera(raio_esfera)
print("O volume da esfera é:" , volume_esfera)
