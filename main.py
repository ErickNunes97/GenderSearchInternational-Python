from deletar import deletar
from cadastrar import cadastrar
from visualizar import visualizar
from grafico import grafico
from update import atualizar

print('Seja bem vindo ao programa assistente de cadastro para pesquisa quantitativa de Homens e Mulheres por país. '
      '\nEscolha uma das opções do menu por favor: ')

opcao = '0'

funcoes = {
    '1': cadastrar,
    '2': visualizar,
    '3': atualizar,
    '4': grafico,
    '5': deletar
}

while opcao != 'SAIR':
    print('\n================ MENU PRINCIPAL =================')
    print('1- Cadastrar - Cadastrar um novo registro')
    print('2- Visualizar - Visualizar no console os registros')
    print('3- Atualizar - Atualizar no console os registros')
    print('4- Grafico - Visualizar o gráfico na tela')
    print('5- Deletar registro - Apagar dados cadastrados')
    print('\nDigite Sair - Sair do programa')
    opcao = input(str("\nDigite a opcao desejada : ")).upper()
    print('================================================')
    print('\n')
    print('\n')
    print('\n')

    if opcao in funcoes:
        funcoes[opcao]()
