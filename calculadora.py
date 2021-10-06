# importa Tkinder
from tkinter import *
from tkinter import ttk

#cores

backgroundColor = "#0d0901"
frameColor = "#524f49"

# declara janela
window = Tk()
window.title("Calculadora")

# definicao de configurações de largura e comprimento
window.geometry("400x500")
window.config(bg = backgroundColor)

# definicao de duas janelas: display com cálculo e botões
frame_window = Frame(window, width = "400", height = "100", bg = frameColor)
frame_window.grid(row = 0, column = 0)



# executa eventos da janela
window.mainloop()
