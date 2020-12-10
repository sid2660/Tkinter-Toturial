from tkinter import *
from PIL import Image, ImageTK
sid_root = Tk()

sid_root.geometry("455x244")
## Image 
photo = PhotoImage(file = 'save.png')
## Label
sid_label = Label(image = photo)
sid_label.pack()



sid_root.mainloop()