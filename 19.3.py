#coding:utf-8

from swampy.Gui import *

g = Gui()
g.title('GUI')

canvas = g.ca(width=500, height=500)
canvas.config(bg='blue')

def draw_circle():
    canvas.circle([0, 0], 100, fill='red', outline='green')

g.bu(text='Create a circle', command=draw_circle)

g.mainloop()

