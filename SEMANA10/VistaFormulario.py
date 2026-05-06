"""
aqui use el messagebox como ventana emergente para mi respuesta al accionar
el boton que tengo, ese messagebox lo saque de la siguiente pagina
https://recursospython.com/guias-y-manuales/cuadros-de-dialogo-messagebox-en-tkinter/

"""

import tkinter as Ventana
from tkinter import messagebox

class Vista_formulario:
    def __init__(self):
        self.formulario = Ventana.Tk()
        self.formulario.title("Programa de Números")
        self.formulario.geometry("300x200")
        self.MeterNumero = ""

    def pedir_numero(self, accion):
        Ventana.Label(self.formulario, text="INGRESE UN NÚMERO:").pack()
        self.MeterNumero = Ventana.Entry(self.formulario)
        self.MeterNumero.pack()
        boton = Ventana.Button(self.formulario, text="Procesar", command=lambda: accion())
        boton.pack()

    def imprimir_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def Valores(self):
        return self.MeterNumero.get()