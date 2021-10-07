# importa Tkinder
from tkinter import *
from tkinter import ttk

#cores

black = "#0d0901"
brown = "#524f49"
orange = "#f27130"
gray = "#ccc8c6"
white = "#ffffff"

# declara janela
window = Tk()
window.title("Calculadora")

# definicao de configurações de largura e comprimento
window.geometry("235x318")
window.config(bg = black)

# frame de calculo
frameHead = Frame(window, width = "235", height = "50", bg = brown)
frameHead.grid(row = 0, column = 0)

# frame de botões
frameBody = Frame(window, width = "235", height = "268")
frameBody.grid(row = 1, column = 0)

#cria botões
#line1
clean = Button(frameBody, text = "C", width = 11, height= 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
clean.place(x = 0, y = 0)

module = Button(frameBody, text = "%", width = 5, height = 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
module.place(x = 118, y = 0)

division = Button(frameBody, text = "/", width = 5, height = 2, bg = orange, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
division.place(x = 177, y = 0)
#line2
seven = Button(frameBody, text = "7", width = 5, height= 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
seven.place(x = 0, y = 52)

eight = Button(frameBody, text = "8", width = 5, height = 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
eight.place(x = 60, y = 52)

nine = Button(frameBody, text = "9", width = 5, height = 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
nine.place(x = 118, y = 52)

mult = Button(frameBody, text = "X", width = 5, height = 2, bg = orange, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
mult.place(x = 177, y = 52)



# executa eventos da janela
window.mainloop()
