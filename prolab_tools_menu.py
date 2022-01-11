import teor_de_umidade
import teor_de_cinzas
import residuo_apos_evaporacao
import solucoes_acidas


def prolab_tools():

    msg_abertura()
    menu_calculadoras()
    parametro = numero_parametro()
    selecao(parametro)


def msg_abertura():
    print('***********************************************')
    print('**** PróLab Biotecnologia - Físico Química ****')
    print('***********************************************')


def menu_calculadoras():
    print('(1) - Teor de Umidade\n(2) - Teor de Cinzas\n(3) - Resíduo após evaporação\n(4) - Soluções Ácidas')


def numero_parametro():
    return int(input('Digite o número do parâmetro desejado: '))


def selecao(parametro):
    if parametro == 1:
        print('Teor de Umidade selecionado')
        teor_de_umidade.teor_umidade()
    elif parametro == 2:
        print('Teor de Cinzas selecionado')
        teor_de_cinzas.teor_cinzas()
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
