import sqlite3
import random
from time import sleep
import datetime
import smtplib
from turtle import pu
# Funções autoexplicativas 
def cadastrar_Eventos():
    con = sqlite3.connect('banco_dados.db')
    cursor = con.cursor()
    mens = cor_String(cod1=1, cod2=36, msg="CADASTRO DE EVENTOS")
    print(f'\n{mens:-^40}\n')
    while True:
        escolha = int(input("""Pessoa Física [1]
Pessoa Jurídica [2]
Opção: """))
        if escolha == 1 or escolha == 2:
            nome_Evento = str(input('\nNome do Evento: '))
            nome_Criador = str(input('Nome do Organizador: '))
            data_Inicio = str(input('Data de início do Evento (Utilize o formato DD/MM/AAAA): '))
            data_Termino = str(input('Data de encerramento do Evento (Utilize o formato DD/MM/AAAA): '))
            modalidade = input('Modalidade: ')
            descricao = input('Descrição: ')
            local = input('Local do Evento: ')
            contato = input('Contato da Organização: ')    
            token = random.randint(1, 1000)
            validadorPF = validar_TokenPF(token)
            validadorPJ = validar_TokenPJ(token) 
            while True:
                if validadorPF == [] and validadorPJ == []: 
                    if escolha == 1:
                        consultaCreate = """INSERT INTO mural_PF (token_seguranca, nome_Evento, nome_Criador, data_Inicio, data_Termino, 
                        modalidade, descricao, local, contato) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
                        cursor.execute(consultaCreate,(token, nome_Evento, nome_Criador, data_Inicio, data_Termino, modalidade, descricao, local, contato))
                        print(f"Seu token de segurança é: {token}\n")
                        print()
                        sleep(0.5)
                        print(cor_String(cod2=30, cod3=43, msg="IMPORTANTE! Anote o seu token de segurança!"))
                        break
                    else:
                        consultaCreate = """INSERT INTO mural_PJ (token_seguranca, nome_Evento, nome_Criador, data_Inicio, data_Termino, 
                        modalidade, descricao, local, contato) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
                        cursor.execute(consultaCreate,(token, nome_Evento, nome_Criador, data_Inicio, data_Termino, modalidade, descricao, local, contato))
                        print(f"Seu token de segurança é: {token}")
                        print()
                        sleep(0.5)
                        print(cor_String(cod2=30, cod3=43, msg="IMPORTANTE! Anote o seu token de segurança!"))
                        break
                else:
                    token = random.randint(1, 1000)
                    validadorPF = validar_TokenPF(token)
                    validadorPJ = validar_TokenPJ(token)
            break  
        else:
            sleep(0.5)
            print(cor_String(cod2=31, msg="OPÇÃO INVÁLIDA! Informe 1 ou 2."))
    print()
    sleep(0.5)
    print(cor_String(cod2=32, msg="CADASTRO CONCLUÍDO COM SUCESSO!"))
    print()
    con.commit()
    con.close()

def listar_Eventos():
    mens = cor_String(cod1=1, cod2=36, msg="EVENTOS CADASTRADOS")
    print(f'\n{mens:-^40}\n')
    sleep(0.2)
    print(cor_String(cod1=1, msg="LEGENDA:"))
    print(f"\033[33mID\033[m Pessoa Física.\n\033[35mID\033[m Pessoa Jurídica.\n")
    con = sqlite3.connect('banco_dados.db')
    cursor = con.cursor()
    consulta = """SELECT id, nome_Evento, nome_Criador, data_Inicio, data_Termino, modalidade,
    descricao, local, contato FROM mural_PF;"""
    cursor.execute(consulta)
    for linha in cursor.fetchall():
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
    consulta = """SELECT id, nome_Evento, nome_Criador, data_Inicio, data_Termino, modalidade,
    descricao, local, contato FROM mural_PJ;"""
    cursor.execute(consulta)
    for linha in cursor.fetchall():
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
        con.close()

