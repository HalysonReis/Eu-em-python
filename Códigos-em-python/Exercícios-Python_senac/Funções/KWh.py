def KWh(potencia, horas):
    consumido = (potencia * horas) / 1000

    return consumido

conversao = KWh(300, 5)

print(conversao)