from tkinter import *

class ColorButton:
    def __init__(self, master, color, e):
        self.e = e
        self.button = Button(master, bg=color, width = 25, command = self.printColor)
        self.color = color
        self.button.pack()

    def printColor(self):
        self.e.delete(0, END)
        self.e.insert(0, self.color)

root = Tk()


e = Entry(root)
e.pack()


button1 = ColorButton(root, "#ff0000", e)
button2 = ColorButton(root, "#ff7d00", e)
button3 = ColorButton(root, "#ffff00", e)
button4 = ColorButton(root, "#00ff00", e)
button5 = ColorButton(root, "#007dff", e)
button6 = ColorButton(root, "#0000ff", e)
button7 = ColorButton(root, "#7d00ff", e)





root.mainloop()