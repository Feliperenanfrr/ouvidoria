from operacoesbd import *


def titulos(texto):
    print('-' * 60)
    print(f'{texto:^60}')
    print('-' * 60)


def listarManifestacoes(conexao):
    consultaListagem = 'select * from ocorrencias'
    ouvidoria = listarBancoDados(conexao, consultaListagem)

    if len(ouvidoria) != 0:
        for item in ouvidoria:
            print(f'ID: {item[0]} - TIPO: {item[1]} - TÍTULO: {item[2]} - DESCRIÇÃO: {item[3]} - AUTOR: {item[4]}')
            print()

    else:
        print('Não há manifestações cadastradas')


def listarPorTipo(conexao):
    print('Qual tipo de manifestação que quer visualizar\n1 - Reclamação\n2 - Sugestão\n3 - Elogio')
    tipo = int(input('Digite sua opção: '))

    if tipo == 1:
        consultaListagem = "select * from ocorrencias where tipo = 'reclamação' "
        ouvidoria = listarBancoDados(conexao, consultaListagem)

        for item in ouvidoria:
            print(f'ID: {item[0]} - TIPO: {item[1]} - TÍTULO: {item[2]} - DESCRIÇÃO: {item[3]} - AUTOR: {item[4]}')
            print()

    elif tipo == 2:
        consultaListagem = "select * from ocorrencias where tipo = 'sugestão' "
        ouvidoria = listarBancoDados(conexao, consultaListagem)

        for item in ouvidoria:
            print(f'ID: {item[0]} - TIPO: {item[1]} - TÍTULO: {item[2]} - DESCRIÇÃO: {item[3]} - AUTOR: {item[4]}')
            print()

    elif tipo == 3:
        consultaListagem = "select * from ocorrencias where tipo = 'elogio' "
        ouvidoria = listarBancoDados(conexao, consultaListagem)

        for item in ouvidoria:
            print(f'ID: {item[0]} - TIPO: {item[1]} - TÍTULO: {item[2]} - DESCRIÇÃO: {item[3]} - AUTOR: {item[4]}')
            print()

    else:
        print('Opção invalida')


def criarManifestacao(conexao):
    print('1 - Reclamação\n2 - Sugestão\n3 - Elogio')
    tipo = int(input('Digite sua opção: '))

    if tipo == 1:
        tipo = 'reclamação'
        titulo = input('digite o titulo da sua reclamação: ')
        descricao = input('Descreva sua reclamação: ')
        nome = input('Digite seu nome: ')

        sqlInsercao = 'insert into ocorrencias (tipo,titulo,descricao,autor) values(%s,%s,%s,%s)'
        valores = (tipo, titulo, descricao, nome)
        insertNoBancoDados(conexao, sqlInsercao, valores)

        print('Manifestação criada com sucesso')

    elif tipo == 2:
        tipo = 'sugestão'
        titulo = input('digite o titulo da sua sugestão: ')
        descricao = input('Descreva sua sugestão: ')
        nome = input('Digite seu nome: ')

        sqlInsercao = 'insert into ocorrencias (tipo,titulo,descricao,autor) values(%s,%s,%s,%s)'
        valores = (tipo, titulo, descricao, nome)
        insertNoBancoDados(conexao, sqlInsercao, valores)

        print('Manifestação criada com sucesso')

    elif tipo == 3:
        tipo = 'elogio'
        titulo = input('digite o titulo do seu elogio: ')
        descricao = input('Descreva seu eslogio: ')
        nome = input('Digite seu nome: ')

        sqlInsercao = 'insert into ocorrencias (tipo,titulo,descricao,autor) values(%s,%s,%s,%s)'
        valores = (tipo, titulo, descricao, nome)
        insertNoBancoDados(conexao, sqlInsercao, valores)

        print('Manifestação criada com sucesso')

    else:
        print('Solicitação invalida')


def quantidadeManifestacoes(conexao):
    """
            O count gera uma tupla com a quantidade de elementos do que foi selecionado
            por isso a é utilizado a variável 'quantidadeX[0][0]', que é apenas o recorte
            do numero representando a quantidade
            """

    consultaContador = 'select count(*) from ocorrencias'
    quantidadeGeral = listarBancoDados(conexao, consultaContador)

    consultaReclamacao = "select count(*) from ocorrencias where tipo = 'reclamação' "
    quantidadeReclamacao = listarBancoDados(conexao, consultaReclamacao)

    consultaSugestao = "select count(*) from ocorrencias where tipo = 'sugestão' "
    quantidadeSugestao = listarBancoDados(conexao, consultaSugestao)

    consultaElogio = "select count(*) from ocorrencias where tipo = 'elogio' "
    quantidadeElogio = listarBancoDados(conexao, consultaElogio)

    print(f'Quantidade de manifestações: {quantidadeGeral[0][0]}')
    print(f'Quantidade de reclamações: {quantidadeReclamacao[0][0]}')
    print(f'Quantidade de sugestões: {quantidadeSugestao[0][0]}')
    print(f'Quantidade de elogios: {quantidadeElogio[0][0]}')


def pesquisaID(conexao):
    id = input('Digite o ID da Manifestação: ')
    consultaID = f"select * from ocorrencias where ID = '{id}' "
    ouvidoria = listarBancoDados(conexao, consultaID)

    if len(ouvidoria) != 0:
        for item in ouvidoria:
            print(f'ID: {item[0]} - TIPO: {item[1]} - TÍTULO: {item[2]} - DESCRIÇÃO: {item[3]} - AUTOR: {item[4]}')

    else:
        print('Não há manifestações com esse ID')


def modificarManifestacao(conexao):
    id = input('Digite o ID da Manifestação: ')
    consultaID = f"select * from ocorrencias where ID = '{id}' "
    ouvidoria = listarBancoDados(conexao, consultaID)

    if len(ouvidoria) != 0:

        novoTitulo = input('Digite o novo titulo da manifestação: ')
        novaDescricao = input('Digite a nova descrição da manifestação: ')
        sqlAtualizar = f"update ocorrencias set titulo = %s, descricao = %s  where ID = {id}"
        valores = (novoTitulo, novaDescricao)

        atualizarBancoDados(conexao, sqlAtualizar, valores)
        print('Manifestação modificada com sucesso')
    else:
        print('Não há Manifestação com este ID para ser modificado\nTente novamente')


def excluirManifestacao(conexao):
    """
           Importando mencionar que são utilizados aspas duplas na consulta
           pois ao utilizar o format, a variavel id precisa estar entre aspas,
           para manter a hierarquia utilizamos tipos diferentes de aspas
           """

    id = input('Digite o ID da manifestação: ')
    consultaListagem = f"select * from ocorrencias where ID = '{id}' "
    ouvidoria = listarBancoDados(conexao, consultaListagem)

    if len(ouvidoria) != 0:
        consultaExcluir = 'delete from ocorrencias where ID = %s '
        dados = [id]

        excluirBancoDados(conexao, consultaExcluir, dados)
        print('Excluido com sucesso')
    else:
        print('Não existe manifestações com esse ID')
