def teor_cinzas():
    tara = peso_tara()
    p1 = peso1()
    p2 = peso2()
    calculo_cinzas(tara, p1, p2)


def peso_tara():
    tara = float(input('Digite a massa da cápsula vazia (em gramas): '))
    return tara


def peso1():
    p1 = float(input('Digite a massa da amostra (em gramas): '))
    return p1


def peso2():
    p2 = float(input('Digite a massa da cápsula + amostra após secagem (em gramas): '))
    return p2


def calculo_cinzas(tara, p1, p2):
    cinzas = ((p2 - tara) / p1) * 100
    print(f'O teor de cinzas da amostra é %.2f' % cinzas + '%')


if __name__ == '__main__':
    teor_cinzas()
