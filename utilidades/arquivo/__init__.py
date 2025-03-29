from utilidades import dado

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()

    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print('Arquivo {} criado com sucesso!'.format)

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    
    except:
        print('Erro ao ler o arquivo!')
    
    else:
        dado.cabeçalho('PESSOAS CADASTRADAS')
        print('ID | Nome',' '*23, 'Idade')
        print('-'*42)
        for linha in a:
            dados = linha.split(';')
            dados[2] = dados[2].replace('\n','')
            print('{} | {:<30}{} anos'.format(dados[0],dados[1],dados[2]))
            

    finally:
        a.close()

def cadastrar(arq, nome = 'desconhecido', idade = 0):
    num_ids = -1
    try:
        a = open(arq, 'at')
    
    except:
        print('Houve um erro na abertura do arquivo.')
    
    else:
        try: 
            with open(arq, 'r') as arquivo:
                for linha in arquivo:
                    num_ids +=1
            a.write('{};{};{}\n'.format(num_ids+1,nome,idade))

        except:
            print('Houve um erro ao escrever os dados.')
        
        else:
            print('Sucesso ao realizar o cadastro de {}!'.format(nome))
            a.close()

def removercadastro(arq,line):
    with open(arq, 'r') as arquivo:
        linhas_arq = arquivo.readlines()

    if 0 <= line < len(linhas_arq):
        with open(arq,'w') as arquivo:
            for i, linhas_arq in enumerate(linhas_arq):
                if i != line: 
                    arquivo.write(linhas_arq)