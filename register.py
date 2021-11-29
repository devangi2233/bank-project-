from tkinter import*
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("1548x800+0+0")
root.title("Bank Registration")

###Frame

left_frame = Frame(root, width=774, height=800, background='dark turquoise',bd=0)
left_frame.pack(side=LEFT)

right_frame = Frame(root, width=774, height=800, background='gray20',bd=0)
right_frame.pack(side=RIGHT)

###Left frame###
l_label = Label(left_frame, text='Welcome to\n Bank of Mumbai', bg='dark turquoise', fg='gray20', font=('Times new roman', 45, 'bold'))
l_label.place(x=150,y=100)

####variables#####3
var_fname = StringVar()
var_username = StringVar()
var_contact = StringVar()
var_email = StringVar()
var_pswd = StringVar()
var_confirm_pswd = StringVar()
var_check = IntVar()

###Functions
def register_data():
    if var_fname.get()== "" or var_username.get()=="" or var_email.get()== "":
        messagebox.showerror("Error","All fields are required")
    elif var_pswd.get() != var_confirm_pswd.get():
        messagebox.showerror("Error","Password and Confirm Password must be same")
    elif var_check.get == 0:
        messagebox.showerror("Error","Please agree our terms and conditions")
    else:
        try:
            conn = mysql.connector.connect(host='localhost',username='root', password='',port=3306,database='Bank')
            cur = conn.cursor()
            cur.execute("INSERT INTO register(fname, username, contact, email, password, confirmpassword) VALUES (%s,%s,%s,%s,%s,%s)",(txt_fname.get(),txt_username.get(),txt_contact.get(),txt_email.get(),txt_pswd.get(),txt_confirm_pswd.get()))
            conn.commit()
            messagebox.showinfo("Success","Register successfully")
            root.destroy()
            import login
        except Exception as es:
            messagebox.showerror("Error",f"error due to : {str(es)}")


def login_window():
    root.destroy()
    import login
 


##Right Frame###
register_lbl = Label(right_frame, text='Register Here',font=('times new roman',35,'bold'), fg='dark turquoise', bg='gray20')
register_lbl.place(x=50, y=100)

fname = Label(right_frame, text='Name', font=('times new roman',20,'bold'),fg='dark turquoise', bg='gray20')
fname.place(x=50,y=200)

txt_fname = Entry(right_frame, font=('times new roman', 18), textvariable=var_fname,fg='gray8',bg='dark turquoise', width=25)
txt_fname.place(x=50, y=250)

username = Label(right_frame, text='Username', font=('times new roman',20,'bold'),fg='dark turquoise', bg='gray20')
username.place(x=420,y=200)

txt_username = Entry(right_frame, font=('times new roman', 18), textvariable=var_username,fg='gray8',bg='dark turquoise', width=25)
txt_username.place(x=420, y=250)

contact = Label(right_frame, text='Contact No', font=('times new roman',20,'bold'),fg='dark turquoise', bg='gray20')
contact.place(x=50,y=320)

txt_contact = Entry(right_frame, font=('times new roman', 18), textvariable=var_contact,fg='gray8',bg='dark turquoise', width=25)
txt_contact.place(x=50, y=370)

email = Label(right_frame, text='Email', font=('times new roman',20,'bold'),fg='dark turquoise', bg='gray20')
email.place(x=420,y=320)

txt_email = Entry(right_frame, font=('times new roman', 18), textvariable=var_email,fg='gray8',bg='dark turquoise',width=25)
txt_email.place(x=420, y=370)


pswd = Label(right_frame, text='Password', font=('times new roman',20,'bold'),fg='dark turquoise', bg='gray20')
pswd.place(x=50,y=440)

txt_pswd = Entry(right_frame, font=('times new roman', 18), textvariable=var_pswd,fg='gray8',bg='dark turquoise',width=25,show='*')
txt_pswd.place(x=50, y=490)

confirm_pswd = Label(right_frame, text='Confirm Password', font=('times new roman',20,'bold'),fg='dark turquoise', bg='gray20')
confirm_pswd.place(x=420,y=440)

txt_confirm_pswd = Entry(right_frame, font=('times new roman', 18), textvariable=var_confirm_pswd,fg='gray8',bg='dark turquoise',width=25,show='*')
txt_confirm_pswd.place(x=420, y=490)

chkbtn = Checkbutton(right_frame, text='I Agree The Terms And Condition',font=('times new roman',20,'bold'),fg='dark turquoise',bg='gray20', variable=var_check,activebackground='gray20',activeforeground='dark turquoise')
chkbtn.place(x=50, y=560)

register_img = PhotoImage(file='register.png')
register_btn = Button(right_frame, image=register_img,command=register_data,cursor='hand2',bd=0, bg='gray20',activebackground='gray20')
register_btn.place(x=180, y=650)

login_img = PhotoImage(file='login.png')
login_btn = Button(right_frame, image=login_img,cursor='hand2',bd=0, bg='gray20',activebackground='gray20',command=login_window)
login_btn.place(x=420, y=650)


######Function


root.mainloop()
