import tkinter as tk
from tkinter import messagebox

def create_gui(list):
    selected_antigens = []

    def submit_selection():
        nonlocal selected_antigens
        selected_indices = antigen_listbox.curselection()
        if len(selected_indices) > 10:
            messagebox.showwarning("Warning", "Please select maximum 10 antigens.")
        else:
            selected_antigens = [list[idx] for idx in selected_indices]
            messagebox.showinfo("Selected Antigens", f"Selected Antigens: {', '.join(selected_antigens)}")
            root.destroy()

    root = tk.Tk()
    root.title("Antigen Selection")
    root.geometry("200x500")

    antigen_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)

    for antigen in list:
        antigen_listbox.insert(tk.END, antigen)
    antigen_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=antigen_listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    submit_button = tk.Button(root, text="Submit", command=submit_selection)
    submit_button.pack(pady=10)

    root.mainloop()

    return selected_antigens