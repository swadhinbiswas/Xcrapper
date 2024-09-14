import customtkinter


class LoginFrame(customtkinter.CTkFrame,):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.title("Login")
        self.geometry("851x573")
        self.configure(bg = "#10141C")
        
        
        
        
        