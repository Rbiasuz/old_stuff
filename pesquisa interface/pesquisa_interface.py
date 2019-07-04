from tkinter import *

#Primeiro
#pyi-makespec <yourscript.py>
#pyi-makespec pesquisa_interface.py

# then add your files to the list of tuples data=[].
# The tuples contains the actual path to the file and the path within your bundle.
# If you followed the first point, this should look like datas = [('/your/file/is/here.ext','/your/file/is/')]

# datas=[('all.csv','all.csv')],

#pyinstaller --onefile pesquisa_interface.spec



import os, sys

try:
   wd = sys._MEIPASS
except AttributeError:
   wd = os.getcwd()

file_path = os.path.join(wd,'all.csv/all.csv')

with open(file_path,'r') as csv_file:
    lines = csv_file.readlines()

df = lines

procurar = ''
mostrar = 'nada pra mostrar aqui'
i = 0


def texto1(procurar):
    lista = []

    for Answers in df:
        if procurar in Answers.lower():
            lista.append(Answers)

    return (lista)

def printari(i, lista):
    try:
        mostrar = lista[i]
    except:
        mostrar = 'nada pra mostrar aqui'
    return (mostrar)


window = Tk()


window.title("Welcome to My app")

window.geometry('400x50')

lbl = Label(window, text="O que você gostaria de encontrar?")

lbl.grid(column=0, row=0)

txt = Entry(window, width=40)

txt.grid(column=1, row=0)


def clicked():
    res = txt.get()

    global procurar
    procurar = res

    global i, mostrar, var, lista
    i = 0

    lista = texto1(procurar)

    mostrar = printari(i, lista)

    root = Tk()
    S = Scrollbar(root)
    T = Text(root, height=4, width=50)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = mostrar
    T.insert(END, quote)
    mainloop()


btn = Button(window, text="Atualizar", command=clicked)

btn.grid(column=0, row=1)

def proxima():
    global i, mostrar, var, lista
    i = i + 1

    mostrar = printari(i, lista)

    root = Tk()
    S = Scrollbar(root)
    T = Text(root, height=4, width=50)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = mostrar
    T.insert(END, quote)
    mainloop()


btn2 = Button(window, text="Próxima resposta", command=proxima)

btn2.grid(column=1, row=1)

window.mainloop()