def editar_Eventos():
    con = sqlite3.connect('banco_dados.db')
    cursor = con.cursor()
    mens = cor_String(cod1=1, cod2=36, msg="EDITOR DE EVENTOS")
    print(f'\n{mens:-^40}\n')
    sleep(0.5)
    listar_Eventos()
    while True:
        escolha = int(input('O evento à editar é de Pessoa Física [1] ou Pessoa Jurídica [2]: '))
        if escolha == 1 or escolha ==2:
            token = int(input("Insira o token de segurança: "))
            if escolha == 1:
                validador = validar_TokenPF(token)
            else: 
                validador = validar_TokenPJ(token)
            if validador != []:
                nome_Evento = input('Nome do evento: ')
                nome_Criador = input('Organizador: ')
                data_Inicio = input('Início (Utilize o formato DD/MM/AAAA): ')
                data_Termino = input('Término (Utilize o formato DD/MM/AAAA): ')
                modalidade = input('Modalidade: ')
                descricao = input('Descrição: ')
                local = input("Local: ")
                contato = input("Contato: ")
                if escolha == 1:
                        consultaEditar = 'UPDATE mural_PF SET nome_Evento = ?, nome_Criador = ?, data_Inicio = ?, data_Termino = ?, modalidade = ?, descricao = ?, local = ?, contato = ? WHERE token_seguranca = ?;'
                        cursor.execute(consultaEditar,(nome_Evento, nome_Criador, data_Inicio, data_Termino, modalidade, descricao, local, contato, token))
                        break
                else:
                    consultaEditar = 'UPDATE mural_PJ SET nome_Evento = ?, nome_Criador = ?, data_Inicio = ?, data_Termino = ?, modalidade = ?, descricao = ?, local = ?, contato = ? WHERE token_seguranca = ?;'
                    cursor.execute(consultaEditar,(nome_Evento, nome_Criador, data_Inicio, data_Termino, modalidade, descricao, local, contato, token))
                    break
            else:
                sleep(0.5)
                print()
                print(cor_String(cod2=31, msg="TOKEN INVÁLIDO!"))
        else:
            sleep(0.5)
            print()
            print(cor_String(cod2=31, msg="OPÇÃO INVÁLIDA! Tente novamente."))
    sleep(0.5)
    print()
    print(cor_String(cod2=32, msg="EVENTO EDITADO COM SUCESSO!"))
    print()
    con.commit()
    con.close()

def deletar_Eventos():
    mens = cor_String(cod1=1, cod2=36, msg="DELETOR DE EVENTOS")
    print(f'\n{mens:-^40}\n')
    sleep(0.5)
    listar_Eventos()
    while True:
        sleep(0.5)
        escolha = int(input('O evento à deletar é de Pessoa Física [1] ou Pessoa Jurídica [2]: '))
        if escolha == 1 or escolha == 2:
            token = int(input("Insira o token de segurança: "))
            con = sqlite3.connect('banco_dados.db')
            cursor = con.cursor()
            if escolha == 1:
                validador = validar_TokenPF(token)
                if validador != []:
                    consultaDelete = f'DELETE FROM mural_PF WHERE token_seguranca = {token};'
                    break
                else:
                    sleep(0.5)
                    print(cor_String(cod2=31, msg="TOKEN INVÁLIDO!"))
            else:
                validador = validar_TokenPJ(token)
                if validador != []:
                    consultaDelete = f'DELETE FROM mural_PJ WHERE token_seguranca = {token};'
                    break
                else:
                    sleep(0.5)
                    print(cor_String(cod2=31, msg="TOKEN INVÁLIDO!"))
        else:
            sleep(0.5)
            print(cor_String(cod2=31, msg="OPÇÃO INVÁLIDA! Tente novamente."))
    sleep(0.5)
    print()
    print(cor_String(cod2=32, msg="EVENTO DELETADO COM SUCESSO!"))
    print()
    cursor.execute(consultaDelete)
    con.commit()
    con.close()

