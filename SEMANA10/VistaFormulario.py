import tkinter as Ventana

class Vista_formulario:
    def __init__(self):
        self.titulo = "Parcial Semana10 Python"
        self.pregunta_campo_numero = "INGRESE UN NÚMERO:"
        self.campo_dato_numero = ""
        self.formulario = Ventana.Tk()
        self.formulario.title(self.titulo)
        self.formulario.geometry("600x600")
        self.label_resultado = Ventana.Label(self.formulario, text="...")

    def pedir_numero(self, accion):
        label_pregunta = Ventana.Label(self.formulario, text=self.pregunta_campo_numero)
        label_pregunta.pack()
        
        self.campo_dato_numero = Ventana.Entry(self.formulario)
        self.campo_dato_numero.pack()
        
        boton = Ventana.Button(self.formulario, text="Resolver", command=lambda: accion())
        boton.pack()
        self.label_resultado.pack()

    def imprimir_mensaje(self, dato_mensaje):
        self.label_resultado.config(text=dato_mensaje)

    def imprimir_numero(self, dato_numero):
        print(dato_numero)