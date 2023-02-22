import tkinter as tk

def button_clicked():
     miles = entry.get()
     kms = float(miles) * 1.6
     Lable_3.config(text=f"{kms}")

window = tk.Tk()
window.title("My First GUI")
#window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
entry = tk.Entry(width=10)
entry.grid(column=2, row=0)
button = tk.Button(text="Convert", command=button_clicked)
button.grid(column=2, row=2)
Lable_1 = tk.Label(text="Miles")
Lable_1.grid(column=3, row=0)
Lable_2 = tk.Label(text="is equal to ")
Lable_2.grid(column=1, row=1)
Lable_3 = tk.Label(text="")
Lable_3.grid(column=2, row=1)
Lable_4 = tk.Label(text="Kilometers")
Lable_4.grid(column=3, row=1)
window.mainloop()