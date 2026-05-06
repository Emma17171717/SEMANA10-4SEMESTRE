from Numero_Modelo import Numero
from VistaFormulario import Vista_formulario

class Controlador:
    def __init__(self):
        self.obj_numero = Numero()
        self.obj_vista = Vista_formulario()

    def gestionar_datos(self):
        valor = self.obj_vista.Valores() 
        self.obj_numero.set_numero(valor)

        res1 = self.obj_numero.ParImpar()
        res2 = self.obj_numero.PosiNega()
        
        mensaje_final = f"El número {valor}:\n{res1}\n{res2}"
        self.obj_vista.imprimir_mensaje("Resultado Final", mensaje_final)

    def iniciar(self):
        self.obj_vista.pedir_numero(self.gestionar_datos)
        self.obj_vista.formulario.mainloop()