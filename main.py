#IMPORTS#
import tkinter as tk
import tkinter.messagebox 
import tkinter.ttk
from tkinter.constants import SUNKEN
import math
import random
#WINDOW SETUP#
window = tk.Tk()
window.title('Best Calculator')
frame = tk.Frame(master=window, bg="#FAF7DF", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=10, width=30)
entry.grid(row=0, column=0, columnspan=10, ipady=2, pady=2)
intvalue = 0
#VARIABLE SETUP#
dog = tk.PhotoImage(file = r"dog.png")
open = True
#FUNCTIONS#
def myclick(number):
	entry.insert(tk.END, number)
def equal():
  try:
    y = str(eval(entry.get()))
    entry.delete(0, tk.END)
    entry.insert(0, y)
  except:
    tkinter.messagebox.showinfo("Error", "Syntax Error")
def clear():
	entry.delete(0, tk.END)
def dogyears():
  try:
    y = int(entry.get())
    entry.delete(0, tk.END)
    if y < 1:
      return '1'
    elif y >= 1 and y < 2:
      return 15
    elif y >= 2 and y <3:
      return 24
    else:
      return 24 + y*5
  except:
    tkinter.messagebox.showinfo("Error", "Syntax Error")
def random_number():
  try:
    y = int(entry.get())
    entry.delete(0, tk.END)
    return str(random.randrange(y))
  except:
    tkinter.messagebox.showinfo("Error", "Syntax Error")
def prnth():
  global open
  if open:
    open = False
    return('(')
  else:
    open = True
    return(')')
    
#BUTTON 1#
button_1 = tk.Button(master=frame, bg = '#CFC7AB', activebackground='#DCD8B8', text='1', padx=10,
					pady=10, width=3, command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)
#BUTTON 2#
button_2 = tk.Button(master=frame, bg = '#CFC7AB', activebackground='#DCD8B8', text='2', padx=10, pady=10, width=3, command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
#BUTTON 3#
button_3 = tk.Button(master=frame, bg = '#CFC7AB', activebackground='#DCD8B8', text='3', padx=10, pady=10, width=3, command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
#BUTTON 4#
button_4 = tk.Button(master=frame, activebackground='#DCD8B8', bg = '#CFC7AB', text='4', padx=10, pady=10, width=3, command=lambda: (myclick(4)))
button_4.grid(row=2, column=0, pady=2)
#BUTTON 10#
button_5 = tk.Button(master=frame, bg = '#CFC7AB', activebackground='#DCD8B8', text='5', padx=10, pady=10, width=3, command=lambda: (myclick(5)))
button_5.grid(row=2, column=1, pady=2)
#BUTTON 6#
button_6 = tk.Button(master=frame, bg = '#CFC7AB', activebackground='#DCD8B8', text='6', padx=10, pady=10, width=3, command=lambda: (myclick(6)))
button_6.grid(row=2, column=2, pady=2)
#BUTTON 7#
button_7 = tk.Button(master=frame, bg = '#CFC7AB', activebackground='#DCD8B8', text='7', padx=10, pady=10, width=3, command=lambda: (myclick(7)))
button_7.grid(row=3, column=0, pady=2)
#BUTTON 8#
button_8 = tk.Button(master=frame, bg = '#CFC7AB', activebackground='#DCD8B8', text='8', padx=10, pady=10, width=3, command=lambda: (myclick(8)))
button_8.grid(row=3, column=1, pady=2)
#BUTTON 9#
button_9 = tk.Button(master=frame, bg = '#CFC7AB', activebackground='#DCD8B8', text='9', padx=10, pady=10, width=3, command=lambda: (myclick(9)))
button_9.grid(row=3, column=2, pady=2)
#BUTTON 0#
button_0 = tk.Button(master=frame, bg = '#CFC7AB', activebackground='#DCD8B8', text='0', padx=10, pady=10, width=3, command=lambda: (myclick(0)))
button_0.grid(row=4, column=1, pady=2)
#BUTTON +#
button_add = tk.Button(master=frame, bg = '#EEF0CA', activebackground='#DCD8B8', text="+", padx=10,
					pady=10, width=3, command=lambda: myclick('+'))
button_add.grid(row=6, column=0, pady=2)
#BUTTON -#
button_subtract = tk.Button(
	master=frame, bg = '#EEF0CA', activebackground='#DCD8B8', text="-", padx=10, pady=10, width=3, command=lambda: myclick('-'))
button_subtract.grid(row=6, column=1, pady=2)
#BUTTON *#
button_multiply = tk.Button(
	master=frame, bg = '#EEF0CA', activebackground='#DCD8B8', text="*", padx=10, pady=10, width=3, command=lambda: myclick('*'))
button_multiply.grid(row=6, column=2, pady=2)
#BUTTON /#
button_div = tk.Button(master=frame, bg = '#EEF0CA', activebackground='#DCD8B8', text="/", padx=10,
					pady=10, width=3, command=lambda: myclick('/'))
button_div.grid(row=6, column=3, pady=2)
#BUTTON CLEAR#
button_clear = tk.Button(master=frame, bg = '#CFC7AB', activebackground='#DCD8B8', text="clear",
						padx=7, pady=10, width=10, command=clear)
button_clear.grid(row=7, column=2, columnspan=2, pady=2)
#BUTTON =#
button_equal = tk.Button(master=frame, bg = '#CFC7AB', activebackground='#DCD8B8', text="=", padx=7,
						pady=10, width=10, command=equal)
button_equal.grid(row=7, column=0, columnspan=2, pady=2)
#BUTTON SQUARE ROOT#
button_sqrt = tk.Button(master=frame, bg = '#EEF0CA', activebackground='#DCD8B8', text="√", padx = 10, pady=10, width=3, command=lambda: myclick('**0.10'))
button_sqrt.grid(row=1, column=3, columnspan=1, pady=2)
#BUTTON EXPONENT#
button_expo = tk.Button(master=frame, bg = '#EEF0CA', activebackground='#DCD8B8', text="^x", padx = 10, pady=10, width=3, command=lambda: myclick('**'))
button_expo.grid(row=2, column=3, columnspan=1, pady=2), 
#BUTTON e#
button_e = tk.Button(master=frame, bg = '#EEF0CA', activebackground='#DCD8B8', text="e", padx = 10, pady=10, width=3, command=lambda: myclick(str(math.exp(1))))
button_e.grid(row=4, column=0, columnspan=1, pady=2)
#BUTTON pi#
button_pi = tk.Button(master=frame, bg = '#EEF0CA', activebackground='#DCD8B8', text="pi", padx = 10, pady=10, width=3, command=lambda: myclick(str(math.radians(180))))
button_pi.grid(row=4, column=2, columnspan=1, pady=2)
#BUTTON DOG YEARS#
button_dog = tk.Button(master=frame, text = 'Dog Years', bg = '#F6875F', activebackground='#AF4823', image = dog, padx = 10, pady=10, width=45, height=35, command=lambda: myclick(str(dogyears())))
button_dog.grid(row=7, column=4, columnspan=1, pady=2)
#BUTTON RANDOM 1-?#
button_1 = tk.Button(master=frame, bg = '#3BA7A8', activebackground='#457D7E', text="1-?", padx = 10, pady=10, width=3, command=lambda: myclick(random_number()))
button_1.grid(row=4, column=3, columnspan=1, pady=2)
#BUTTON ()#
button_1 = tk.Button(master=frame, bg = '#EEF0CA', activebackground='#DCD8B8', text="()", padx = 10, pady=10, width=3, command=lambda: myclick(prnth()))
button_1.grid(row=3, column=3, columnspan=1, pady=2)

window.mainloop()
