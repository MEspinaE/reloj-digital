import tkinter as tk
import time

def actualiza_reloj():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, actualiza_reloj)  

root = tk.Tk()
root.title("Reloj Digital")

clock_label = tk.Label(root, font=("Arial", 35))
clock_label.pack()

actualiza_reloj() 

root.mainloop()
