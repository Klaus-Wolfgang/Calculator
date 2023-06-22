from tkinter import *
w = Tk()

def bksp():
    x = display.index(INSERT)
    display.delete('{}-1c'.format(x), "{}".format(x))
def clear():
    display.delete("1.0", "end")

def addtofield(n):
    display.insert(display.index(INSERT), n)

def compute():
    try:
        text = ''+ str(eval(display.get("1.0","end-1c")))
        clear()
        display.insert(END, text)
    except SyntaxError:
        clear()
        display.insert(END, 'Invalid Syntax.')


display = Text(w, font=('Calibri',20), height= 2, width=17, relief=RIDGE, bd=5, padx=8, bg='#1c1c1c', fg='#D4D4D2')
display.grid(row=0, column=0, columnspan=4)
class Click:
    def __init__(self, text, r, c, clr1, clr2):
        self.text = str(text)
        self.r = r
        self.c = c
        self.clr1 = clr1
        self.clr2 = clr2
        Button(w, text= text, font=('Calibri', 20), width=4,
               bg='{}'.format(clr1), activebackground= '{}'.format(clr1),
               fg='{}'.format(clr2), activeforeground='{}'.format(clr2),
               command=lambda : addtofield(text)).grid(row=r, column=c)

g = '#D4D4D2'
b = '#1c1c1c'
o = '#ff9500'
gr = '#505050'

b1 = Click('(', 2, 3, g, b)
b2 = Click(')', 3, 3, g, b)
b4 = Click(7, 2, 0, gr, g)
b5 = Click(8, 2, 1, gr, g)
b6 = Click(9, 2, 2, gr, g)
b7 = Click('/', 1, 3, g, b)
b8 = Click(4, 3, 0, gr, g)
b9 = Click(5, 3, 1, gr, g)
b10= Click(6, 3, 2, gr, g)
b11= Click('*', 1, 2, g, b)
b12= Click(1, 4, 0, gr, g)
b13= Click(2, 4, 1, gr, g)
b14= Click(3, 4, 2, gr, g)
b15= Click('+', 1, 0, g, b)
b16= Click(0, 5, 0, gr, g)
b17= Click('.', 5, 1, gr, g)
b18= Click('-', 1, 1, g, b)
Button(w, text='C', font=('Calibri', 20), width=4,
        bg=o, activebackground= o,
        fg=g, activeforeground=g,
       command=lambda : clear()).grid(row=5, column=2)  # C

Button(w, text='=', font=('Calibri', 20), width=4,
        bg=o, activebackground= o,
        fg=g, activeforeground=g,
       command=lambda : compute()).grid(row=4, column=3)  # =

Button(w,text='Bksp',font=('Calibri', 20),width=4,
        bg=o, activebackground= o,
        fg=g, activeforeground=g,
       command=lambda : bksp()).grid(row=5, column=3)  # backspace

w.title('Calculator')
w.config(background='#1C1C1C')
w.resizable(False, False)

w.mainloop()
