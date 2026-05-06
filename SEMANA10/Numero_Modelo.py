class Numero:
    def __init__(self):
        self.dato_numero = 0

    def set_numero(self, nuevo_numero):
        self.dato_numero = int(nuevo_numero)

    def get_numero(self):
        return self.dato_numero

    def ParImpar(self):
        if self.dato_numero % 2 == 0:
            return "Es Par"
        else:
            return "Es Impar"

    def PosiNega(self):
        if self.dato_numero > 0:
            return "Es Positivo"
        elif self.dato_numero < 0:
            return "Es Negativo"
        else:
            return "Es Neutro"