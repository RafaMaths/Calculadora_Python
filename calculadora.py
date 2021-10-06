# importa Tkinder
from tkinter import *
from tkinter import ttk

#cores

backgroundColor = "#0d0901"
frameColor = "#524f49"
operationButton = "#f27130"
numberBotton = "#ccc8c6"

# declara janela
window = Tk()
window.title("Calculadora")

# definicao de configurações de largura e comprimento
window.geometry("400x500")
window.config(bg = backgroundColor)

# frame de calculo
frameHead = Frame(window, width = "400", height = "100")
frameHead.grid(row = 0, column = 0)

# frame de botões
frameBody = Frame(window, width = "400", height = "400")
frameBody.grid(row = 1, column = 0) 

# executa eventos da janela
window.mainloop()
