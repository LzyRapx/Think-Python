#coding:utf-8

from swampy.Gui import *

g = Gui()
g.title('GUI')

def create_button():
    g.bu(text='I am the new button. Press me!', command=make_label)

def make_label():
    g.la(text='Thank you.')

button1 = g.bu(text='Please press me.', command=create_button)

button1

g.mainloop()

