class Numero:
    def __init__(self):
        self.dato_numero = 0
        pass
    
    def get_numero(self):
        return self.dato_numero
        pass

    def set_numero(self, nuevo_numero):
        self.dato_numero = int(nuevo_numero)
        pass
    
    def validar_numero(self, dato_numero):
        if dato_numero % 2 == 0:
            res1 = "Es Par"
        else:
            res1 = "Es Impar"
        
        if dato_numero > 0:
            res2 = "Es Positivo"
        elif dato_numero < 0:
            res2 = "Es Negativo"
        else:
            res2 = "Es Neutro"
        
        return res1 + " - " + res2
        pass