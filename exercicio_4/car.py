import os


class Automovel:

    def init(self, cap_dep, quant_comb, consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo

    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        return self.quant_comb * 100 / self.consumo

    def abastercer(self, capacidade_litros):
        if capacidade_litros > self.cap_dep - self.consumo:
            raise os.error("Máxima capacidade atingida")

        self.quant_comb += capacidade_litros
        return self.autonomia()

    def percorrer(self, distanciaPercorrida):
        if distanciaPercorrida > self.autonomia():
            raise os.error(f"Não ha gasolina disponivel para {distanciaPercorrida}Km")

        self.quant_comb -= distanciaPercorrida * self.consumo / 100
        return self.autonomia()

