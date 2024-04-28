import tkinter as tk
from tkinter import messagebox
import json
import random


def load_vocabularies(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise Exception("The specified file was not found.")


def check_answer():
    global vocab_list, current_vocab
    user_input = entry_var.get()
    if (
        user_input.strip().lower().replace("(to)", "").replace("to", "").strip()
        == current_vocab["English"]
        .lower()
        .replace("(to)", "")
        .replace("to", "")
        .strip()
    ):
        proceed_to_next()
    else:
        vocab_list.insert(
            0, current_vocab
        )  # Re-insert the vocab at the first position if the answer is wrong
        show_correction(user_input)


def show_correction(user_input):
    correction_label.config(
        text=f"Correct: {current_vocab['English']}\nYour Answer: {user_input}"
    )
    entry_var.set("")
    root.after(
        5000, proceed_to_next
    )  # Display the correction for 2 seconds, then proceed


def proceed_to_next():
    global vocab_list, current_vocab
    if vocab_list:
        current_vocab = vocab_list.pop(0)
        word_label.config(
            text=f"Translate (German to English): {current_vocab['German']} ({len(vocab_list)+1} words left)"
        )
        entry_var.set("")
        correction_label.config(text="")
    else:
        show_end_screen()


def show_end_screen():
    messagebox.showinfo("Congratulations!", "You have completed the quiz!")
    root.destroy()


# Load vocabulary data
vocab_list = load_vocabularies("vocabularies/unit4.json")
random.shuffle(vocab_list)
current_vocab = vocab_list.pop(0) if vocab_list else None

# Set up the GUI
root = tk.Tk()
root.title("Vocabulary Trainer")

word_label = tk.Label(
    root,
    text=f"Translate to English:\n\n{current_vocab['German']}\n\n({len(vocab_list)+1} words left)",
)
word_label.pack(pady=20)

entry_var = tk.StringVar()
answer_entry = tk.Entry(root, textvariable=entry_var)
answer_entry.pack()

correction_label = tk.Label(root, text="", fg="red")
correction_label.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=20)

root.mainloop()
