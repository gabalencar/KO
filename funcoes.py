import sqlite3

def listar_Eventos():
    con = sqlite3.connect('/home/hadassa/Documentos/IFCE/yuri/meu_banco.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM mural_PF;')
    cursor.execute('SELECT * FROM mural_PJ;')
    con.commit()
    con.close()

def editar_Eventos():
    listar_Eventos()
    evento = str(input("""EVENTO A EDITAR:
Pessoa Física [PF]
Pessoa Jurídica [PJ]
OPÇÃO: """)).strip().upper()
    nome_Evento = input('Qual o nome do evento a editar? ')
    nome_Criador = input('Nome do criador: ')
    data_Inicio = input('Data de início: ')
    data_Termino = input('Data de termino: ')
    modalidade = input('Modalidade: ')
    descricao = input('Descrição: ')
    contato = input('Contatos: ')
    con = sqlite3.connect('/home/hadassa/Documentos/IFCE/yuri/meu_banco.db')
    cursor = con.cursor()
    if evento == 'PF':
        consultaEditar = 'UPDATE mural_PF SET nome_Evento = ?, nome_Criador = ?, data_Inicio = ?, data_Termino = ?, modalidade = ?, descricao = ?, contato = ? WHERE id = ?;'
        cursor.execute(consultaEditar,(nome_Evento, nome_Criador, data_Inicio, data_Termino, modalidade, descricao, contato))
    elif evento == 'PJ':
        consultaEditar = 'UPDATE mural_PJ SET nome_Evento = ?, nome_Criador = ?, data_Inicio = ?, data_Termino = ?, modalidade = ?, descricao = ?, contato = ? WHERE id = ?;'
        cursor.execute(consultaEditar,(nome_Evento, nome_Criador, data_Inicio, data_Termino, modalidade, descricao, contato))
    con.commit()
    con.close()

def deletar_Eventos():
    listar_Eventos()
    evento = int(input("""EVENTO A REMOVER:
    PESSOA FÍSICA [1]
    PESSOA JURÍDICA [2]
    OPÇÃO: """)).strip()
    id = int(input('Qual o ID do evento a remover? '))
    con = sqlite3.connect('/home/hadassa/Documentos/IFCE/yuri/meu_banco.db')
    cursor = con.cursor()
    if evento == 'PF':
        consultaDelete = f'DELETE FROM mural_PF WHERE id = {id};'
    elif evento == 'PJ':
        consultaDelete = f'DELETE FROM mural_PJ WHERE id = {id};'
    else:
        print("OPÇÃO INVÁLIDA, INFORME 1 OU 2")
    cursor.execute(consultaDelete)
    con.commit()
    con.close()

def cadastrar_Eventos():
    con = sqlite3.connect('/home/hadassa/Documentos/IFCE/yuri/meu_banco.db')
    cursor = con.cursor()
    print()
    print('-' * 60)
    print(f'\033[1;33m{"CADASTRO DE NOVO CLIENTE":=^40}\033[m')
    escolha = int(input("""
    PESSOA FÍSICA [1]
    PESSOA JURÍDICA [2]
    OPÇÃO: """)).strip()
    nome_Evento = str(input('Nome do Evento: '))
    nome_Criador = str(input('Nome do Organizador: '))
    data_Inicio = str(input('Data de início do Evento: '))
    data_Termino = str(input('Data de encerramento do Evento: '))
    modalidade = input("Modalidade: ")
    descricao = input("Descrição: ")
    contato = input("Contato da Organização: ")

    if escolha == 1:
        consultaCreate = """INSERT INTO mural_PF (nome_Evento, nome_Criador, data_Inicio, data_Termino, 
        modalidade, descricao, contato) VALUES (?, ?, ?, ?, ?, ?, ?);"""
        cursor.execute(consultaCreate,(nome_Evento, nome_Criador, data_Inicio, data_Termino, modalidade, descricao, contato))

    elif escolha == 2:
        consultaCreate = """INSERT INTO mural_PJ (nome_Evento, nome_Criador, data_Inicio, data_Termino, 
        modalidade, descricao, contato) VALUES (?, ?, ?, ?, ?, ?, ?);"""
        cursor.execute(consultaCreate,(nome_Evento, nome_Criador, data_Inicio, data_Termino, modalidade, descricao, contato))
    
    else:
        print("OPÇÃO INVÁLIDA, INFORME 1 OU 2")

    con.commit()
    con.close()

