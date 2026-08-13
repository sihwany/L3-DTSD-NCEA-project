import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import os

DATA_FILE = "study_notes.txt"

# Main window
root = tk.Tk()
root.title("NCEA Quiz Helper")
root.geometry("900x700")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=15, pady=15)


# Study Notes Tab
notes_tab = ttk.Frame(notebook)
notebook.add(notes_tab, text="Study Notes")

ttk.Label(notes_tab, text="Study Notes", font=("Arial", 12, "bold")).pack(pady=10)

notes_box = scrolledtext.ScrolledText(notes_tab, height=20, font=("Arial", 10))
notes_box.pack(padx=20, pady=10, fill="both", expand=True)

# Load notes from file
try:
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        content = file.read()
    notes_box.insert(tk.END, content)
except:
    notes_box.insert(tk.END, "Could not load ncea_study_notes.txt")

notes_box.config(state="disabled")


root.mainloop()