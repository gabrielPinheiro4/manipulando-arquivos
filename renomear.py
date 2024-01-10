import os, platform

def renomear():
    print()
    print('*************************************')
    print('******** RENOMEAR ARQUIVOS **********')
    print('*************************************')
    print()
    print('**************************************************************')
    print('******** ATENÇÃO AO PASSAR OS CAMINHOS DOS ARQUIVOS **********')
    print('**************************************************************')
    print()
    try:
        while True:
            arquivo = input('Digite o caminho para o arquivo que você deseja mudar: ')

            if platform.system() == 'Linux' and '/' not in arquivo:
                print('Você precisa digitar o caminho para seu arquivo')
                continue

            elif platform.system() == 'Windows' and '\\' not in arquivo:
                print('Você precisa digitar o caminho para seu arquivo')
                continue

            while True:
                novo_nome = input('Digite o caminho completo e o novo nome do arquivo: ')

                if platform.system() == 'Linux' and '/' not in novo_nome:
                    print('Você precisa digitar o caminho completo')
                    continue

                elif platform.system() == 'Windows' and '\\' not in novo_nome:
                    print('Você precisa digitar o caminho para seu arquivo')
                    continue 


                os.rename(arquivo, novo_nome)
                return 'Arquivo renomeado com sucesso'
        

    except FileNotFoundError:
        return 'Arquivo não encontrado'

    except KeyboardInterrupt:
        return 'Você saiu do programa'
