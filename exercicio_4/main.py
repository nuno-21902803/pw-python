import car


def main():
    carro = car.Automovel()
    carro.init(60, 10, 15)

    print(f"Car Status\nAutonomia :{round(carro.autonomia(),3)}\nCombustivel :{carro.combustivel()}")
    print(f"Capacidade :{carro.cap_dep}\nConsumo :{carro.consumo}")
    print("\nExemplo de funcinalidades\n"
          f"Autonomia passado percorrer 30km (Ex) :{round(carro.percorrer(30),3)}\n"
          f"Dá para abastecer 25Litros? Se sim, quantos ficam (Ex) :{round(carro.abastercer(25),3)}\n")



if __name__ == "__main__":
    main()
