import requests, bs4
from tkinter import Tk, Label

root = Tk()
root.title("Funserials")
root.geometry("1000x600")    

s = requests.get('http://fanserials.care/new/')
b = bs4.BeautifulSoup(s.text, 'html.parser')

serials=b.select('.serial-bottom')
row = 0
for serial in serials:
    title = serial.select('.field-title')
    description = serial.select('.field-description')
    Label(root, text=title[0].getText(), font=16, height=1).grid(row=row,column=0)
    Label(root, text=description[0].getText(), font=16, height=1).grid(row=row,column=1)
    row+=1

root.mainloop()

