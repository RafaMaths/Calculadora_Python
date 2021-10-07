# importa Tkinder
from tkinter import *
from tkinter import ttk

#cores

backgroundColor = "#0d0901"
frameHeadColor = "#524f49"
operationButtonColor = "#f27130"
numberBottonColor = "#ccc8c6"
modelColor = "#3054f2"

# declara janela
window = Tk()
window.title("Calculadora")

# definicao de configurações de largura e comprimento
window.geometry("400x500")
window.config(bg = backgroundColor)

# frame de calculo
frameHead = Frame(window, width = "400", height = "100", bg = frameHeadColor)
frameHead.grid(row = 0, column = 0)

# frame de botões
frameBody = Frame(window, width = "400", height = "400")
frameBody.grid(row = 1, column = 0)

#cria botões
clean = Button(frameBody, text = "C", width = 26, height= 4)
clean.place(x = 0, y = 0)

module = Button(frameBody, text = "%", width = 13, height = 4)
module.place(x = 195, y = 0)

division = Button(frameBody, text = "/", width = 13, height = 4)
division.place(x = 300, y = 0)

# executa eventos da janela
window.mainloop()
