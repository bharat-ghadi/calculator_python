# calculation using tkinter

from tkinter import *


def btnClick(number):
    global val
    val = val + str(number)
    print(val)
    data.set(val)


def btnClear():
    global val
    val = ''
    data.set('')


def btnEqual():
    global val
    result = str(eval(val))
    print(result)
    data.set(result)


root = Tk()
root.title('My calculator')
root.geometry('361x450+200+200')
val = ''
data = StringVar()

display = Entry(root, textvariable=data, bd=30, bg='powderblue', justify='right', font=('ariel', 20))
display.grid(row=0, columnspan=4)

# first row:
btn7 = Button(root, text=7, bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick(7))
btn7.grid(row=1, column=0)

btn8 = Button(root, text=8, bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick(8))
btn8.grid(row=1, column=1)

btn9 = Button(root, text=9, bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick(9))
btn9.grid(row=1, column=2)
btn_add = Button(root, text='+', bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick('+'))
btn_add.grid(row=1, column=3)

# second row:
btn4 = Button(root, text=4, bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick(4))
btn4.grid(row=2, column=0)

btn5 = Button(root, text=5, bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick(5))
btn5.grid(row=2, column=1)

btn6 = Button(root, text=6, bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick(6))
btn6.grid(row=2, column=2)

btn_sub = Button(root, text='-', bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick('-'))
btn_sub.grid(row=2, column=3)

# fthird row:
btn1 = Button(root, text=1, bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick(1))
btn1.grid(row=3, column=0)

btn2 = Button(root, text=2, bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick(2))
btn2.grid(row=3, column=1)

btn3 = Button(root, text=3, bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick(3))
btn3.grid(row=3, column=2)

btn_mul = Button(root, text='x', bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick('*'))
btn_mul.grid(row=3, column=3)

# row 4


btn0 = Button(root, text=0, bd=12, height=2, width=6, font=('ariel', 12), command=lambda: btnClick(0))
btn0.grid(row=4, column=1)

btn_div = Button(root, text='/', font=('ariel', 12), bd=12, height=2, width=6, command=lambda: btnClick('/'))
btn_div.grid(row=4, column=2)

btn_equal = Button(root, text="=", font=('ariel', 12), bd=12, height=2, width=6, command=btnEqual)
btn_equal.grid(row=4, column=3)

btnDecimal = Button(root, text='.', bd=12, height=2, width=6, font=('ariel', 12, 'bold'), command=lambda: btnClick('.'))
btnDecimal.grid(row=4, column=0)

# Row 5
btnPower = Button(root, text='Pow', bd=12, height=2, width=6, font=('ariel', 12, 'bold'),
                  command=lambda: btnClick('**'))
btnPower.grid(row=5, column=0)

btnRightBracket = Button(root, text=')', bd=12, height=2, width=6, font=('ariel', 12, 'bold'),
                         command=lambda: btnClick(')'))
btnRightBracket.grid(row=5, column=2)
btnLeftBracket = Button(root, text='(', bd=12, height=2, width=6, font=('ariel', 12, 'bold'),
                        command=lambda: btnClick('('))
btnLeftBracket.grid(row=5, column=1)

btnc = Button(root, text='clear', bd=12, height=2, width=6, font=('ariel', 12, 'bold'), command=btnClear)
btnc.grid(row=5, column=3)
root.mainloop()
