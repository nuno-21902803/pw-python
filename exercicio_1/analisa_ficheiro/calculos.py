def calcula_linhas(nome):
    file = open(nome, "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    return line_count


def calcula_carateres(nome):
    file = open(nome, "r")
    char_count = 0
    for line in file:
        if line != "\n":
            char_count += len(line)
    file.close()
    return char_count


def calcula_palavra_comprida(nome):
    file = open(nome, "r")
    max_word = ""
    for line in file:
        if line != "\n":
            line.strip("\n")

            palavras = line.split()

            for word in palavras:
                if len(word) > len(max_word):
                    max_word = word

    file.close()
    return max_word


def calcula_correncia_de_letras(nome):
    filename = open(nome, "r").read().replace("\n", "")
    letras = {}
    for a in filename.lower():
        if a not in letras:
            letras[a] = filename.lower().count(a)
    return letras
