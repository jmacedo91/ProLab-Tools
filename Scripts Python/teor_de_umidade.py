def teor_umidade():
    tara = valor_tara()
    p1 = peso1()
    p2 = peso2()
    calculo_umidade(tara, p1, p2)


def valor_tara():
    tara = float(input('Digite a massa da cápsula vazia (em gramas): '))
    return tara


def peso1():
    p1 = float(input('Digite a massa da amostra (em gramas): '))
    return p1


def peso2():
    p2 = float(input('Digite a massa da cápsula + amostra após secagem (em gramas): '))
    return p2


def calculo_umidade(tara, p1, p2):
    umidade = (1 - ((p2 - tara) / p1)) * 100
    print(f'O teor de umidade da amostra é %.2f' % umidade + '%')


if __name__ == '__main__':
    teor_umidade()
