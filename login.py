from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("1550x800")
root.title("Bank login")
root.config(background='dark turquoise')

frame = Frame(root, bg="gray20")
frame.place(x=450, y=150, width=650, height=500)

######function
def register_window():
    root.destroy()
    import register

def login():
    if txt_username.get() =="" or txt_password.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        try:
            conn = mysql.connector.connect(host='localhost',username='root', password='',port=3306,database='Bank')
            cur = conn.cursor()
            cur.execute("SELECT * FROM register where username=%s and password=%s",(
                txt_username.get(),
                txt_password.get()
            ))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                messagebox.showinfo("Success","Login successfully")
                root.destroy()
                import main
        
        except Exception as es:
            messagebox.showerror("Error",f"error due to : {str(es)}")\

    


lbl = Label(frame, text="Bank Of Mumbai", bg='gray20',fg="dark turquoise", font=("times new roman",35,'bold'))
lbl.place(x=120, y=30)

lbl_login = Label(frame, text="Login", bg='gray20',fg="dark turquoise", font=("times new roman",35,'bold'))
lbl_login.place(x=230, y=100)

username = Label(frame, text='Username : ', font=('times new roman',20,'bold'),fg='dark turquoise', bg='gray20')
username.place(x=30,y=180)

txt_username = Entry(frame,font=('times new roman', 18),fg='gray8',bg='dark turquoise', width=25)
txt_username.place(x=180, y=185)

password = Label(frame, text='Password : ', font=('times new roman',20,'bold'),fg='dark turquoise', bg='gray20')
password.place(x=30,y=260)

txt_password = Entry(frame,font=('times new roman', 18),fg='gray8',bg='dark turquoise', width=25,show="*")
txt_password.place(x=180, y=265)

login_img = PhotoImage(file='login.png')
login_btn = Button(frame, image=login_img,cursor='hand2',bd=0, bg='gray20',activebackground='gray20',command=login)
login_btn.place(x=120, y=350)

register_img = PhotoImage(file='register.png')
register_btn = Button(frame, image=register_img,cursor='hand2',bd=0, bg='gray20',activebackground='gray20',command=register_window)
register_btn.place(x=300, y=350)






root.mainloop()