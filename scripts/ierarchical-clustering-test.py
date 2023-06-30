#ESTE CODIGO ES UNA CAGADA IGNORADLO

import tkinter as tk
import random

class Data:
    def __init__(self, posicion_x, posicion_y):
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y

def generar_datos():
    datos = []
    for _ in range(4):
        posicion_x = random.randint(0, 100)
        posicion_y = random.randint(0, 100)
        datos.append(Data(posicion_x, posicion_y))
    return datos


def dibujar_puntos(canvas, datos):
    for data in datos:
        x = data.posicion_x
        y = data.posicion_y
        canvas.create_oval(x-2, y-2, x+2, y+2, fill="red")

def refres():
    
    datos = generar_datos()
    dibujar_puntos(canvas, datos)

def main():
    ventana = tk.Tk()
    ventana.title("Visualización de Datos")
    canvas = tk.Canvas(ventana, width=100, height=100)
    canvas.pack()

    datos = generar_datos()
    dibujar_puntos(canvas, datos)

    boton = tk.Button(ventana, text="Resfres Points", command=refres)
    boton.pack()

    ventana.mainloop()

if __name__ == "__main__":
    main()




