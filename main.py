import customtkinter as cttk


class calculatorApp(cttk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.title("Calculator")
        cttk.set_appearance_mode("dark")
        cttk.set_default_color_theme("green")
        
        self.equation = ''
        self.expression = ''
        
        calculator_Widgets = [
            ("button", 'c', self.clear, 0, 0),
            ("button", '', None, 0, 1),
            ("button", '', None, 0, 2),
            ("button", '+', lambda: self.press('+'), 0, 3),
            ("button", '7', lambda: self.press(7), 1, 0),
            ("button", '8', lambda: self.press(8), 1, 1),
            ("button", '9', lambda: self.press(9), 1, 2),
            ("button", '-', lambda: self.press('-'), 1, 3),
            ("button", '4', lambda: self.press(4), 2, 0),
            ("button", '5', lambda: self.press(5), 2, 1),
            ("button", '6', lambda: self.press(6), 2, 2),
            ("button", 'x', lambda: self.press('*'), 2, 3),
            ("button", '1', lambda: self.press(1), 3, 0),
            ("button", '2', lambda: self.press(2), 3, 1),
            ("button", '3', lambda: self.press(3), 3, 2),
            ("button", '/', lambda: self.press('/'), 3, 3),
            ("button", '0', lambda: self.press(0), 4, 0),
            ("button", 'pi', lambda: self.press(3.141), 4, 1),
            ("button", 'e', lambda: self.press(2.718), 4, 2),
            ("button", '=', self.equals, 4, 3),
        ]

        self.text_box = cttk.CTkEntry(self, textvariable = self.expression, height = 100, width = 580, font = ('Arial', 90))
        self.text_box.grid(padx = 10, pady = 10)

        functionality_frame = frame_Gen(master = self, widgets = calculator_Widgets)
        functionality_frame.grid(padx = 0, pady = 15, sticky = "s")
    

    def press(self, num):
        self.equation += str(num)
        self.text_box.delete(0, 'end')
        self.text_box.insert('end', self.equation)


    def equals(self):
        try: 
            self.total = str(eval(self.equation))
            self.text_box.delete(0, 'end')
            self.text_box.insert('end', self.total)
            self.equation = self.total
        except:
            self.text_box.delete(0, 'end')
            self.text_box.insert('end', 'error')
            

    def clear(self): 
        self.equation = '' 
        self.text_box.delete(0, 'end')
        self.text_box.insert('end', self.equation)

            

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


def main(): 
    app = calculatorApp()
    app.mainloop()


if __name__ == '__main__':
    main()