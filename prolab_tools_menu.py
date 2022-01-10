import teor_de_umidade
import teor_de_cinzas
import residuo_apos_evaporacao
import solucoes_acidas


def prolab_tools():
    print('***********************************************')
    print('**** PróLab Biotecnologia - Físico Química ****')
    print('***********************************************')

    print('(1) - Teor de Umidade\n(2) - Teor de Cinzas\n(3) - Resíduo após evaporação\n(4) - Soluções Ácidas')

    parametro = int(input('Digite o número do parâmetro desejado: '))

    if parametro == 1:
        print('Teor de Umidade selecionado')
        teor_de_umidade.teor()
    elif parametro == 2:
        print('Teor de Cinzas selecionado')
        teor_de_cinzas.teor()
    elif parametro == 3:
        print('Resíduo após evaporação selecionado')
        residuo_apos_evaporacao.residuo()
    elif parametro == 4:
        print('Soluções Ácidas selecionado')
        solucoes_acidas.volume()
    else:
        print('O número digitado não corresponde as opções\n\n')
        prolab_tools()


if __name__ == '__main__':
    prolab_tools()
