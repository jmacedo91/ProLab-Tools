def residuo():
    tara = tara_bequer()
    volume = volume_amostra()
    final = peso_final()
    calculo_residuo(tara, volume, final)


def tara_bequer():
    tara = float(input('Digite a massa do béquer que você utilizou (em gramas): '))
    return tara


def volume_amostra():
    volume = float(input('Digite o volume da amostra (em mL): '))
    return volume


def peso_final():
    final = float(input('Digite a massa do béquer após a evaporação da amostra (em gramas):'))
    return final


def calculo_residuo(tara, volume, final):
    resposta = 1e6 * ((final - tara)/volume)
    print(f'A sua amostra contém %.2f mg/L de resíduo após evaporação' % resposta)


if __name__ == '__main__':
    residuo()
