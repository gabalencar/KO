import sqlite3

def inicializa_bd_mural():
    con = sqlite3.connect('banco_dados.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS mural_PF (id integer primary key autoincrement, token_seguranca integer NOT NULL, nome_Evento VARCHAR(100) NOT NULL, nome_Criador VARCHAR(50) NOT NULL, data_Inicio VARCHAR(10) NOT NULL, data_Termino VARCHAR(10) NOT NULL, modalidade VARCHAR(20) NOT NULL, descricao VARCHAR(255) NOT NULL, local VARCHAR(50), contato VARCHAR(100));')
    cursor.execute('CREATE TABLE IF NOT EXISTS mural_PJ (id integer primary key autoincrement, token_seguranca integer NOT NULL, nome_Evento VARCHAR(100) NOT NULL, nome_Criador VARCHAR(50) NOT NULL, data_Inicio VARCHAR(10) NOT NULL, data_Termino VARCHAR(10) NOT NULL, modalidade VARCHAR(20) NOT NULL, descricao VARCHAR(255) NOT NULL, local VARCHAR(50), contato VARCHAR(100));')
    con.commit()
    con.close()

def inicializa_bd_cadastros():
    con = sqlite3.connect('banco_dados.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS pessoa_Fisica (id integer primary key autoincrement, nome VARCHAR(50) NOT NULL, email VARCHAR(100) NOT NULL);')
    cursor.execute('CREATE TABLE IF NOT EXISTS pessoa_Juridica (id integer primary key autoincrement, nome VARCHAR(50) NOT NULL, email VARCHAR(100) NOT NULL);')
    con.commit()
    con.close()
