from cProfile import label
from cgitb import text
from sys import builtin_module_names
from tkinter import *
from tkinter import messagebox
from matplotlib import pyplot
from random import random
import random
import numpy as np


principal = Tk()
ANCHO = 480
ALTO = 240
s=3
n = StringVar()
x = StringVar()

def generar ():
    matriz=np.array(2,2)

    for i in range(2):
        for j in range(2):
            matriz[i][j]=s

    for i in range(3):
        for j in range(3):
            print(matriz[i][j])

principal.title("Parcial 2")

principal.geometry("500x600")

principal.resizable(0,0)

principal.config(bg="black")

frame_entrada= Frame(principal)
frame_entrada.config(bg="green", width=480, height=260)
frame_entrada.place(x=10, y=10)

titulo = Label(frame_entrada, text= "Ingrese el tamaño de la matriz nxn " )
titulo.config(bg="green", fg="white", font=("Arial",16))
titulo.place(x=10, y=10)

lb_n = Label(frame_entrada, text=" Tamaño = " )
lb_n.config(bg="green", fg="white", font=("Arial",16))
lb_n.place(x=10, y=50, width=100, height=30)

entry_n= Entry(frame_entrada, textvariable=n) 
entry_n.config(font=("Arial, 16"), justify=LEFT, fg="black")
entry_n.focus_set()
entry_n.place(x=120, y=50, width=70, height=30)


lb_b = Label(frame_entrada, text=" Numero a buscar = " )
lb_b.config(bg="green", fg="white", font=("Arial",16))
lb_b.place(x=10, y=120, width=180, height=30)

entry_b= Entry(frame_entrada, textvariable=x) 
entry_b.config(font=("Arial, 16"), justify=LEFT, fg="black")
entry_b.place(x=200, y=120, width=70, height=30)

bt_buscar= Button(frame_entrada, text="Generar", command=generar)
bt_buscar.place(x=200, y=50, width=100, height=30)

bt_generar= Button(frame_entrada, text="Buscar", )
bt_generar.place(x=300, y=120, width=100, height=30)

bt_limpiar= Button(frame_entrada, text="Limpiar", )
bt_limpiar.place(x=10, y=200, width=100, height=30)

frame_matriz= Frame(principal)
frame_matriz.config(bg="red", width=ANCHO, height=ALTO)
frame_matriz.place(x=10, y=280)

principal.mainloop()