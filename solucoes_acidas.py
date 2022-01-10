
def volume():
    massamolar = 0
    densidade = 0
    pureza = 0

    print('Bem vindo a calculadora de soluções ácidas!\n')

    acido = float(input('Digite o número correspondente ao ácido utilizado no preparo:'
                        '\n1 - Ácido Sulfúrico. \n2 - Ácido Clorídrico. \n3 - Ácido Nítrico.\n'))

    if acido == 1:
        massamolar = 98.079
        densidade = 1.83
        pureza = 98
        print('Você selecionou o Ácido Sulfúrico.\n')
    elif acido == 2:
        massamolar = 36.458
        densidade = 1.18
        pureza = 37
        print('Você selecionou o Ácido Clorídrico.\n')
    elif acido == 3:
        massamolar = 63.01
        densidade = 1.51
        pureza = 65
        print('Você selecionou o Ácido Nítrico.\n')

    volume_final = float(input('Qual o volume desejado da solução final (em Litros)? '))
    concentracao = float(input('Qual é a concentração dessa solução (em mol/L)? '))

    v = ((100 * massamolar * concentracao * volume_final) / (pureza * densidade))
    print(f'Para fazer {volume_final} litros da solução, você precisará de %.2f' % v + 'mL do ácido desejado')


if __name__ == '__main__':
    volume()

