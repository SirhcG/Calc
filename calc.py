from tkinter import *

root = Tk()
root.title('Calculator')

large_font = ('Veranda', 24)

e = Entry(root, width = 15, borderwidth = 5, font = large_font, justify = 'right')
e.grid(row = 0, column = 0, columnspan = 10, padx = 10, pady = 10)

#Global variables

First_val = ''
Second_val = ''
Symbol = ''
Reset = ''

def button_press(number):
    global Reset

    if Reset == 'R':
        e.delete(0, END)
        Reset = ''
    digit = e.get()
    e.delete(0, END)
    e.insert(0, str(digit) + str(number))
    
def clear():
    e.delete(0, END)

def add():
    global First_val
    global Symbol
    Symbol = '+'
    First_val = e.get()
    e.delete(0, END)

def sub():
    global First_val
    global Symbol
    Symbol = '-'
    First_val = e.get()
    e.delete(0, END)

def mul():
    global First_val
    global Symbol
    Symbol = '*'
    First_val = e.get()
    e.delete(0, END)

def div():
    global First_val
    global Symbol
    Symbol = '/'
    First_val = e.get()
    e.delete(0, END)

def equal():
    global First_val
    global Second_val
    global Symbol
    global Reset
    
    Second_val = e.get()
    
    if Symbol == '+':
        result = int(First_val) + int(Second_val)
        e.delete(0, END)
        e.insert(0, result)
        Reset = 'R'
        
    elif Symbol == '-':
        result = int(First_val) - int(Second_val)
        e.delete(0, END)
        e.insert(0, result)
        Reset = 'R'
        
    elif Symbol == '*':
        result = int(First_val) * int(Second_val)
        e.delete(0, END)
        e.insert(0, result)
        Reset = 'R'
        
    elif Symbol == '/':
        if int(Second_val) > 0 or int(Second_val) < 0:
            result = int(First_val) / int(Second_val)
            e.delete(0, END)
            e.insert(0, result)
            Reset = 'R'
            
        else:
            First_val = ''
            Second_val = ''
            e.delete(0, END)
            e.insert(0, 'ERROR')
            Reset = 'R'
    
    

#Buttons    

button_1 = Button(root, text = '1', padx = 40, pady = 20, command = lambda: button_press(1))
button_2 = Button(root, text = '2', padx = 40, pady = 20, command = lambda: button_press(2))
button_3 = Button(root, text = '3', padx = 40, pady = 20, command = lambda: button_press(3))
button_4 = Button(root, text = '4', padx = 40, pady = 20, command = lambda: button_press(4))
button_5 = Button(root, text = '5', padx = 40, pady = 20, command = lambda: button_press(5))
button_6 = Button(root, text = '6', padx = 40, pady = 20, command = lambda: button_press(6))
button_7 = Button(root, text = '7', padx = 40, pady = 20, command = lambda: button_press(7))
button_8 = Button(root, text = '8', padx = 40, pady = 20, command = lambda: button_press(8))
button_9 = Button(root, text = '9', padx = 40, pady = 20, command = lambda: button_press(9))
button_0 = Button(root, text = '0', padx = 40, pady = 20, command = lambda: button_press(0))
button_equal = Button(root, text = '=', padx = 40, pady = 20, command = lambda: equal())
button_add = Button(root, text = '+', padx = 40, pady = 20, command = lambda: add())
button_sub = Button(root, text = '-', padx = 40, pady = 20, command = lambda: sub())
button_mul = Button(root, text = '*', padx = 40, pady = 20, command = lambda: mul())
button_div = Button(root, text = '/', padx = 40, pady = 20, command = lambda: div())
button_clear = Button(root, text = 'c', padx = 40, pady = 20, command = lambda: clear())

#Buttons layout


button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_div.grid(row = 1, column = 3)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_mul.grid(row = 2, column = 3)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_sub.grid(row = 3, column = 3)

button_0.grid(row = 4, column = 0)
button_clear.grid(row = 4, column = 1)
button_equal.grid(row = 4, column = 2)
button_add.grid(row = 4, column = 3)







root.mainloop()
