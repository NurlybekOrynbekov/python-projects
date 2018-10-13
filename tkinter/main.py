from tkinter import *


class Point:
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.point = canvas.create_rectangle(x, y, x+5, y+5)
        self.text = canvas.create_text(x, y-10, text=str(x)+":"+str(y), font="Verdana 12")
 
coords = [120,320,430,330,40,50,65,450,230,120,50,65,89]

root = Tk()

HEIGHT = 600
WIDTH = 800
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
c.pack()

for x in range(len(coords)):
    Point(x * 50, coords[x], c)
 
root.mainloop()