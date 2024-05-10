# GUI in python
from tkinter import *
window = Tk()  # instansiate an instance of a window
window.geometry("420x420")
window.title("First window")

icon = PhotoImage(file='D:\\python projects\\12\\images.png')
window.iconphoto(True, icon)
window.config(background="black")
window.mainloop()
