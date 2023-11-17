import customtkinter as cttk


class calculatorApp(cttk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.title("Calculator")
        
        self.equation = cttk.StringVar()
        self.expression = cttk.StringVar()
        
        calculator_Widgets = [
            ("button", "c", None, 0, 0),
            ("button", "(", None, 0, 1),
            ("button", ")", None, 0, 2),
            ("button", "+", None, 0, 3),
            ("button", "7", None, 1, 0),
            ("button", "8", None, 1, 1),
            ("button", "9", None, 1, 2),
            ("button", "-", None, 1, 3),
            ("button", "4", None, 2, 0),
            ("button", "5", None, 2, 1),
            ("button", "6", None, 2, 2),
            ("button", "x", None, 2, 3),
            ("button", "1", None, 3, 0),
            ("button", "2", None, 3, 1),
            ("button", "3", None, 3, 2),
            ("button", "/", None, 3, 3),
            ("button", "0", lambda: self.press(0), 4, 0),
            ("button", "pi", None, 4, 1),
            ("button", "e", None, 4, 2),
            ("button", "=", None, 4, 3),
        ]

        text_box = cttk.CTkEntry(self, textvariable = self.expression, height = 100, width = 580, font = ('Arial', 90))
        text_box.grid(padx = 10, pady = 10)

        functionality_frame = frame_Gen(master = self, widgets = calculator_Widgets)
        functionality_frame.grid(padx = 0, pady = 15, sticky = "s")
    
    def press(self, num): 
        self.expression.set(self.equation.get() + str(num))
            


class frame_Gen(cttk.CTkFrame):
    def __init__(self, master, widgets, **kwargs):
        super().__init__(master, **kwargs)

        #this is a poor way of doing this and may lead to issues later as we add widgets
        #and adjust them as the tuple passed will need to contain many 'None' values, 
        #I will come back to this later, however at this time I would like to work on the 
        #functionality of the apps
        for row, widget_info in enumerate(widgets): 
            widget_type, widget_text, widget_command, widget_row, widget_column = widget_info

            if widget_type == "button":
                widget = cttk.CTkButton(self, text=widget_text, command = widget_command)
            elif widget_type == "label":
                widget = cttk.CTkLabel(self, text=widget_text)
            else:
                #place holder for other widgets 
                continue

            widget.grid(row = widget_row, column = widget_column)


class App(cttk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Appliation")
        self.geometry("400x600")
        cttk.set_appearance_mode("dark")
        cttk.set_default_color_theme("green")
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)

        main_Widgets = [
            ("label", "Here are the Applications", None, None, None),
            ("button", "Calculator App", self.button_Calculator, None, None),
            ("button", "Sales Finder App", self.button_SalesFinder, None, None),
            ("button", "Tangerine Finance App", self.button_TangerineFinance, None, None)
        ]


        frame1 = frame_Gen(master = self, widgets = main_Widgets)
        frame1.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = "nsew")


    def button_Calculator(self):
        calculator_instance = calculatorApp()
        calculator_instance.mainloop()
        print("Calculator app Opened")

    def button_SalesFinder(self):
        print("SalesFinder App Opened")

    def button_TangerineFinance(self):
        print("Tangerine Finance App Opened")

    
def main(): 
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()