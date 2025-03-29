from utilidades import dado
from utilidades import arquivo
from time import sleep

arq = 'treinofelipe.txt'


while True:
    if not arquivo.arquivoExiste(arq):
        arquivo.criarArquivo(arq)
    dado.cabeçalho('MENU PRINCIPAL')
    dado.menu()
    escolha = dado.escolha('Sua opção: ')

    if escolha == 1:
        arquivo.lerArquivo(arq)
        sleep(2)

    elif escolha == 2:
        dado.cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ').capitalize()
        idade = dado.escolha('Idade: ')
        arquivo.cadastrar(arq,nome,idade)
    
    elif escolha == 3:
        dado.cabeçalho('REMOVER CADASTRO')
        id = int(input('Insira o ID do usuário que deseja remover: '))
        arquivo.removercadastro(arq,id)

    elif escolha == 4:
        sair = dado.sairsistema()
        break

    else:
        print('ERRO! Digite uma opção válida.')
        sleep(1)
        continue
