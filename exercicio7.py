def converter_para_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

horas = 2
minutos = 40
segundos = 10

total_segundos = converter_para_segundos(horas, minutos, segundos)
print(f"{horas}h, {minutos}min e {segundos}seg correspondem a {total_segundos} segundos.")
