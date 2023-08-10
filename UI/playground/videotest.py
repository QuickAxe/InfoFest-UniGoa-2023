import tkinterweb as tkw
from tkinter import *

root = Tk()

frame = tkw.HtmlFrame(root)
frame.load_website("https://youtube.com")
frame.pack()

root.mainloop()

