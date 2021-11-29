from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import random
import mysql.connector


root = Tk()
root.geometry("1548x800+0+0")
root.title("Staff Control Dashboard")
root.config(background='dark turquoise')


####variable
var_id = StringVar()
x = random.randint(1000, 9999)
var_id.set(str(x))

var_name = StringVar()
var_email = StringVar()
var_address = StringVar()
var_gender = StringVar()
var_dob = StringVar()
var_pswd = StringVar()
var_salary = StringVar()
var_contact = StringVar()
var_doj = StringVar()
var_type= StringVar()

####Top Frame
top_frame = Frame(root,bg="gray20")
top_frame.place(x=18,y=10,width=1500,height=100)

staff_lbl = Label(top_frame, text="Staff Control Dashboard", bg="gray20", fg="dark turquoise", font=("times new roman",45,"bold"))
staff_lbl.place(x=450, y= 12)


######Search Type
search_frame = LabelFrame(root, text="Search staff",font=("times new roman",18,"bold"),bg="dark turquoise", fg="gray20", bd=5)
search_frame.place(x=270, y=130, width=950, height=110)


select_type_lbl = Label(root, text="Search by : ",font=("times new roman",18,"bold"),fg="gray20",bg="dark turquoise")
select_type_lbl.place(x=290, y=170)

var_search_type = StringVar()
select_type = ttk.Combobox(root, textvariable=var_search_type, width=10, font=("times new roman",15), state="readonly")
select_type['values']=("id","name","salary","email","address")
select_type.place(x=420,y=175)

txt_search = StringVar()
type_entry = Entry(root, textvariable=txt_search,font=("times new roman",18,"bold"),bg="gray20",fg="dark turquoise")
type_entry.place(x=560, y=175)




####staff id

staff_id = Label(root,text="Staff Id   ", font=("times new roman",18,"bold"),bg="dark turquoise", fg="gray20")
staff_id.place(x=18, y=280)

txt_staff_id = Entry(root,font=("times new roman",18),bg="gray20",fg="dark turquoise", textvariable=var_id)
txt_staff_id.place(x= 130, y=280)


##staff name
staff_name = Label(root,text="Name     ", font=("times new roman",18,"bold"),bg="dark turquoise",fg="gray20")
staff_name.place(x=18, y=350)

txt_staff_name = Entry(root, textvariable=var_name,font=("times new roman", 18), bg="gray20",fg="dark turquoise")
txt_staff_name.place(x=130, y=350)


### staff email
staff_email = Label(root,text="Email   ",font=("times new roman",18,"bold"), bg="dark turquoise",fg="gray20")
staff_email.place(x=18,y=420)

txt_staff_email = Entry(root, textvariable=var_email,font=("times new roman",18),bg="gray20", fg="dark turquoise")
txt_staff_email.place(x = 130, y=420)


##staff gender
staff_gender = Label(root, text="Gender      ", font=("times new roman",18,"bold"), bg="dark turquoise", fg="gray20")
staff_gender.place(x=450,y=280)

txt_staff_gender = Entry(root, textvariable=var_gender,font=("times new roman",18), bg="gray20",fg="dark turquoise")
txt_staff_gender.place(x=580, y=280)


### staff dob
staff_dob = Label(root, text ="DOB          ", font=("times new roman",18,"bold"), bg="dark turquoise", fg="gray20")
staff_dob.place(x=450, y=350)

txt_staff_dob = Entry(root, textvariable=var_dob,font=("times new roman", 18), bg="gray20", fg="dark turquoise")
txt_staff_dob.place(x=580, y=350)


## staff pswd
staff_pswd = Label(root, text="Password   ", font=("times new roman", 18, "bold"),bg="dark turquoise", fg="gray20")
staff_pswd.place(x=450, y=420)

txt_staff_pswd = Entry(root, textvariable=var_pswd,font=("times new roman",18), fg="dark turquoise", bg="gray20")
txt_staff_pswd.place(x=580, y=420)


###staff contact
staff_contact = Label(root, text="Contact No   ", font=("times new roman",18,"bold"), bg="dark turquoise", fg="gray20")
staff_contact.place(x=885,y=280)

txt_staff_contact = Entry(root, textvariable=var_contact,font=("times new roman", 18), fg="dark turquoise", bg="gray20")
txt_staff_contact.place(x=1030, y=280)


