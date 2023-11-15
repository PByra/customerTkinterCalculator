import tkinter as tk
from tkinter import ttk


class main_application(tk.Frame):
        def __init__(self, parent, *args, **kwargs):
              tk.Frame.__init__(self, parent, *args, **kwargs)
              self.parent = parent 
              root.title("my application")
              root.geometry("562x768")


        #started button functionality 
        def button_func(self):
            print('a button was pressed')




if __name__ == "__main__":
    root = tk.Tk()
    main_application(root)
    root.mainloop()