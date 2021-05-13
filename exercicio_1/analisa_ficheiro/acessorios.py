import os


def pede_nome():
    while True:
        try:
            name = input(f"Insira o nome do ficheiro (pasta {os.getcwd()}): ")
            f = open(name, 'r')
            return name
        except IOError:
            print("Ficheiro nao existe")


def ler_texto(nome):
    ficheiro = open(nome, encoding='utf-8')
    texto = ficheiro.read()
    ficheiro.close()
    return texto


def ler_linhas(nome):
    ficheiro = open(nome, encoding='utf-8')
    lista = ficheiro.readlines()
    ficheiro.close()
    return lista


def gera_nome(fileName):
    fileName = fileName[0:-4]
    fileName += ".json"

    return fileName
