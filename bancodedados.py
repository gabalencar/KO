import sqlite3

def iniciar_bd():
    con = sqlite3.connect('mural.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE mural_PF (id integer primary key autoincrement, nome_Evento VARCHAR(100), nome_Criador VARCHAR(50) not null, data_Inicio VARCHAR(10), data_Termino VARCHAR(10), modalidade VARCHAR(20), descricao VARCHAR(255), contato VARCHAR(100));')
    cursor.execute('CREATE TABLE mural_PJ (id integer primary key autoincrement, nome_Evento VARCHAR(100), nome_Criador VARCHAR(50) not null, data_Inicio VARCHAR(10), data_Termino VARCHAR(10), modalidade VARCHAR(20), descricao VARCHAR(255), contato VARCHAR(100));')
    cursor.execute('CREATE TABLE pessoa_Fisica (id integer primary key autoincrement, nome VARCHAR(50), email VARCHAR(100))')
    cursor.execute('CREATE TABLE pessoa_Juridica (id integer primary key autoincrement, nome VARCHAR(50), email VARCHAR(100))')
    con.commit()
    con.close()





