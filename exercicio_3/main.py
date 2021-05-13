import csv
import os
import pathlib


def pede_pasta():
    while True:
        try:
            nome = input("Introduza o caminho para pasta:  ")
            if os.path.isdir(nome):
                return os.path.realpath(nome)
        except IOError:
            print("Pasta não existente")


def calcula_tamanho_pasta(pasta):
    if os.path.isfile(pasta):
        return os.path.getsize(pasta)

    sizes = [calcula_tamanho_pasta(os.path.join(pasta, file)) for file in os.listdir(pasta)]
    return sum(sizes)



def main():
    nome = pede_pasta()
    size = calcula_tamanho_pasta(nome)
    print(f"Tamanho da pasta: {9.537*0.00000010 * size}MB")


if __name__ == "__main__":
    main()
