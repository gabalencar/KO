import datetime
import sqlite3
import funcoes

# A função realiza a listagem dos eventos que iniciam na data em que o usuário está acessando o sistema
def eventos_Ativos():
    con = sqlite3.connect('banco_dados.db')
    cursor = con.cursor()
    data_hoje = datetime.date.today()
    data_br = data_hoje.strftime("%d/%m/%Y")
    mens = funcoes.cor_String(cod1=1, cod2=36, msg="EVENTOS INICIANDO HOJE")
    print(f'\n{mens:-^40}\n')
    funcoes.sleep(0.2)
    print(funcoes.cor_String(cod1=1, msg="LEGENDA:"))
    print(f"\033[33mID\033[m Pessoa Física.\n\033[35mID\033[m Pessoa Jurídica.\n")
    con = sqlite3.connect('banco_dados.db')
    cursor = con.cursor()
    cursor.execute(f"""SELECT id, nome_Evento, nome_Criador, data_Inicio, data_Termino, modalidade,
    descricao, local, contato FROM mural_PF;""")
    for linha in cursor.fetchall():
        if linha[3] == data_br:
            print('\033[33mID\033[m: ', linha[0])
            print('Nome do evento: ', linha[1])
            print('Organizador: ', linha[2])
            print('Início: ', linha[3])
            print('Termino: ', linha[4])
            print('Modalidade: ', linha[5])
            print('Descrição: ', linha[6])
            print('Local: ', linha[7])
            print('Contato: ', linha[8])
            print('~' * 50)
            print()
    cursor.execute(f"""SELECT id, nome_Evento, nome_Criador, data_Inicio, data_Termino, modalidade,
    descricao, local, contato FROM mural_PJ;""")
    for linha in cursor.fetchall():
        if linha[3] == data_br:
            print('\033[35mID\033[m: ', linha[0])
            print('Nome do evento: ', linha[1])
            print('Organizador: ', linha[2])
            print('Início: ', linha[3])
            print('Termino: ', linha[4])
            print('Modalidade: ', linha[5])
            print('Descrição: ', linha[6])
            print('Local: ', linha[7])
            print('Contato: ', linha[8])
            print('~' * 50)
            print()

