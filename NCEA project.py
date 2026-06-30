import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import os

DATA_FILE = "study_notes.txt"

# Main window
root = tk.Tk()
root.title("NCEA Quiz Helper")
root.geometry("900x700")

root.mainloop()

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=15, pady=15)
