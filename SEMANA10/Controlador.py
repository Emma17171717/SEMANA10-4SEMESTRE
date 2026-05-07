from Numero_Modelo import Numero
from VistaFormulario import Vista_formulario

class Controlador:
    def __init__(self):
        self.obj_numero = Numero()
        self.obj_vista = Vista_formulario()

    def tomar_numero(self):
        valor = self.obj_vista.campo_dato_numero.get()
        self.obj_numero.set_numero(valor)
        n = self.obj_numero.get_numero()
        resultado = self.obj_numero.validar_numero(n)
        self.obj_vista.imprimir_mensaje(resultado)
        self.obj_vista.imprimir_numero(n)

    def iniciar(self):
        self.obj_vista.pedir_numero(self.tomar_numero)
        self.obj_vista.formulario.mainloop()