###staff doj
staff_doj =Label(root, text="DOJ               ", font=("times new roman", 18,"bold"), bg="dark turquoise", fg="gray20")
staff_doj.place(x=885, y=350)

txt_staff_doj = Entry(root, textvariable=var_doj,font=("times new roman", 18), bg="gray20", fg="dark turquoise")
txt_staff_doj.place(x=1030, y=350)


### staff user type
staff_user_type = Label(root, text="User Type   ", font=("times new roman",18,"bold"), bg="dark turquoise",fg="gray20")
staff_user_type.place(x=885, y=420)

txt_staff_user_type = Entry(root, textvariable=var_type,font=("times new roman",18), bg="gray20", fg="dark turquoise")
txt_staff_user_type.place(x=1030, y=420)


###staff address
staff_address = Label(root, text="Address", bg="dark turquoise", fg="gray20", font=("times new roman",18,"bold"))
staff_address.place(x=18, y= 490)

txt_staff_address = Text(root,font=("times new roman",18), bg="gray20", fg="dark turquoise")
txt_staff_address.place(x=130, y=490, width=400, height=70)
txt_staff_address.insert(END,"")


####staff salary
staff_salary = Label(root, text="Salary",font=("times new roman", 18, "bold"), bg="dark turquoise", fg="gray20")
staff_salary.place(x=580, y=490)

txt_staff_salary = Entry(root, textvariable=var_salary,font=("times new roman",18), bg="gray20", fg="dark turquoise")
txt_staff_salary.place(x=680, y=490)

#####Function
def save_data():
    if var_contact.get() == "" or var_email=="":
        messagebox.showerror("Error","All fields are required")
    else:
        try:
            conn = mysql.connector.connect(host = "localhost", username="root", password="",port=3306,database="Bank")
            cur = conn.cursor()
            cur.execute("Insert into staff(id,name,email,address,gender,dob,pswd,salary,contact,doj,type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                var_id.get(),
                var_name.get(),
                var_email.get(),
                txt_staff_address.get('1.0',END),
                var_gender.get(),
                var_dob.get(),
                var_pswd.get(),
                var_salary.get(),
                var_contact.get(),
                var_doj.get(),
                var_type.get()

            ))
            conn.commit()
            fetch_data()
            conn.close()

            messagebox.showinfo("success","Successfully registered")
        except Exception as es:
            messagebox.showerror("Error",f"error due to : {str(es)}")


def dashboard():
    root.destroy()
    import main

##########
def fetch_data():
    conn = mysql.connector.connect(host = "localhost", username="root", password="",port=3306,database="Bank")
    cur = conn.cursor()
    cur.execute("select * from staff")
    rows = cur.fetchall()
    if len(rows) != 0:
        staff_details_table.delete(*staff_details_table.get_children())
        for i in rows:
            staff_details_table.insert("",END,values=i)
    conn.commit()
    conn.close()

def search_data():
    conn = mysql.connector.connect(host = "localhost", username="root", password="",port=3306,database="Bank")
    cur = conn.cursor()
    cur.execute("select * from staff where "+str(var_search_type.get())+" LIKE '%"+str(txt_search.get())+"%'")
    rows = cur.fetchall()
    if len(rows) != 0:
        staff_details_table.delete(*staff_details_table.get_children())
        for i in rows:
            staff_details_table.insert("",END,values=i)
    conn.commit()
    conn.close()


def get_cursor(event=""):
    cursor_row = staff_details_table.focus()
    content = staff_details_table.item(cursor_row)
    row= content["values"]

    var_id.set(row[0]),
    var_name.set(row[1]),
    var_email.set(row[2]),
    txt_staff_address.delete("1.0",END),
    txt_staff_address.insert(END,row[3])
    var_gender.set(row[4]),
    var_dob.set(row[5]),
    var_pswd.set(row[6]),
    var_salary.set(row[7]),
    var_contact.set(row[8]),
    var_doj.set(row[9]),
    var_type.set(row[10])

def clear():
    var_id.set("")
    var_name.set("")
    var_email.set("")
    txt_staff_address.delete("1.0",END)
    var_gender.set("")
    var_dob.set("")
    var_pswd.set("")
    var_salary.set("")
    var_contact.set("")
    var_doj.set("")
    var_type.set("")

