import customtkinter
from PIL import Image
import os

class TitleFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")


class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class TreeFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class ProgressFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Boom ECCN")
        self.geometry("600x1000")

        # configure grid layout (3x3)
        self.grid_columnconfigure((0, 1, 2))
        self.grid_rowconfigure((0, 1, 2))


        self.title_frame = TitleFrame(self)
        self.title_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 0), sticky="nswe")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")


app = App()
app.mainloop()