def cadastrar_pessoaFisica():
    mens = cor_String(cod1=1, cod2=34, msg="CADASTRO DE PESSOA FÍSICA")
    print(f'\n{mens:-^40}\n')
    sleep(0.5)
    con = sqlite3.connect('banco_dados.db')
    cursor = con.cursor()
    nome = str(input('Nome: '))
    email = str(input('Email: '))
    consultaInsert = 'INSERT INTO pessoa_Fisica (nome ,email) VALUES (?,?);'
    cursor.execute(consultaInsert,(nome,email))
    sleep(0.5)
    print()
    print(cor_String(cod2=32, msg="CADASTRO REALIZADO COM SUCESSO!"))
    print()
    con.commit()
    con.close()

def cadastrar_pessoaJuridica():
    mens = cor_String(cod1=1, cod2=34, msg="CADASTRO DE PESSOA JURÍDICA")
    print(f'\n{mens:-^40}\n')
    sleep(0.5)
    con = sqlite3.connect('banco_dados.db')
    cursor = con.cursor()
    nome = str(input('Nome: '))
    email = str(input('Email: '))
    consultaCreate = 'INSERT INTO pessoa_Juridica (nome ,email) VALUES (?,?);'
    cursor.execute(consultaCreate,(nome,email))
    sleep(0.5)
    print()
    print(cor_String(cod2=32, msg="CADASTRO REALIZADO COM SUCESSO!"))
    print()
    con.commit()
    con.close()

def validar_TokenPF(token):
    con = sqlite3.connect('banco_dados.db')
    cursor = con.cursor()
    cursor.execute(f"SELECT token_seguranca FROM mural_PF WHERE token_seguranca = {token};")
    token_banco = []
    for tokens in cursor.fetchall():
        token_banco.append(tokens)
    return token_banco

def validar_TokenPJ(token):
    con = sqlite3.connect('banco_dados.db')
    cursor = con.cursor()
    cursor.execute(f"SELECT token_seguranca FROM mural_PJ WHERE token_seguranca = {token};")
    token_banco = []
    for tokens in cursor.fetchall():
        token_banco.append(tokens)
    return token_banco

#Função para formatação de strings
def cor_String(cod1=5, cod2=37, cod3=48, msg=""):
    """
    -> Formata strings
    parametro cod1: código para formatação da letra
    (1:negrito; 3:itálico; 4:sublinhado; 7:negativo)
    parametro cod2: código para cor da letra
    (30:preto; 31: vermelho; 32: verde; 33:amarelo; 34:lilás; 35:rosa; 36:azul)
    parametro cod3: código para cor de fundo
    (41: vermelho; 42:verde; 43:amarelo; 44:lilás; 45:rosa; 46:azul; 47:branco) 
    parametro msg: string para formatação
    return: retorna a string formatada
    """
    return f"\033[{cod1};{cod2};{cod3}m{msg}\033[m"
#puxa os email cadrastrado no banco.
def puxar_Email():
    con = sqlite3.connect('banco_dados.db')
    cursor = con.cursor()
    cursor2 = con.cursor()
    consuta='SELECT email FROM pessoa_Fisica;'
    consuta2='SELECT email FROM pessoa_Juridica;'
    cursor.execute(consuta)
    cursor2.execute(consuta2)
    email=[]
    for i in cursor.fetchall():
        email.append(i[0])
    for i in cursor2.fetchall():
        email.append(i[0])
    con.close()
    return email

def envio_de_email(i,text):
    sender = "Karirioportunity@gmail.com"
    receiver = i

    message = f"""\
    Subject: eventos ativos.
    To: {receiver}
    From: {sender}

    {text}"""

    with smtplib.SMTP("localhost", 2525) as smtp:
        smtp.login("dde8513e9027fa", "cd372aebed0cab")
        smtp.sendmail(sender, receiver, message)
        smtp.noop()


def noticação_evento():
    for i in puxar_Email():
        envio_de_email(i,'eventos')

