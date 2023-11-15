import tkinter as tk
from tkinter import ttk

def button_func():
    print('a button was pressed')


#create window 
window = tk.Tk() 
window.title("Window and Widgets")
window.geometry('800x500')

#Create Widgets 
text = tk.Text(master = window)
text.pack()


#ttk widgets 
label = ttk.Label(master = window, text = 'this is some text')
label.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()

#ttk button
button = ttk.Button(master = window, text = 'Button', command = button_func) 
button.pack()

#run 
window.mainloop()

