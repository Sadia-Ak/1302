# Sadia Akther 
# sakther1@student.gsu.edu

import tkinter as tk

window = tk.Tk()
window.title("Shapes")
window.geometry("600x600")


canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()

# square
canvas.create_rectangle(50, 50, 150, 150, fill="red")

# rectangle with a border
canvas.create_rectangle(500, 500, 600, 600, outline="green", width=2)
canvas.create_rectangle(500, 500, 600, 600, width=0, fill="")

# triangle with dashed lines as a border
canvas.create_polygon(300, 100, 200, 300, 400, 300, outline="black", dash=(4, 4))

window.mainloop()
