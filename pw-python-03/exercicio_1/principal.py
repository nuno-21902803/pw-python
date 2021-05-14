import analisa_ficheiro
import json


def main():
    nome = analisa_ficheiro.pede_nome()
    nomeJSON = analisa_ficheiro.gera_nome(nome)

    file_dict = {
        "calcula_linhas": analisa_ficheiro.calcula_linhas(nome),
        "calcula_carateres": analisa_ficheiro.calcula_carateres(nome),
        "calcula_palavra_comprida": analisa_ficheiro.calcula_palavra_comprida(nome),
        "calcula_correncia_de_letras": analisa_ficheiro.calcula_correncia_de_letras(nome)
    }

    with open(nomeJSON, 'w', encoding='utf-8') as json_file:
        json.dump(file_dict, json_file, indent=4)


if __name__ == "__main__":
    main()
