from tkinter import *

# Definir cores
cor1 = "#000000"  # preto
cor2 = "#ffffff" # branca
cor3 = "#1b4d8f" # azul escuro
cor4 = "#b0b0b0" # cinza
cor5 = "#db7107" # laranja

# Criando a janela com tkinter
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x308")
janela.config(background=cor1)


# Criar os frames (Dividir o app em partes)
frame_tela = Frame(janela, width=235, height=50, background=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, background=cor1)
frame_corpo.grid(row=1, column=0)


#para armazenar todas as expressões que serão avaliadas
todos_valores = ""

# para entrada de valor único
valor_texto = StringVar()

# Criando Função
def entrar_valor(event):
    global todos_valores

    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Criando a label (Onde resultado irá aparecer)
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, font=('Ivy 18'), padx=6, justify=RIGHT, relief=FLAT, anchor="e", background=cor3, fg=cor2)
app_label.place(x=0,y=0)

# Criar os botoes
b_1 = Button(frame_corpo,command = lambda: limpar_tela(), text="C", width=11, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo,command = lambda: entrar_valor('%'), text="%", width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo,command = lambda: entrar_valor('/'), text="/", width=5, height=2, background=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo,command = lambda: entrar_valor('7'), text="7", width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=51)
b_5 = Button(frame_corpo,command = lambda: entrar_valor('8'), text="8", width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=51)
b_6 = Button(frame_corpo,command = lambda: entrar_valor('9'), text="9", width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=51)
b_7 = Button(frame_corpo,command = lambda: entrar_valor('*'), text="*", width=5, height=2, background=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=51)

b_8 = Button(frame_corpo,command = lambda: entrar_valor('4'), text="4", width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=103)
b_9 = Button(frame_corpo,command = lambda: entrar_valor('5'), text="5", width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=103)
b_10 = Button(frame_corpo,command = lambda: entrar_valor('6'), text="6", width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=103)
b_11 = Button(frame_corpo,command = lambda: entrar_valor('-'), text="-", width=5, height=2, background=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=103)

b_12 = Button(frame_corpo,command = lambda: entrar_valor('1'), text="1", width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=155)
b_13 = Button(frame_corpo,command = lambda: entrar_valor('2'), text="2", width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=155)
b_14 = Button(frame_corpo,command = lambda: entrar_valor('3'), text="3", width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=155)
b_15 = Button(frame_corpo,command = lambda: entrar_valor('+'), text="+", width=5, height=2, background=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=155)

b_16 = Button(frame_corpo,command = lambda: entrar_valor('0'), text="0", width=11, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=207)
b_17 = Button(frame_corpo,command = lambda: entrar_valor('.'), text=".", width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=207)
b_18 = Button(frame_corpo,command = lambda: calcular(), text="=", width=5, height=2, background=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=207)





janela.mainloop()