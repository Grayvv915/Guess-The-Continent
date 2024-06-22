import tkinter as tk

root = tk.Tk()
root.resizable(False,False)
root.attributes("-fullscreen", False)
root.overrideredirect(0)
root.geometry("400x200+600+200")
root.title(string="Guess The Continent")

tk.Label(root, text="# Bienvenido a Guess The Continent // Adivina El Continente. #",
         font="Arial 10", pady=10, fg="red").pack()
tk.Label(root, text="Se nombrarán 10 países. Tienes que escoger el continente en el que se sitúan; Europa, América, África, Asia u Oceanía.",
         font="Arial 10", wraplength=400, pady=10).pack()

def start():
    root.destroy()
    import play

tk.Button(root, text="Comenzar", padx=5, pady=5, command=start).place(x=160 ,y=125)

root.mainloop()