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
window.geometry("235x314")
window.config(bg = black)

# frame de calculo
frameHead = Frame(window, width = "235", height = "58", bg = brown)
frameHead.grid(row = 0, column = 0)

# frame de botões
frameBody = Frame(window, width = "235", height = "268")
frameBody.grid(row = 1, column = 0)

#criação de labels
appLabel = Label(frameHead, text = '123456789', font = "Arial, 16", bg = brown, fg = white, width = 19, height = 2, padx = 5, pady = 5, relief = FLAT, anchor="e", justify=RIGHT)
appLabel.grid(row = 0, column = 0)

#cria botões
#line1
clean = Button(frameBody, text = "C", width = 11, height= 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
clean.place(x = 0, y = 0)

module = Button(frameBody, text = "%", width = 5, height = 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
module.place(x = 118, y = 0)

division = Button(frameBody, text = "/", width = 5, height = 2, bg = orange, fg = white, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
division.place(x = 177, y = 0)

#line2
seven = Button(frameBody, text = "7", width = 5, height= 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
seven.place(x = 0, y = 52)

eight = Button(frameBody, text = "8", width = 5, height = 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
eight.place(x = 60, y = 52)

nine = Button(frameBody, text = "9", width = 5, height = 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
nine.place(x = 118, y = 52)

mult = Button(frameBody, text = "X", width = 5, height = 2, bg = orange, fg = white, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
mult.place(x = 177, y = 52)

#line3
six = Button(frameBody, text = "6", width = 5, height= 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
six.place(x = 0, y = 104)

five = Button(frameBody, text = "5", width = 5, height = 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
five.place(x = 60, y = 104)

four = Button(frameBody, text = "4", width = 5, height = 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
four.place(x = 118, y = 104)

subt = Button(frameBody, text = "-", width = 5, height = 2, bg = orange, fg = white, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
subt.place(x = 177, y = 104)

#line4
three = Button(frameBody, text = "3", width = 5, height= 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
three.place(x = 0, y = 156)

two = Button(frameBody, text = "2", width = 5, height = 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
two.place(x = 60, y = 156)

one = Button(frameBody, text = "1", width = 5, height = 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
one.place(x = 118, y = 156)

sum = Button(frameBody, text = "+", width = 5, height = 2, bg = orange, fg = white, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
sum.place(x = 177, y = 156)

#line5
naught = Button(frameBody, text = "C", width = 11, height= 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
naught.place(x = 0, y = 208)

dot = Button(frameBody, text = ".", width = 5, height = 2, bg = gray, fg = black, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
dot.place(x = 118, y = 208)

equal = Button(frameBody, text = "=", width = 5, height = 2, bg = orange, fg = white, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
equal.place(x = 177, y = 208)

# executa eventos da janela
window.mainloop()
