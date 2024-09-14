import customtkinter



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Xcrapper")
        self.geometry("1102x630")
        self.resizable(False, False)
        self.screen_width=self.winfo_screenwidth()
        self.screen_height=self.winfo_screenheight()
        self.x=(self.screen_width/2)-(1102/2)
        self.y=(self.screen_height/2)-(630/2)
        self.geometry(f"{1102}x{630}+{int(self.x)}+{int(self.y)}")
        self.configure(bg = "#232844")
        




app = App()
app.mainloop()