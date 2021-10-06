# importa Tkinder
from tkinter import *
from tkinter import ttk

# declara janela
window = Tk()
window.title("Calculadora")

# definicao de configurações de largura e comprimento
window.geometry("235x318")

# definicao de duas janelas: display com cálculo e botões
frame_window = Frame(window, width="235", height="50")
frame_window.grid(row=0, column=0)



# executa eventos da janela
window.mainloop()
