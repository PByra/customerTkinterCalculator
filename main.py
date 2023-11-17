import customtkinter as cttk

class frame_Gen(cttk.CTkFrame):
    def __init__(self, master, widgets, **kwargs):
        super().__init__(master, **kwargs)


        #this is a poor way of doing this and may lead to issues later as we add widgets
        #and adjust them as the tuple passed will need to contain many 'None' values, 
        #I will come back to this later, however at this time I would like to work on the 
        #functionality of the apps
        for row, widget_info in enumerate(widgets): 
            widget_type, widget_text, widget_command = widget_info

            if widget_type == "button":
                widget = cttk.CTkButton(self, text=widget_text, command = widget_command)
            elif widget_type == "label":
                widget = cttk.CTkLabel(self, text=widget_text)
            else:
                #place holder for other widgets 
                continue

            widget.pack(pady = 5, padx = 10)



class App(cttk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        cttk.set_appearance_mode("dark")
        cttk.set_default_color_theme("green")
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)

        main_Widgets = [
            ("label", "Here are the Applications", None),
            ("button", "Calculator App", self.button_Calculator),
            ("button", "Sales Finder App", self.button_SalesFinder),
            ("button", "Tangerine Finance App", self.button_TangerineFinance)
        ]


        frame1 = frame_Gen(master=self, widgets=main_Widgets)
        frame1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


    def button_Calculator(self):
        print("Calculator app Opened")

    def button_SalesFinder(self):
        print("SalesFinder App Opened")

    def button_TangerineFinance(self):
        print("Tangerine Finance App Opened")

    



app = App()
app.mainloop()
