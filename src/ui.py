import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk


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

max_details = Image.open("../data/maxwell_formula_details.png")
max_details = max_details.resize((1000, 400), Image.LANCZOS)
max_details_photo = ImageTk.PhotoImage(max_details)
max_details_label = tk.Label(root, image=max_details_photo)
max_details_label.grid(row=2, column=1, padx=5, pady=5)

def run_loop():
    root.mainloop()