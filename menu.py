"""
FUNÇÕES DO MENU
"""

from base import linha, ler_inteiro

def mensagem_menu(txt, tam=40):
    
    linha()
    print(f"{txt.center(tam)}")
    linha()


def opcao_menu(lista):
    
    mensagem_menu(lista[0])
    
    for i in range(1, len(lista)):
        print(f"{i} - \t{lista[i]}")
    
    linha()
    opcao = ler_inteiro("Digite sua opção: ")

    return opcao