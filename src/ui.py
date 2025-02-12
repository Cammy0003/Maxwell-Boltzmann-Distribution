import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Maxwell Bol")
        self.title("Maxwell Boltzmann Distribution")
        self.geometry('1120x720')

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Allow the container to expand
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        self.frames = {}

        """HomePage, CalculationPage, PeriodicTablePage DisplayPage"""
        for PageClass in (HomePage, CalculationPage):
            page = PageClass(self.container, self)
            self.frames[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)


        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # main title setup
        title_font = font.Font(family="Times New Roman", size=50, weight="bold")
        self.title = tk.Label(self, text="Maxwell Boltzmann Distribution", font=title_font,)
        self.title.grid(row=0, column=1, padx=5, pady=5)

        # Maxwell Formula display
        max_image = Image.open("../data/maxwell_formula.png")
        max_image = max_image.resize((700, 150), Image.LANCZOS)
        self.max_photo = ImageTk.PhotoImage(max_image)
        self.max_label = tk.Label(self, image=self.max_photo)
        self.max_label.grid(row=1, column=1, padx=5, pady=5)

        # Maxwell Formula Details
        max_details = Image.open("../data/maxwell_formula_details.png")
        max_details = max_details.resize((1000, 400), Image.LANCZOS)
        self.max_details_photo = ImageTk.PhotoImage(max_details)
        self.max_details_label = tk.Label(self, image=self.max_details_photo)
        self.max_details_label.grid(row=2, column=1, padx=5, pady=5)

        # Calculation Button
        button_font = font.Font(family="Times New Roman", size=20, weight="bold")
        self.calculation_button = tk.Button(
            self,
            text="Calculate",
            font=button_font,
            command=lambda: controller.show_frame(CalculationPage),
            borderwidth=5,
            relief="ridge",
            padx=10,
            pady=5
        )
        self.calculation_button.grid(row=3, column=1, padx=5, pady=5)


class CalculationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.title = tk.Label(self, text="test")
        self.title.grid(row=0, column=1, padx=5, pady=5)



'''
class PeriodicTablePage(tk.Frame):

class DisplayPage(tk.Frame):
'''

'''
# main window setup
root = tk.Tk()

root.title("Maxwell Boltzmann Distribution")
root.geometry('1120x720')
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# main title setup
title_font = font.Font(family="Times New Roman", size=50, weight="bold")
title = tk.Label(
    root,
    text="Maxwell Boltzmann Distribution",
    font=title_font,
)
title.grid(row=0, column=1, padx=5, pady=5)

# Maxwell Formula display
max_image = Image.open("../data/maxwell_formula.png")
max_image = max_image.resize((700, 150), Image.LANCZOS)
max_photo = ImageTk.PhotoImage(max_image)
max_label = tk.Label(root, image=max_photo)
max_label.grid(row=1, column=1, padx=5, pady=5)

# Maxwell Formula Details
max_details = Image.open("../data/maxwell_formula_details.png")
max_details = max_details.resize((1000, 400), Image.LANCZOS)
max_details_photo = ImageTk.PhotoImage(max_details)
max_details_label = tk.Label(root, image=max_details_photo)
max_details_label.grid(row=2, column=1, padx=5, pady=5)



def run_loop():
    root.mainloop()

'''