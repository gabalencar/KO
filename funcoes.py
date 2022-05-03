import sqlite3

def listar_Eventos():
    con = sqlite3.connect('mural.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM mural_PF;')
    cursor.execute('SELECT * FROM mural_PJ;')
    con.commit()
    con.close()

def editar_Eventos():
    listar_Eventos()
    nome_Evento = input('Qual o nome do evento a editar? ')
    nome_Criador = input('Nome do criador: ')
    data_Inicio = input('Data de início: ')
    data_Termino = input('Data de termino: ')
    codigo_Plano = input('Código do Plano: ')
    con = sqlite3.connect('/home/hadassa/Documentos/IFCE/yuri/meu_banco.db')
    cursor = con.cursor()
    consultaEditar = 'UPDATE clientes SET nome = ?, cpf = ?, email = ?, codigo_Plano = ? WHERE id = ?;'
    cursor.execute(consultaEditar,(nome, cpf, email, codigo_Plano, id))
    con.commit()
    con.close()

