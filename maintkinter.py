import tkinter as tk
from tkinter import ttk as tema
from tkinter.messagebox import showinfo
import ttkbootstrap as tb

root = tb.Window(themename="solar")

name_var = tk.StringVar()
kelas_var = tk.IntVar()
jk_var = tk.StringVar()
ba_var = tk.StringVar()
setuju_var = tk.IntVar()

def send():
    if setuju_var.get() == 1:
        stj = "bersedia"
    else:
        stj = "tidak bersedia"

    h = f"halo nama saya {name_var.get()} jenis kelamin {jk_var.get()} di kelas {kelas_var.get()} dan saya {stj} mengerjakan projek bahasa asing {ba_var.get()} "
    showinfo(title="BIOGRAFI", message=h)

root.title("BIO")
root.geometry("1000x500")
root.resizable(False, False)
root.config(bg="gray")

frame = tema.Frame(root)
frame.pack(padx=10, pady=10, fill="x", expand=True)

# Name Label and Entry
name_label = tema.Label(frame, text="NAME = ", font=("arial", 12, 'bold'))
name_label.pack(padx=10, pady=10, fill="x", expand=True)
name_entry = tema.Entry(frame, textvariable=name_var)
name_entry.pack(padx=10, pady=10, fill="x", expand=True)

# Class Label and Entry
class_label = tema.Label(frame, text="CLASS = ", font=("arial", 12, 'bold'))
class_label.pack(padx=10, pady=10, fill="x", expand=True)
class_entry = tema.Entry(frame, textvariable=kelas_var)
class_entry.pack(padx=10, pady=10, fill="x", expand=True)

# Gender Label and Combobox
gender_label = tema.Label(frame, text="JENIS KELAMIN = ", font=("arial", 12, 'bold'))
gender_label.pack(padx=10, pady=10, fill="x", expand=True)
gender_combobox = tema.Combobox(frame, textvariable=jk_var, values=["laki-laki", "perempuan"])
gender_combobox.pack(padx=10, pady=10, fill="x", expand=True)

# BA Label and Radiobuttons
ba_label = tema.Label(frame, text="BA :")
ba_label.pack(padx=10, fill="x", expand=True)
ba1 = tema.Radiobutton(frame, value="dkv", text="dkv", variable=ba_var)
ba1.pack(padx=10, fill="x", expand=True)
ba2 = tema.Radiobutton(frame, value="coding", text="coding", variable=ba_var)
ba2.pack(padx=10, fill="x", expand=True)

# Agreement Checkbutton
agreement_checkbutton = tema.Checkbutton(frame, variable=setuju_var, text="Saya setuju mengerjakan Project Akhir ..", onvalue=1, offvalue=0)
agreement_checkbutton.pack(padx=10, fill="x", expand=True)

# Submit Button
submit_button = tema.Button(frame, text="SUBMIT", command=send)
submit_button.pack(padx=10, pady=10, fill="x", expand=True)

root.mainloop()