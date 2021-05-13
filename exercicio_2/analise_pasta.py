import csv
import os
from matplotlib import pyplot as plt
from numpy import inf


def pede_pasta():
    while True:
        try:
            nome = input("Introduza o caminho para pasta:  ")
            if os.path.isdir(nome):
                return nome
        except IOError:
            print("Pasta não existente")


def faz_calculos(directoryInput):
    dic_dir = {}
    directory = os.listdir(directoryInput)

    for file in directory:
        filename = f"testeDir\\{file}"
        if os.path.isfile(filename):
            size = os.path.getsize(filename)
            split_info = filename.split(".")[-1]
            if not split_info in dic_dir:
                dic_dir[split_info] = {}
                dic_dir[split_info]['quantity'] = 1
                dic_dir[split_info]['size'] = size
            else:
                dic_dir[split_info]['quantity'] = dic_dir[split_info]['quantity'] + 1
                dic_dir[split_info]['size'] = dic_dir[split_info]['size'] + size

    return dic_dir


def guarda_resultados(ficheiro):
    dados = faz_calculos(ficheiro)

    with open(ficheiro + '.csv', 'w', newline='') as file:
        campos = ['Extensao', 'Quantidade', 'Tamanho[kByte]']
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        for extention, info in dados.items():
            writer.writerow({'Extensao': extention, 'Quantidade': info['quantity'], 'Tamanho[kByte]': info['size']})


def faz_grafico_queijos(titulo, ficheiro):
    dados = faz_calculos(ficheiro)
    lista_valores = []
    for i in dados.values():
        lista_valores.append(i['quantity'])

    plt.pie(lista_valores, labels=dados.keys(), autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()


def faz_grafico_barras(titulo, nome_ficheiro):
    data = faz_calculos(nome_ficheiro)
    lista_valores = []
    for i in data.values():
        lista_valores.append(i['quantity'])

    plt.bar(data.keys(), lista_valores)
    plt.title(titulo)
    plt.show()
