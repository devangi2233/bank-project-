from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk


root = Tk()
root.geometry("1558x800+0+0")
root.title("Customer control")
root.config(background='dark turquoise')

###Top frame
top_frame = Frame(root,bg="gray20")
top_frame.place(x=0,y=0,width=1550,height=90)

staff_lbl = Label(top_frame, text="Customer Control Dashboard", bg="gray20", fg="dark turquoise", font=("times new roman",45,"bold"))
staff_lbl.place(x=420, y= 5)


root.mainloop()
