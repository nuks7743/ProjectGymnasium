from tkinter import*
from tkinter import ttk
from typing import Self
import mysql.connector
from tkinter import messagebox
import tkinter

class GymnasiumManagementSystem: 
    def __init__(self,root):
        self.root=root
        self.root.title("Gymnasium Mangemnt System") 
        self.root.geometry("1366x800+0+0")

        #================================================Variable====================================

        self.Member_var=StringVar()
        self.CodeNo_var=StringVar() 
        self.FirstName_var=StringVar()
        self.LastName_var=StringVar()
        self.DOB_var=StringVar() 
        self.ContactNo_var=StringVar()
        self.Email_var=StringVar() 
        self.CurrentAddress_var=StringVar()
        self.PermanantAddress_var=StringVar()
        self.PostCode_var=StringVar()
        self.Weight_var=StringVar() 
        self.Height_var=StringVar()
        self.BicepsSize_var=StringVar()
        self.ChestSize_var=StringVar()
        self.JoiningDate_var=StringVar()
        self.Fees_var=StringVar()
        self.ExpiryDate_var=StringVar()

        #=============================================TITLE==============================================

        lbltitle=Label(self.root,text="GYMNASIUM   MANAGEMNT   SYSTEM",bg="White",fg="GREEN",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="White")
        frame.place(x=0,y=130,width=1366,height=616)

        # ==========================================Data Frame============================================

        DataFrame=LabelFrame(frame,text="Gymnasium   Membership   Form ",bg="White",fg="green",bd=10,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrame.place(x=-10,y=5,width=1330,height=250)

        lblMember=Label(DataFrame,font=("arial",12,"bold"),text="Member Type",padx=2,pady=6,bg="PINK")
        lblMember.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(DataFrame,textvariable=self.Member_var,state="readonly",font=("arial",12,"bold"),width=27)
        comMember["value"]=("Select","Male","Fe-Male","Trans-Gender")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblCodeNo=Label(DataFrame,font=("arial",12,"bold"),text="Code No :",padx=2,bg="PINK")
        lblCodeNo.grid(row=0,column=2,sticky=W)
        txtCodeNo=Entry(DataFrame,font=("arial",13,"bold"),textvariable=self.CodeNo_var,width=29)
        txtCodeNo.grid(row=0,column=3)

        lblFirstName=Label(DataFrame,font=("arial",12,"bold"),text="First Name :",padx=2,pady=6,bg="White")
        lblFirstName.grid(row=1,column=0,sticky=W)
        txtFirstName=Entry(DataFrame,font=("arial",13,"bold"),textvariable=self.FirstName_var,width=29)
        txtFirstName.grid(row=1,column=1)

        lblLastName=Label(DataFrame,font=("arial",12,"bold"),text="Last Name :",padx=2,pady=6,bg="White")
        lblLastName.grid(row=1,column=2,sticky=W)
        txtLastName=Entry(DataFrame,font=("arial",13,"bold"),textvariable=self.LastName_var,width=29)
        txtLastName.grid(row=1,column=3)

        lblDOB=Label(DataFrame,font=("arial",12,"bold"),text="DOB :",padx=2,pady=6,bg="White")
        lblDOB.grid(row=1,column=4,sticky=W)
        txtDOB=Entry(DataFrame,font=("arial",13,"bold"),textvariable=self.DOB_var,width=29)
        txtDOB.grid(row=1,column=5)

        lblContact_No=Label(DataFrame,font=("arial",12,"bold"),text="Contact No :",padx=2,pady=6,bg="White")
        lblContact_No.grid(row=2,column=0,sticky=W)
        txtContact_No=Entry(DataFrame,font=("arial",13,"bold"),textvariable=self.ContactNo_var,width=29)
        txtContact_No.grid(row=2,column=1)

        lblEmail=Label(DataFrame,font=("arial",12,"bold"),text="E Mail :",padx=2,pady=6,bg="White")
        lblEmail.grid(row=2,column=2,sticky=W)
        txtEmail=Entry(DataFrame,font=("arial",13,"bold"),textvariable=self.Email_var,width=29)
        txtEmail.grid(row=2,column=3)

        lblCurrent_Address=Label(DataFrame,font=("arial",12,"bold"),text="Current Address :",padx=2,pady=6,bg="White")
        lblCurrent_Address.grid(row=2,column=4,sticky=W)
        txtCurrent_Address=Entry(DataFrame,font=("arial",13,"bold"),textvariable=self.CurrentAddress_var,width=29)
        txtCurrent_Address.grid(row=2,column=5)

        lblPermanent_Address=Label(DataFrame,font=("arial",12,"bold"),text="Permanent Address :",padx=2,pady=6,bg="White")
        lblPermanent_Address.grid(row=3,column=0,sticky=W)
        txtPermanent_Address=Entry(DataFrame,font=("arial",13,"bold"),textvariable=self.PermanantAddress_var,width=29)
        txtPermanent_Address.grid(row=3,column=1)

        lblPost_Code=Label(DataFrame,font=("arial",12,"bold"),text="Post Code :",padx=2,pady=6,bg="White")
        lblPost_Code.grid(row=3,column=2,sticky=W)
        txtPost_Code=Entry(DataFrame,font=("arial",13,"bold"),textvariable=self.PostCode_var,width=29)
        txtPost_Code.grid(row=3,column=3)

        lblWeight=Label(DataFrame,font=("arial",12,"bold"),text="Weight :",padx=2,pady=6,bg="White")
        lblWeight.grid(row=3,column=4,sticky=W)
        txtWeight=Entry(DataFrame,font=("arial",12,"bold"),textvariable=self.Weight_var,width=29)
        txtWeight.grid(row=3,column=5)

        lblHeight=Label(DataFrame,font=("arial",12,"bold"),text="Height(cm) :",padx=2,pady=6,bg="White")
        lblHeight.grid(row=4,column=0,sticky=W)
        comHeight=ttk.Combobox(DataFrame,textvariable=self.Height_var,state="readonly",font=("arial",12,"bold"),width=27)
        comHeight["value"]=("Select","90","92","94","95","96","97","98","99","100","102","105","106","108","110","111","114","116","117","119","120","122","125","126","128","130","135","145.2","152.41","154.9","157.4","158.9","159.48","160.0","162.5","165.1","167.7","170.1","172.02", "175.18","176.72","178.26","179.80","180.34","182.88","185.45","187.96","190.50","193.04","195.58","197.5","198.2","200.8","202.3","205.9")
        comHeight.current(0)
        comHeight.grid(row=4,column=1)

        lblBiceps_Size=Label(DataFrame,font=("arial",12,"bold"),text="Biceps Size(inch) :",padx=2,pady=6,bg="White")
        lblBiceps_Size.grid(row=4,column=2,sticky=W)
        comBiceps_Size=ttk.Combobox(DataFrame,textvariable=self.BicepsSize_var,state="readonly",font=("arial",12,"bold"),width=27)
        comBiceps_Size["value"]=("Select","5.35","5.71","5.8","76.06","6.30","6.57","6.89","7.28","7.48","7.95","8.00","8.39","8.54","9.00","9.29","9.80","10.00","10.35","10.51","10.94","11.06","11.01","11.30","11.69","11.80","12.05","12.41","13.34","13.75","14.01","14.40","15.22","15.80","16.05","16.41","17.24","17.75","18.01","18.40","19.08","19.70","20.05")
        comBiceps_Size.current(0)
        comBiceps_Size.grid(row=4,column=3)

        lblChest_Size=Label(DataFrame,font=("arial",12,"bold"),text="Chest Size(cm) : ",padx=2,pady=6,bg="White")
        lblChest_Size.grid(row=4,column=4,sticky=W)
        comChest_Size=ttk.Combobox(DataFrame,textvariable=self.ChestSize_var,state="readonly",font=("arial",12,"bold"),width=27)
        comChest_Size["value"]=("Select","50","55","58","60","62","65","68","70","74","76","78","80","82","85","86","88","90","92","94","95","96","97","98","99","100","102","105","106","108","110","111","114","116","117","119","120","122","125","126","128","130","135")
        comChest_Size.current(0)
        comChest_Size.grid(row=4,column=5)

        lblJoining_Date=Label(DataFrame,font=("arial",12,"bold"),text="Joining Date :",padx=2,pady=6,bg="White")
        lblJoining_Date.grid(row=5,column=0,sticky=W)
        txtJoining_Date=Entry(DataFrame,font=("arial",12,"bold"),textvariable=self.JoiningDate_var,width=29)
        txtJoining_Date.grid(row=5,column=1)

        lblFees=Label(DataFrame,font=("arial",12,"bold"),text="Fees :",padx=2,pady=6,bg="White")
        lblFees.grid(row=5,column=2,sticky=W)
        comFees=ttk.Combobox(DataFrame,textvariable=self.Fees_var,state="readonly",font=("arial",12,"bold"),width=27)
        comFees["value"]=("Select","Monthly - 700rs","Quarterly - 2000rs","6 Months - 4000rs","Yearly - 7000rs")
        comFees.current(0)
        comFees.grid(row=5,column=3)

        lblExpiry_Date=Label(DataFrame,font=("arial",12,"bold"),text="Expiry Date :",padx=2,pady=6,bg="PINK")
        lblExpiry_Date.grid(row=0,column=4,sticky=W)
        txtExpiry_Date=Entry(DataFrame,font=("arial",12,"bold"),textvariable=self.ExpiryDate_var,width=29)
        txtExpiry_Date.grid(row=0,column=5)

        # =============================================Button Frame===========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="White")
        Framebutton.place(x=20,y=400,width=1330,height=58)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=24,bg="Powder blue",fg="Black")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=24,bg="Powder blue",fg="Black")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=24,bg="Powder blue",fg="Black")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.Reset,text="Reset",font=("arial",12,"bold"),width=24,bg="Powder blue",fg="Black")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=24,bg="Powder blue",fg="Black")
        btnAddData.grid(row=0,column=5)

        # =============================================Information Frame=========================================

        FrameDetails=LabelFrame(frame,text="Members   Information",bg="White",fg="green",bd=10,relief=RIDGE,font=("times new roman",12,"bold"))
        FrameDetails.place(x=-10,y=320,width=1330,height=270)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="White")
        Table_frame.place(x=10,y=2,width=1300,height=240)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.Gymnasium_table=ttk.Treeview(Table_frame,column=("Member","codeno","firstname","lastname","dob","contactno","email","currentaddress","permanantaddress","postcode","weight","height","bicepssize","chestsize","joiningdate","fees","expirydate"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.Gymnasium_table.xview)
        yscroll.config(command=self.Gymnasium_table.yview)

        self.Gymnasium_table.heading("Member",text="Member")
        self.Gymnasium_table.heading("codeno",text="Code No")
        self.Gymnasium_table.heading("firstname",text="First Name")
        self.Gymnasium_table.heading("lastname",text="Last Name")
        self.Gymnasium_table.heading("dob",text="Date Of Birth")
        self.Gymnasium_table.heading("contactno",text="Contact No")
        self.Gymnasium_table.heading("email",text="E-Mail")
        self.Gymnasium_table.heading("currentaddress",text="Current Address")
        self.Gymnasium_table.heading("permanantaddress",text="Permnant Address")
        self.Gymnasium_table.heading("postcode",text="Post Code")
        self.Gymnasium_table.heading("weight",text="Weight")
        self.Gymnasium_table.heading("height", text="Height")
        self.Gymnasium_table.heading("bicepssize",text="Biceps Size")
        self.Gymnasium_table.heading("chestsize",text="Chest Size")
        self.Gymnasium_table.heading("joiningdate",text="Joining Date")
        self.Gymnasium_table.heading("fees",text="Fees")
        self.Gymnasium_table.heading("expirydate",text="Expiry Date")

        self.Gymnasium_table["show"]="headings"
        self.Gymnasium_table.pack(fill=BOTH,expand=1)

        self.Gymnasium_table.column("Member",width=60)
        self.Gymnasium_table.column("codeno",width=60)
        self.Gymnasium_table.column("firstname",width=100)
        self.Gymnasium_table.column("lastname",width=100)
        self.Gymnasium_table.column("dob",width=80)
        self.Gymnasium_table.column("contactno",width=100)
        self.Gymnasium_table.column("email",width=100)
        self.Gymnasium_table.column("currentaddress",width=100)
        self.Gymnasium_table.column("permanantaddress",width=100)
        self.Gymnasium_table.column("postcode",width=60)
        self.Gymnasium_table.column("weight",width=50)
        self.Gymnasium_table.column("height",width=50)
        self.Gymnasium_table.column("bicepssize",width=50)
        self.Gymnasium_table.column("chestsize",width=60)
        self.Gymnasium_table.column("joiningdate",width=100)
        self.Gymnasium_table.column("fees",width=100)
        self.Gymnasium_table.column("expirydate",width=100)

        self.fatch_data()
        self.Gymnasium_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ainpur@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into gymnasium values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.Member_var.get(),
                                                                                                                self.CodeNo_var.get(),
                                                                                                                self.FirstName_var.get(),
                                                                                                                self.LastName_var.get(),
                                                                                                                self.DOB_var.get(),
                                                                                                                self.ContactNo_var.get(),
                                                                                                                self.Email_var.get(),
                                                                                                                self.CurrentAddress_var.get(),
                                                                                                                self.PermanantAddress_var.get(),
                                                                                                                self.PostCode_var.get(),
                                                                                                                self.Weight_var.get(),
                                                                                                                self.Height_var.get(),
                                                                                                                self.BicepsSize_var.get(),
                                                                                                                self.ChestSize_var.get(),
                                                                                                                self.JoiningDate_var.get(),
                                                                                                                self.Fees_var.get(),
                                                                                                                self.ExpiryDate_var.get()
                                                                                                                ))
        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Sucsess","Member Has Been Insertes Successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ainpur@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update gymnasium set Member=%s,FirstName=%s,LastName=%s,DOB=%s,ContactNo=%s,Email=%s,CurrentAddress=%s,PermanantAddress=%s,PostCode=%s,Weight=%s,Height=%s,BicepsSize=%s,ChestSize=%s,JoiningDate=%s,Fees=%s,ExpiryDate=%s where CodeNo=%s",(
                                                                                                                                                                                                                                                                                self.Member_var.get(),
                                                                                                                                                                                                                                                                                self.FirstName_var.get(),
                                                                                                                                                                                                                                                                                self.LastName_var.get(),
                                                                                                                                                                                                                                                                                self.DOB_var.get(),
                                                                                                                                                                                                                                                                                self.ContactNo_var.get(),
                                                                                                                                                                                                                                                                                self.Email_var.get(),
                                                                                                                                                                                                                                                                                self.CurrentAddress_var.get(),
                                                                                                                                                                                                                                                                                self.PermanantAddress_var.get(),
                                                                                                                                                                                                                                                                                self.PostCode_var.get(),
                                                                                                                                                                                                                                                                                self.Weight_var.get(),
                                                                                                                                                                                                                                                                                self.Height_var.get(),
                                                                                                                                                                                                                                                                                self.BicepsSize_var.get(),
                                                                                                                                                                                                                                                                                self.ChestSize_var.get(),
                                                                                                                                                                                                                                                                                self.JoiningDate_var.get(),
                                                                                                                                                                                                                                                                                self.Fees_var.get(),
                                                                                                                                                                                                                                                                                self.ExpiryDate_var.get(),
                                                                                                                                                                                                                                                                                self.CodeNo_var.get(),
                                                                                                                                                                                                                                                                        ))
        conn.commit()
        self.fatch_data()
        self.Reset()
        conn.close()
        messagebox.showinfo("Sucsess","Member Has Been Update Successfully")

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ainpur@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from gymnasium")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.Gymnasium_table.delete(*self.Gymnasium_table.get_children())
            for I in rows:
                self.Gymnasium_table.insert("",END,values=I)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Gymnasium_table.focus()
        content=self.Gymnasium_table.item(cursor_row)
        row=content["values"]

        self.Member_var.set(row[0]),
        self.CodeNo_var.set(row[1]),
        self.FirstName_var.set(row[2]),
        self.LastName_var.set(row[3]),
        self.DOB_var.set(row[4]),
        self.ContactNo_var.set(row[5]),
        self.Email_var.set(row[6]),
        self.CurrentAddress_var.set(row[7]),
        self.PermanantAddress_var.set(row[8]),
        self.PostCode_var.set(row[9]),
        self.Weight_var.set(row[10]),
        self.Height_var.set(row[11]),
        self.BicepsSize_var.set(row[12]),
        self.ChestSize_var.set(row[13]),
        self.JoiningDate_var.set(row[14]),
        self.Fees_var.set(row[15]),
        self.ExpiryDate_var.set(row[16]),

    def Reset(self):
        self.Member_var.set(""),
        self.CodeNo_var.set(""),
        self.FirstName_var.set(""),
        self.LastName_var.set(""),
        self.DOB_var.set(""),
        self.ContactNo_var.set(""),
        self.Email_var.set(""),
        self.CurrentAddress_var.set(""),
        self.PermanantAddress_var.set(""),
        self.PostCode_var.set(""),
        self.Weight_var.set(""),
        self.Height_var.set(""),
        self.BicepsSize_var.set(""),
        self.ChestSize_var.set(""),
        self.JoiningDate_var.set(""),
        self.Fees_var.set(""),
        self.ExpiryDate_var.set(""),

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Gymnasium Management System","Do you Want To Exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.CodeNo_var.get()=="" or self.PostCode_var.get()=="":
            messagebox.showerror("Error","First Select The Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Ainpur@123",database="gymmsdata")
            my_cursor=conn.cursor()
            query="delete from gymnasium where CodeNo=%s"
            value=(self.CodeNo_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.Reset()
            conn.close()

            messagebox.showinfo("Success","Member Has Been Deleted")


if __name__ == "__main__":
    root=Tk()
    obj=GymnasiumManagementSystem(root)
    root.mainloop()