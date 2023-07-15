import requests
from tkinter import *
from tkinter import ttk
from datetime import datetime

Azul='#0a31f5'
Vermelho='#eb1515'
Verde='#68e8b3'
Preto='#000000'
Branco='#ffffff'
Bege='#dadde3'

#Cores

def entrada():

    hora = datetime.now().strftime('%H:%M')

    with open('entrada', 'w', encoding='utf-8') as file:
        file.write(f'\nEntrada as {hora}')

    with open('log', 'a', encoding='utf-8') as file:
        file.write(f'\n{data} Entrada as {hora}')
        file.write(f'\n{data} Entrada as {hora}')

    btEntrada.destroy()

    lt3.configure(text=f'Hora\n{hora}')
    lt4 = Label(ts, text='', font='courier 15 bold', fg=Preto, bg=Azul)
    lt4.place(width=350, height=445, x=420, y=0)

    with open('entrada', 'r', encoding='utf-8') as file:
        for linha in file:
            t = file.read()
            lt4.configure(text=t)

    def escrev():

        hora = datetime.now().strftime('%H:%M')

        esc=input1.get()
        with open('entrada', 'a', encoding='utf-8') as file:
            file.write(f'\n{esc}')

        with open('log', 'a', encoding='utf-8') as file:
            file.write(f'\n{hora} {esc}')
            file.write(f'\n{hora} {esc}')

        with open('entrada', 'r', encoding='utf-8') as file:
            for linha in file:
                t = file.read()
                lt4.configure(text=t)
        lt3.configure(text=f'Hora\n{hora}')

        input1.delete('0','end')

    def almoso():
        global img

        hora = datetime.now().strftime('%H:%M')

        with open('entrada', 'a', encoding='utf-8') as file:
            file.write(f'\n Almoço as {hora}')

        with open('log', 'a', encoding='utf-8') as file:
            file.write(f'\n Almoço as {hora}')
            file.write(f'\n Almoço as {hora}')

        with open('entrada', 'r', encoding='utf-8') as file:
            for linha in file:
                t = file.read()
                lt4.configure(text=t)

        btAlmos.destroy()

        btEntrada.destroy()

        def volta():

            with open('entrada', 'a', encoding='utf-8') as file:
                file.write(f'\n Volta as {hora}')

            with open('log', 'a', encoding='utf-8') as file:
                file.write(f'\n Volta as {hora}')
                file.write(f'\n Volta as {hora}')

            with open('entrada', 'r', encoding='utf-8') as file:
                for linha in file:
                    t = file.read()
                    lt4.configure(text=t)

            btVolta.destroy()
            lt.destroy()

        btVolta = Button(ts, text='Volta', command=volta, font='courier 50 bold', bg=Branco)
        btVolta.place(width=763, height=150, x=0, y=200)
        img = PhotoImage(file=ttt)
        lt = Label(ts, image=img, bg=Bege)
        lt.place(width=300, height=187, x=500, y=170)

    input1 = Entry(ts, font='courier 15 bold', bg=Verde, fg=Preto)
    input1.place(width=350, height=55, x=420, y=445)

    btEscrev = Button(ts, text='anotar', command=escrev, font='courier 15 bold', bg=Branco)
    btEscrev.place(width=123, height=50, x=650, y=410)

    btAlmos = Button(ts, text='Almoço', command=almoso, font='courier 20 bold', bg=Branco)
    btAlmos.place(width=163, height=50, x=100, y=150)

    lt3.configure(text=f'Hora\n{hora}')

    def sair():
        hora = datetime.now().strftime('%H:%M')

        with open('entrada', 'a', encoding='utf-8') as file:
            file.write(f'\n Saida as {hora}')

        with open('log', 'a', encoding='utf-8') as file:
            file.write(f'\n Saida as {hora}')
            file.write(f'\n Saida as {hora}')

        with open('entrada', 'r', encoding='utf-8') as file:
            for linha in file:
                t = file.read()
                lt4.configure(text=t)

        global img
        img = PhotoImage(file=ttipo)
        lt = Label(ts, image=img, bg=Bege)
        lt.place(width=300, height=300, x=450, y=100)

        btSaida.destroy()

        btEscrev.destroy()

        btAlmos.destroy()

        lt3.configure(text=f'Hora\n{hora}')

    btSaida = Button(ts, text='Saida', command=sair, font='courier 20 bold', bg=Branco)
    btSaida.place(width=163, height=50, x=100, y=220)

    def log():
        lt = Label(ts, text='', font='courier 30 bold', fg=Preto, bg=Bege)
        lt.place(width=765, height=499, x=0, y=0)

        lt2 = Label(ts, text='', font='courier 15 bold', fg=Preto, bg=Azul)
        lt2.place(width=500, height=650, x=0, y=0)

        çerçeve=Frame()

        cbk=Scrollbar(çerçeve)
        cbk.pack(side=RIGHT,fill=Y)

        liste=Listbox(çerçeve,font='arial 15 bold',yscrollcommand=cbk.set)

        with open('log', 'r', encoding='utf-8') as file:
            for linha in file:
                y= file.readline()
                for x in range(1):
                    liste.insert(END,y)
        liste.place(width=485, height=499,x=0,y=0)

        cbk.config(command=liste.yview)

        çerçeve.place(width=500, height=499,x=0,y=0)

        input1 = Entry(ts, font='courier 15 bold', bg=Bege, fg=Preto)
        input1.place(width=300, height=55, x=500, y=445)

        def busc():
            x=input1.get()
            with open('log', 'r', encoding='utf-8') as file:
                for linha in file:
                    if x in linha:
                        lt2.configure(text=f'{file.readlines()}')

        def app():
            with open('log', 'w', encoding='utf-8') as file:
                file.write(f'Arquivo apagado {data} {hora}')

        def ext():
            lt.destroy()
            btext.destroy()
            lt2.destroy()
            input1.destroy()
            çerçeve.destroy()
            liste.destroy()
            cbk.destroy()
            btapp.destroy()

        btext= Button(ts, text='Sair', command=ext, font='courier 20 bold', bg=Branco)
        btext.place(width=163, height=50, x=550, y=200)
        btapp= Button(ts, text='Apagar\nHistorico', command=app, font='courier 20 bold', bg=Branco)
        btapp.place(width=163, height=50, x=550, y=300)

    btloG = Button(ts, text='Historico', command=log, font='courier 20 bold', bg=Branco)
    btloG.place(width=193, height=50, x=85, y=290)

    lt3.configure(text=f'Hora\n{hora}')

ts = Tk()

#titulo da tela
ts.title('Agenda')

#tamanho da tela
ts.geometry('763x499')

#se dá para aumentar ou diminuir manualmente
ts.wm_resizable(width=False, height=False)

#Cor do fundo
ts.config(bg=Bege)

data = datetime.now().strftime('%d/%m')
hora = datetime.now().strftime('%H:%M')

mesme = Label(ts, text='', font='courier 30 bold',fg=Preto,bg=Azul)
mesme.place(width=720, height=100, x=100,y=0)

lt2 = Label(ts, text=f'Data\n{data}', font='courier 30 bold',fg=Preto,bg=Azul)
lt2.place(width=120, height=100, x=0,y=0)

lt3 = Label(ts, text=f'Hora\n{hora}', font='courier 30 bold',fg=Preto,bg=Azul)
lt3.place(width=120, height=100, x=140,y=0)

btEntrada=Button(ts, text='Entrada', command=entrada, font='courier 50 bold', bg=Branco)
btEntrada.place(width=763, height=100, x=0, y=200)

ttt='Dragon-Ball-Cafeteria-Diner0.png'
ttipo='top.png'

ts.mainloop()