import customtkinter as cttk

class MyFrame(cttk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Add widgets onto the frame, for example:
        self.label = cttk.CTkLabel(self, text="Frame Label")
        self.label.grid(row=0, column=0, padx=20)


class App(cttk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")  # Adjusted height to accommodate multiple frames
        self.grid_rowconfigure(0, weight=1)  # Configure grid system
        self.grid_columnconfigure(0, weight=1)

        # Create multiple frames and place them in different rows
        frame1 = MyFrame(master=self)
        frame1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        frame2 = MyFrame(master=self)
        frame2.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        frame3 = MyFrame(master=self)
        frame3.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()