def update():
    conn = mysql.connector.connect(host = "localhost", username="root", password="",port=3306,database="Bank")
    cur = conn.cursor()
    cur.execute("update staff set name=%s,email=%s,address=%s,gender=%s,dob=%s,pswd=%s,salary=%s,contact=%s,doj=%s,type=%s where id=%s",(
        var_name.get(),
        var_email.get(),
        txt_staff_address.get('1.0',END),
        var_gender.get(),
        var_dob.get(),
        var_pswd.get(),
        var_salary.get(),
        var_contact.get(),
        var_doj.get(),
        var_type.get(),
        var_id.get()
    ))
    conn.commit()
    fetch_data()
    conn.close()
    messagebox.showinfo("success","success")

def delete():
    delete = messagebox.askyesno("Staff Control","Do you want to delete this staff")
    if delete>0:
        conn = mysql.connector.connect(host = "localhost", username="root", password="",port=3306,database="Bank")
        cur = conn.cursor()
        query = "delete from staff where id=%s"
        value =(var_id.get(),)
        cur.execute(query, value)
    else:
        if not delete:
            return
    conn.commit()
    fetch_data()
    conn.close()



###show table details
show_frame = Frame(root,bg="gray20")
show_frame.place(x=18,y=580,width=1500,height=200)

scroll_x = ttk.Scrollbar(show_frame,orient=HORIZONTAL)

scroll_y = ttk.Scrollbar(show_frame, orient=VERTICAL)


staff_details_table=ttk.Treeview(show_frame, columns=("id","name", "email","address","gender","DOB","pswd","salary","Contact", "DOJ","Type"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=staff_details_table.xview)
scroll_y.config(command=staff_details_table.yview)

staff_details_table.heading("id", text="Staff Id")
staff_details_table.heading("name", text="Name")
staff_details_table.heading("email",text="Email")
staff_details_table.heading("address", text="Address")
staff_details_table.heading("gender", text="Gender")
staff_details_table.heading("DOB", text="DOB")
staff_details_table.heading("pswd",text="Password")
staff_details_table.heading("salary",text="Salary")
staff_details_table.heading("Contact",text="Contact No")
staff_details_table.heading("DOJ",text="DOJ")
staff_details_table.heading("Type", text="User Type")

staff_details_table["show"] = "headings"
staff_details_table.pack(fill=BOTH,expand=1)
fetch_data()
staff_details_table.bind("<ButtonRelease-1>",get_cursor)


#####Right Frame
btn_frame = Frame(root, bg="gray20")
btn_frame.place(x=1320, y=230, width=180, height=330)


save_btn = Button(root, text="Save",bg="dark turquoise", fg="gray20", font=("times new roman",18,"bold"),width=10, activebackground="dark turquoise", activeforeground="gray20", command=save_data)
save_btn.place(x=1335, y=260)

update_btn = Button(root, text="Update",bg="dark turquoise", fg="gray20", font=("times new roman",18,"bold"),width=10, activebackground="dark turquoise", activeforeground="gray20", command=update)
update_btn.place(x=1335, y=330)


clear_btn = Button(root, text="Clear",bg="dark turquoise", fg="gray20", font=("times new roman",18,"bold"),width=10, activebackground="dark turquoise", activeforeground="gray20", command=clear)
clear_btn.place(x=1335, y=400)

delete_btn = Button(root, text="Delete",bg="dark turquoise", fg="gray20", font=("times new roman",18,"bold"),width=10, activebackground="dark turquoise", activeforeground="gray20",command=delete)
delete_btn.place(x=1335, y=470)

search_btn = Button(root, font=("times new roman",18,"bold"),fg="dark turquoise",bg="gray20",text="Search", command=search_data)
search_btn.place(x=820,y=165,width=110)

show_btn = Button(root, font=("times new roman",18,"bold"),fg="dark turquoise",bg="gray20",text="Show all", command=fetch_data)
show_btn.place(x=940,y=165,width=110)

dashboard_btn = Button(root, font=("times new roman",18,"bold"),fg="dark turquoise",bg="gray20",text="Dashboard",command=dashboard)
dashboard_btn.place(x=1060,y=165,width=140)

root.mainloop()