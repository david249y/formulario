import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.config(width=350, height=250)
root.title("Aplica el ingreso")
frame = tk.Frame(root)
frame.place(x=0, y=0, width=350, height=250)
button = tk.Button(frame, text="click me")
button.place(x=50, y=50)
textbox = tk.Entry(frame)
textbox.insert(0,"ingrese su nombre" )
textbox.place(x=50, y=100)
checkbox = ttk.Checkbutton(frame, text="activar ia")
checkbox.place(x=50, y=150)
root.mainloop()
