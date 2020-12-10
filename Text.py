from tkinter import *

root = Tk()

root.geometry("600x300")
root.minsize(400,200)
root.title("My GUI")

## _______________________Important Label options ____________________________________
    ## text = add the text
    ## bd = Background
    ## fg = Foreground
    ## font = sets the font
    ## padx = x paddings
    ## pady = y paddings
    ## relif =  border styling ,, SUNKEN, RAISED, GROOV, RIDGE
    
###-------------------___________________________________________________________

title_label = Label(text= '''  Since the release of java in 1995, Sun Microsystems has been constantly upgrading its products\n to enable users devlop and deploy java solutions with ease and confidence.
                    \n Java platform, Standerd Edition (Java SE)  software is the leading\n platform for devloping and deploying portable 
                    applications that run on server and desktop systems spanning most operating systems. ''',
                    bg= 'black',fg='white',padx=20,pady=20,font = ("Arial",20,'bold'))
                    
title_label.pack()






root.mainloop()
