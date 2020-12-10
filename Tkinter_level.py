from tkinter import *

sid_root = Tk()
##_________________________________________________________
## Width x Height
sid_root.geometry("444x234")

##Width, Height
sid_root.minsize(300,100)

##Width, Height
sid_root.maxsize(1200,988)

sid = Label(text="This is a Label")
sid.pack()






## Main loop
sid_root.mainloop()