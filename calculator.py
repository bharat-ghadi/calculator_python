from tkinter import *
from tkinter import font as tkFont

def btnClick(number):
    global val
    val += str(number)
    data.set(val)

def btnClear():
    global val
    val = ''
    data.set('')

def btnEqual():
    global val
    try:
        result = str(eval(val))
        data.set(result)
    except Exception as e:
        data.set("Error")
        print(f"Error: {e}")
        val = ''

def keyPress(event):
    key = event.char
    if key.isdigit() or key in '+-*/.':
        btnClick(key)
    elif key == '\r':  # Enter key
        btnEqual()
    elif key == '\x1b':  # Escape key
        btnClear()

def clearAll(event=None):
    btnClear()

# Initialize the main window
root = Tk()
root.title('My Stylish Calculator')
root.geometry('400x500')
root.configure(bg='#2C3E50')

val = ''
data = StringVar()

# Create the display entry widget
display = Entry(root, textvariable=data, bd=10, bg='#34495E', fg='white', justify='right', font=('Arial', 24))
display.grid(row=0, columnspan=4, padx=10, pady=10)

# Function to create buttons with styling
def create_button(text, row, column, command):
    button = Button(root, text=text, bd=5, height=2, width=6, font=('Arial', 14),
                    bg='#2980B9', fg='white', activebackground='#3498DB', activeforeground='white', command=command)
    button.grid(row=row, column=column, padx=5, pady=5)
    return button

# First row of buttons
create_button('7', 1, 0, lambda: btnClick(7))
create_button('8', 1, 1, lambda: btnClick(8))
create_button('9', 1, 2, lambda: btnClick(9))
create_button('+', 1, 3, lambda: btnClick('+'))

# Second row of buttons
create_button('4', 2, 0, lambda: btnClick(4))
create_button('5', 2, 1, lambda: btnClick(5))
create_button('6', 2, 2, lambda: btnClick(6))
create_button('-', 2, 3, lambda: btnClick('-'))

# Third row of buttons
create_button('1', 3, 0, lambda: btnClick(1))
create_button('2', 3, 1, lambda: btnClick(2))
create_button('3', 3, 2, lambda: btnClick(3))
create_button('*', 3, 3, lambda: btnClick('*'))

# Fourth row of buttons
create_button('0', 4, 1, lambda: btnClick(0))
create_button('/', 4, 2, lambda: btnClick('/'))
create_button("=", 4, 3, btnEqual)
create_button('.', 4, 0, lambda: btnClick('.'))

# Fifth row of buttons
create_button('Pow', 5, 0, lambda: btnClick('**'))
create_button(')', 5, 2, lambda: btnClick(')'))
create_button('(', 5, 1, lambda: btnClick('('))
create_button('Clear', 5, 3, btnClear)

# Bind keyboard events to the main window
root.bind('<Key>', keyPress)

# Bind Shift + Delete to clear all
root.bind('<Shift-Delete>', clearAll)

# Start the main event loop
root.mainloop()
