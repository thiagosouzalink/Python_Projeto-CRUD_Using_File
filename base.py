"""
FUNÇÕES BÁSICAS PARA O PROGRAMA
"""

from time import sleep

# Imprimir caracter especial
def linha(tam=40):
    
    print(f"{'='*tam}")


# Recebe e valida um nome
def ler_nome(txt):
    
    stop = True

    while stop:
        stop = False

        nome = input(txt).strip()
        lista_nome = nome.split()

        if len(lista_nome) == 0:
            print("ERRO! Você digitou um nome vazio...")
            sleep(1)
            stop = True

        else:
            for valor in lista_nome:
                # Verifica se o nome contém conteúdo não alfabético
                if not valor.isalpha():
                    print("ERRO! Você digitou um nome inválido...")
                    sleep(1)
                    stop = True

    nome = " ".join(lista_nome)
    return nome


# Recebe e valida um número inteiro
def ler_inteiro(txt=""):

    # Caso o texto seja vazio, exibe uma mensagem default
    if txt == "":
        txt = "Digite o valor de um número inteiro"

    while True:
        try:
            inteiro = int(input(txt))
        
        except (KeyboardInterrupt):
            print("ERRO! Entrada de dados interrompida pelo usuário!")
            inteiro = 0
            break
        except(ValueError):
            print("ERRO! Você digitou um valor inteiro inválido...")
            sleep(1)
        except: # Demais erros
            print("ERRO! O programa teve um erro durante a leitura...")
            sleep(1)

        else:
            break

    return inteiro


# Recebe e valida uma idade
def ler_idade(txt):
    
    if txt == "":
        txt = "Digite o valor da idade" 
    
    while True:
        idade = ler_inteiro(txt)

        if idade < 0:
            print("ERRO! Você digitou uma valor negativo...")
            sleep(1)
        else:
            break

    return idade