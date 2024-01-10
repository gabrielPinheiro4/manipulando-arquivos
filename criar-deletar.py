import os

def cria_exclui():
    print()
    print('**********************************')
    print('******* GERENCIAR ARQUIVOS *******')
    print('**********************************')
    print()

    try:
        while True:
            decisao = int(input('(1)Criar Arquivo  (2)Excluir Arquivo (3)Criar Pasta (4)Excluir Pasta: '))

            if decisao == 1:
                nome_arquivo = input('Digite o nome do arquivo: ')
                with open(nome_arquivo, 'w') as arquivo:
                    pass
                return 'Arquivo criado com sucesso'

            elif decisao == 2:
                deletar_arquivo = input('Digite o nome do arquivo que você deseja deletar: ')
                os.remove(deletar_arquivo)
                return 'Arquivo deletado com sucesso'

            elif decisao == 3:
                nome_pasta = input('Digite o nome da pasta: ')
                os.mkdir(nome_pasta)
                return 'Pasta criada com sucesso'

            elif decisao == 4:
                deletar_pasta = input('Digite o nome da pasta que você deseja deletar: ')
                os.rmdir(deletar_pasta)
                return 'Pasta deletada com sucesso'
            
            print('Digite um número de acordo com as opções')

    except FileNotFoundError:
        return 'Arquivo não encontrado'

    except KeyboardInterrupt:
        return 'Você saiu do programa'
    
    except OSError:
        return 'A pasta que você deseja deletar contém arquivos, delete-os primeiro'
