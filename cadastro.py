"""
Mini-Projeto de cadastro em um sistema
Utilização de arquivo como base de registro
Extensão do Exercício 115 do canal Curso em Vídeo

Autor: Thiago Souza
"""
from time import sleep

from base import linha, ler_nome, ler_idade
from menu import mensagem_menu, opcao_menu 
from arquivo import (
    ler_arquivo,
    escrever_arquivo,
    excluir_linha_arquivo
)


arquivo = "cadastro.txt" # Nome do arquivo que guardará os dados

# Lista com menu de opções
lista_menu = ['SISTEMA DE CADASTRO', 'Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Remover uma pessoa', 'Sair do sistema']

while True:

    opcao = opcao_menu(lista_menu)

    if opcao == 1:
        print()
        mensagem_menu("Pessoas Cadastradas")
        ler_arquivo(arquivo)
        print()
        sleep(3)

    elif opcao == 2:
        print()
        mensagem_menu("Novo Cadastro")
        nome = ler_nome("Digite o nome: ")
        idade = ler_idade("Digite a idade: ")
        escrever_arquivo(arquivo, nome, idade)
        print()
        sleep(2)

    elif opcao == 3:
        print()
        linha()
        ler_arquivo(arquivo)
        excluir_linha_arquivo(arquivo)
        print()
        sleep(2)

    elif opcao == 4:
        print()
        mensagem_menu("Saindo do sistema, muito obrigado!")
        sleep(2)
        break

    else:
        print("ERRO! Você digitou uma opção inválida, tente novamente...")
        sleep(1)



