from funcoes import cor_String


def menu_Principal():
    print(cor_String(cod1=1, msg="MENU DE OPÇÕES"))
    print("""1. Mural de eventos.
2. Cadastros.    
3. Sair.""")

def menu_Mural():
    print(cor_String(cod1=1, msg="MENU DE OPÇÕES"))
    print("""1. Cadastrar evento.
2. Listar eventos.
3. Atualizar evento.
4. Deletar evento.
5. Voltar.""")

def menu_Cadastros():
    print(cor_String(cod1=1, msg="MENU DE OPÇÕES"))
    print("""1. Pessoa Física.
2. Pessoa Jurídica.
3. Voltar.""")
