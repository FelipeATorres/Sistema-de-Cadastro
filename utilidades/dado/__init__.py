from time import sleep

def cabeçalho(msg):
    print('-'*42)
    print('{:^40}'.format(msg))
    print('-'*42)

def menu():
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Remover cadastro')
    print('4 - Sair do Sistema')
    print('-'*42)

def escolha(msg):
    while True:
        try:
            opçao = int(input(msg))

        except (ValueError):
            print('ERRO! Digite uma escolha válida e tente novamente!')
            continue
        
        except (KeyboardInterrupt):
            print('O usuário não digitou nada, tente novamente.')
            continue

        except Exception as erro:
            print(erro.__class__)
        
        else:
            return opçao

def sairsistema():
    print('-'*42)
    print('Saindo do sistema... Até logo!'.center(42))
    print('-'*42)