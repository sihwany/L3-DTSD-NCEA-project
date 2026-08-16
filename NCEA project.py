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
    notes_box.insert(tk.END, "Could not load study_notes.txt")

notes_box.config(state="disabled")

#generating Quiz
questions = []

def generate_quiz():
    global questions
    questions = []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()
    except:
        messagebox.showerror("Error", "Could not read notes file")
        return

    blocks = [b.strip() for b in content.split("\n\n") if b.strip()]

    for block in blocks:
        lines = [line.strip() for line in block.split("\n") if line.strip()]
        if len(lines) < 4:
            continue

        title = lines[0]
        correct = lines[1]
        wrongs = lines[2:]

        while len(wrongs) < 3:
            wrongs.append("This statement is incorrect.")

        distractors = random.sample(wrongs, 3)
        options = [correct] + distractors
        random.shuffle(options)

        correct_letter = ["A", "B", "C", "D"][options.index(correct)]

        questions.append({
            "question": f"Which of the following statements about {title} is correct?",
            "options": {
                "A": options[0],
                "B": options[1],
                "C": options[2],
                "D": options[3]
            },
            "correct": correct_letter
        })

    messagebox.showinfo("Success", f"Generated {len(questions)} questions!")

ttk.Button(notes_tab, text="Start The Quiz", command=generate_quiz).pack(pady=15)

root.mainloop()