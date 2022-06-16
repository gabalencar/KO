import bancodedados
import funcoes
import menus
from time import sleep

mens = funcoes.cor_String(cod1=1, cod2=35, cod3=40, msg="KARIRI OPPORTUNITY")
print(f'{mens:.^50}')
print()
sleep(1)

bancodedados.inicializa_bd_mural()
bancodedados.inicializa_bd_cadastros()

while True:
    print('-' * 45)
    menus.menu_Principal()
    escolha = int(input('OPÇÃO: '))
    print()
    if escolha == 1:
        while True:
            print('-' * 45)
            menus.menu_Mural()
            escolha = int(input('OPÇÃO: '))
            print()
            if escolha == 1:
                sleep(0.5)
                funcoes.cadastrar_eventos()
            elif escolha == 2:
                sleep(0.5)
                funcoes.listar_Eventos()
            elif escolha == 3:
                sleep(0.5)
                funcoes.editar_Eventos()
            elif escolha == 4:
                sleep(0.5)
                funcoes.deletar_Eventos()
            elif escolha == 5:
                break
            else:
                sleep(0.5)
                print(funcoes.cor_String(cod2=31, msg="OPÇÃO INVÁLIDA! Tente Novamente."))
    elif escolha == 2:
        while True:
            print('-' * 45)
            menus.menu_Cadastros()
            escolha = int(input('OPÇÃO: '))
            print()
            if escolha == 1:
                sleep(0.5)
                funcoes.cadastrar_pessoaFisica()
            elif escolha == 2:
                sleep(0.5)
                funcoes.cadastrar_pessoaJuridica()
            elif escolha == 3:
                break
            else:
                sleep(0.5)
                print(funcoes.cor_String(cod2=31, msg="OPÇÃO INVÁLIDA! Tente Novamente."))
    elif escolha == 3:
        funcoes.noticação_evento()
        sleep(0.5)
        print(funcoes.cor_String(cod2=32, msg="SISTEMA FINALIZADO COM SUCESSO. ATÉ A PRÓXIMA!"))
        print()
        break
    else:
        sleep(0.5)
        print(funcoes.cor_String(cod2=31, msg="OPÇÃO INVÁLIDA! Tente Novamente."))
