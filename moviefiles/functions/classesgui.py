import customtkinter as ctk

class CustomButton(ctk.CTkButton):
    def __init__(self, master, text="Button", command=None):
        super().__init__(master, text=text, command=command)
        self.pack(pady=12, padx=10)

class CustomCheckBox(ctk.CTkCheckBox):
    def __init__(self, master, text, variable):
        super().__init__(master, text=text, variable=variable)
        self.pack(pady=12, padx=10)

class CustomEntry(ctk.CTkEntry):
    def __init__(self, master, placeholder_text=""):
        super().__init__(master=master, placeholder_text=placeholder_text)
        self.pack(pady=12, padx=10)