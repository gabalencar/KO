import funcoes
import menus
import bancodedados
from time import sleep

print("KARIRI OPORTUNITY")

while True:
    menus.menu_Principal()
    escolhaMenu = int(input("OPÇÃO: "))
    if escolhaMenu == 1:
        while True:
            menus.menu_Mural()
            escolhaMural = int(input("OPÇÃO: "))
            if escolhaMural == 1:
                funcoes.cadastrar_Eventos()
            elif escolhaMural == 2:
                funcoes.listar_Eventos()
            elif escolhaMural == 3:
                funcoes.editar_Eventos()
            elif escolhaMural == 4:
                funcoes.deletar_Eventos()
            elif escolhaMural == 5:
                break
            else:
                print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE")
    elif escolhaMenu == 2:
        menus.menu_Cadastros()
        escolhaCadastros = int(input("OPÇÃO: "))
        
        


