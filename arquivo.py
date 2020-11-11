"""
MANIPULAR ARQUIVO PARA GUARDAR OS DADOS
"""
import os
from time import sleep

from menu import ler_inteiro

def abrir_arquivo(file):

    try:
        arquivo = open(file, 'r', encoding='utf-8')
    
    except FileNotFoundError:
        print("Arquivo não existente, criando arquivo...")
        arquivo = open(file, 'wt+', encoding='utf-8')
        sleep(1.5)
        return arquivo

    except:
        print("ERRO! O arquivo não pode ser aberto.")
        
    else:
        return arquivo


def ler_arquivo(file):

    arquivo = abrir_arquivo(file)

    # Verifica se o arquivo está vazio
    if os.stat(file).st_size == 0:
        print("Cadastro está vazio!")
        arquivo.close()
        sleep(1)

    else:
        i = 1
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"{i} - {dado[0]:<25}{dado[1]:>3} anos")
            i += 1

        arquivo.close()


def escrever_arquivo(file, nome='<Desconhecido>', idade=0):

    try:
        arquivo = open(file, 'at+', encoding='utf-8')

    except:
        print("ERRO! Falha ao abrir arquivo!")

    else:
        try:
            arquivo.write(f"{nome};{idade}\n")
        except:
            print("ERRO! Falha ao registrar os dados!")
        else:
            print("Novo cadastro realizado com sucesso!")
            arquivo.close()


def excluir_linha_arquivo(file):

    try:
        arquivo = open(file, 'r', encoding="utf-8")
        lista_arquivo = arquivo.readlines() # Guarda todo conteúdo do arquivo em uma lista
        arquivo.close()
    except:
        print("ERRO! Falha ao abrir o arquivo.")

    else:
        if len(lista_arquivo) == 0:
            print("Impossível deletar elemento, cadastro vazio!")

        else:
            print()
            num = ler_inteiro("Digite o índice da pessoa que você deseja exluir: ")

            if num < 0 or num > len(lista_arquivo):
                print("ERRO! Você digitou um índice inexistente no cadastro.")
                sleep(1.5)
            else:
                lista_arquivo.pop(num-1)

                try:
                    arquivo = open(file, 'w', encoding='utf-8')
                except:
                    print("ERRO! Falha ao registrar os dados!")
                else:
                    arquivo.writelines(lista_arquivo)
                    arquivo.close()
                    print("Cadastro excluído com sucesso!")

