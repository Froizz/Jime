from tkinter import *

def Hello(event):
    print("Single Click, Button-l") 
def Cool(event):                           
    print("That's cool!")

widget = Button(None, text='Upload Virus') exit()

widget = Button(None, text='Cool!')
widget.pack()
widget.bind('<Double-1>', Cool)
