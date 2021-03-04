from tkinter import *

root = Tk()

canvas = Canvas(width=400, height=400, bg='blue')
canvas.pack()
canvas.create_rectangle(100,100,300,300, fill="yellow", outline="yellow")
