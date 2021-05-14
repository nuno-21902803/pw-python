import analise_pasta



def main():
    nomeDir = analise_pasta.pede_pasta()

    analise_pasta.guarda_resultados(nomeDir)
    analise_pasta.faz_grafico_queijos("Queijo", nomeDir)
    analise_pasta.faz_grafico_barras("Barras", nomeDir)

if __name__ == "__main__":
    main()
