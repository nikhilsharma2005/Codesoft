from tkinter import *

exp=""

def cal(num):
    global exp
    exp=exp+str(num)
    equation.set(exp)

def equal():
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
    except:
        equation.set("Error")
        exp=""

    
def clear():
    global exp
    exp=""
    equation.set("")


wk=Tk()
wk.title("Calculater")
wk.geometry("270x150")
equation=StringVar()

entry=Entry(wk,textvariable=equation)
entry.grid(columnspan=4, ipadx=70)

button9 = Button(wk, text=' 9 ',command=lambda: cal(9), height=1, width=7)
button9.grid(row=2, column=2)
button8 = Button(wk, text=' 8 ',command=lambda: cal(8), height=1, width=7)
button8.grid(row=2, column=1)
button7 = Button(wk, text=' 7 ',command=lambda: cal(7), height=1, width=7)
button7.grid(row=2, column=0)
button6 = Button(wk, text=' 6 ',command=lambda: cal(6), height=1, width=7)
button6.grid(row=3, column=2)
button5 = Button(wk, text=' 5 ',command=lambda: cal(5), height=1, width=7)
button5.grid(row=3, column=1)
button4 = Button(wk, text=' 4 ',command=lambda: cal(4), height=1, width=7)
button4.grid(row=3, column=0)
button3 = Button(wk, text=' 3 ',command=lambda: cal(3), height=1, width=7)
button3.grid(row=4, column=2)
button2 = Button(wk, text=' 2 ',command=lambda: cal(2), height=1, width=7)
button2.grid(row=4, column=1)
button2 = Button(wk, text=' 1 ',command=lambda: cal(1), height=1, width=7)
button2.grid(row=4, column=0)
button0 = Button(wk, text=' 0 ',command=lambda: cal(0), height=1, width=7)
button0.grid(row=5, column=0)
plus = Button(wk, text=' + ',command=lambda: cal("+"), height=1, width=7)
plus.grid(row=5, column=3)
decimal = Button(wk, text=' . ',command=lambda: cal("."), height=1, width=7)
decimal.grid(row=5, column=1)
equals = Button(wk, text=' = ',command=equal, height=1, width=7)
equals.grid(row=5, column=2)
minus = Button(wk, text=' - ',command=lambda: cal("-"), height=1, width=7)
minus.grid(row=4, column=3)
mul = Button(wk, text=' * ',command=lambda: cal("*"), height=1, width=7)
mul.grid(row=3, column=3)
div = Button(wk, text=' / ',command=lambda: cal("/"), height=1, width=7)
div.grid(row=2, column=3)
clean = Button(wk, text=' c ',command=clear, height=1, width=7)
clean.grid(row=6, column=0)
wk.mainloop()
