from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Mangement System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar() 
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
       
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman", 50 ,"bold"))
        lbltitle.pack(side=TOP,fill=X)   

        #######DATAFRAMES  
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)

        dataframeleft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman", 12 ,"bold"),text="Patient Information")
        dataframeleft.place(x=0,y=5,width=980,height=350)

        dataframeright=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman", 12 ,"bold"),text="Prescription")
        dataframeright.place(x=990,y=5,width=460,height=350)

        ## --------------------BUTTON FRAMES-----------------

        ButtonFrame = Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)

        ##-----------------details frame-----------------------
        DetailsFrame = Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=600,width=1530,height=190)

        ##------------------ Dataframe left --------------
        lblnametablet=Label(dataframeleft,text="Names of Tablet",font=("arial", 12 ,"bold"),padx=2,pady=6)
        lblnametablet.grid(row=0,column=0,sticky=W)

        comnametablet=ttk.Combobox(dataframeleft,textvariable=self.Nameoftablets,state="readonlt",font=("arial", 12 ,"bold"),width=33)
        comnametablet["values"]=("Nice","Corona Vaccine","Acetaminophane","Adderal","Amlodipine","Ativan")
        comnametablet.current(0)
        comnametablet.grid(row=0,column=1)
        
        lblref=Label(dataframeleft,font=("arial",12,"bold"),text="Refence no.",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lbldose=Label(dataframeleft,font=("arial",12,"bold"),text="Dose: ",padx=2,pady=4)
        lbldose.grid(row=2,column=0,sticky=W)
        txtdose=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.Dose,width=35)
        txtdose.grid(row=2,column=1)

        lblnooftablets=Label(dataframeleft,font=("arial",12,"bold"),text="No. of tablets:",padx=2,pady=6)
        lblnooftablets.grid(row=3,column=0,sticky=W)
        txtnooftablets=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.NumberofTablets,width=35)
        txtnooftablets.grid(row=3,column=1)

        lbllot=Label(dataframeleft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        lbllot=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.Lot,width=35)
        lbllot.grid(row=4,column=1)
        
        lblExp=Label(dataframeleft,font=("arial",12,"bold"),text="Expiry date:",padx=2,pady=6)
        lblExp.grid(row=5,column=0,sticky=W)
        txtExp=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.ExpDate,width=35)
        txtExp.grid(row=5,column=1)

        lblissue=Label(dataframeleft,font=("arial",12,"bold"),text="Issuedate:",padx=2,pady=6)
        lblissue.grid(row=6,column=0,sticky=W)
        txtissue=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.Issuedate,width=35)
        txtissue.grid(row=6,column=1)

        lbldailydose=Label(dataframeleft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lbldailydose.grid(row=7,column=0,sticky=W)
        txtdailydose=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.DailyDose,width=35)
        txtdailydose.grid(row=7,column=1)
        
        lblsideeffect=Label(dataframeleft,font=("arial",12,"bold"),text="Side effect:",padx=2,pady=6)
        lblsideeffect.grid(row=8,column=0,sticky=W)
        txtsideeffect=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.sideEfect,width=35)
        txtsideeffect.grid(row=8,column=1)

        lblfurtherrinfo=Label(dataframeleft,font=("arial",12,"bold"),text="Further info:",padx=2)
        lblfurtherrinfo.grid(row=0,column=2,sticky=W)
        txtfurtherinfo=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtfurtherinfo.grid(row=0,column=3)

        lblbp=Label(dataframeleft,font=("arial",12,"bold"),text="Blood pressure:",padx=2,pady=6)
        lblbp.grid(row=1,column=2,sticky=W)
        txtbp=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtbp.grid(row=1,column=3)

        lblsto=Label(dataframeleft,font=("arial",12,"bold"),text="Storage advice:",padx=2,pady=6)
        lblsto.grid(row=2,column=2,sticky=W)
        txtsto=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=35)
        txtsto.grid(row=2,column=3)

        lblmed=Label(dataframeleft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblmed.grid(row=3,column=2,sticky=W)
        txtmed=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtmed.grid(row=3,column=3)

        lblpatId=Label(dataframeleft,font=("arial",12,"bold"),text="Patient id:",padx=2,pady=6)
        lblpatId.grid(row=4,column=2,sticky=W)
        txtpatId=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.PatientId,width=35)
        txtpatId.grid(row=4,column=3)

        lblNhsnumber=Label(dataframeleft,font=("arial",12,"bold"),text="Nhs number:",padx=2,pady=6)
        lblNhsnumber.grid(row=5,column=2,sticky=W)
        txtNhsnumber=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsnumber.grid(row=5,column=3)
        
        lblpatname=Label(dataframeleft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblpatname.grid(row=6,column=2,sticky=W)
        txtpatname=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.PatientName,width=35)
        txtpatname.grid(row=6,column=3)

        lbldob=Label(dataframeleft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lbldob.grid(row=7,column=2,sticky=W)
        txtdob=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.DateOfBirth,width=35)
        txtdob.grid(row=7,column=3)

        lblpatadress=Label(dataframeleft,font=("arial",12,"bold"),text="Patient address:",padx=2,pady=6)
        lblpatadress.grid(row=8,column=2,sticky=W)
        txtpatadress=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=35)
        txtpatadress.grid(row=8,column=3)

        #------------------Datfarameright-----------------------
        self.txtPrescription=Text(dataframeright,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #--------------------------Button--------------------------
        
        btnprescription=Button(ButtonFrame,command=self.iPrescription,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnprescription.grid(row=0,column=0)
        
        btndata=Button(ButtonFrame,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6,command=self.iPrescriptionData)
        btndata.grid(row=0,column=1)

        btnupdate=Button(ButtonFrame,command=self.update,text="Update:",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnupdate.grid(row=0,column=2)

        btndelete=Button(ButtonFrame,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btndelete.grid(row=0,column=3)

        btnclear=Button(ButtonFrame,command=self.clear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnclear.grid(row=0,column=4)

        btnexit=Button(ButtonFrame,command=self.iexit,text="exit",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnexit.grid(row=0,column=5)

        #------------Table----------------------------------

        ####------------------ScrollBar---------------------
        
        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(DetailsFrame,column=("nameoftable","ref","dose","nooftablest","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_x=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="name of tablets")
        self.hospital_table.heading("ref",text="refrence no.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablest",text="no of tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Isuuedate")
        self.hospital_table.heading("expdate",text="Expiry date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage:")
        self.hospital_table.heading("nhsnumber",text="Nhs Number:")
        self.hospital_table.heading("pname",text="Patient name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablest",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)


        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.getcursor)


        self.fetchdata()

    #================Functionality DEscription====================

    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="BISHWaa0326",database="hospital_data")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into new_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                       self.Nameoftablets.get(),
                                                                                                       self.ref.get(),
                                                                                                       self.Dose.get(),
                                                                                                       self.NumberofTablets.get(),
                                                                                                       self.Lot.get(),
                                                                                                       self.Issuedate.get(),
                                                                                                       self.ExpDate.get(),
                                                                                                       self.DailyDose.get(),
                                                                                                       self.StorageAdvice.get(),
                                                                                                       self.nhsNumber.get(),
                                                                                                       self.PatientName.get(),
                                                                                                       self.DateOfBirth.get(),
                                                                                                       self.PatientAddress.get()

                                                                                                        ))
            conn.commit()
            self.fetchdata()
            conn.close()
            messagebox.showinfo("Success","RECORD HAS BEEN INSERTED!")

     

    def update(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="BISHWaa0326",database="hospital_data")
            my_cursor=conn.cursor()
            my_cursor.execute("update new_table set Nameoftablets=%s, dose=%s, Numberoftablets=%s, lot=%s, issuedate=%s, expdata=%s, dailydose=%s, storage=%s, nhsnumber=%s, pateint_name=%s, DOB=%s, patientaddress=%s where Reference_No=%s",(
                                                                                                                self.Nameoftablets.get(),
                                                                                                                self.Dose.get(),
                                                                                                                self.NumberofTablets.get(),
                                                                                                                self.Lot.get(),
                                                                                                                self.Issuedate.get(),
                                                                                                                self.ExpDate.get(),
                                                                                                                self.DailyDose.get(),
                                                                                                                self.StorageAdvice.get(),
                                                                                                                self.nhsNumber.get(),
                                                                                                                self.PatientName.get(),
                                                                                                                self.DateOfBirth.get(),
                                                                                                                self.PatientAddress.get(),
                                                                                                                self.ref.get() ))     
            conn.commit()
            conn.close()
            self.fetchdata()
            messagebox.showinfo("Success","RECORD HAS BEEN updated!") 
                                                                                                                    
    def fetchdata(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="BISHWaa0326",database="hospital_data")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from new_table")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                 self.hospital_table.delete(*self.hospital_table.get_children())
                 for i in rows:
                      self.hospital_table.insert("",END,values=i)
                 conn.commit()
            conn.close() 
            
    def getcursor(self,event=""):
         cursor_row=self.hospital_table.focus()
         content=self.hospital_table.item(cursor_row)
         row=content["values"]
         self.Nameoftablets.set(row[0])
         self.ref.set(row[1])
         self.Dose.set(row[2])
         self.NumberofTablets.set(row[3])
         self.Lot.set(row[4])
         self.Issuedate.set(row[5])
         self.ExpDate.set(row[6])
         self.DailyDose.set(row[7])
         self.StorageAdvice.set(row[8])
         self.nhsNumber.set(row[9])
         self.PatientName.set(row[10])
         self.DateOfBirth.set(row[11])
         self.PatientAddress.set(row[12])

    def iPrescription(self):
         self.txtPrescription.insert(END,"name of tabets:\t"+self.Nameoftablets.get()+"\n")                               
         self.txtPrescription.insert(END, "Reference No: \t" + self.ref.get() + "\n")
         self.txtPrescription.insert(END, "Dose:\t" + self.Dose.get() + "\n")
         self.txtPrescription.insert(END, "Number Of Tablets: \t" + self.NumberofTablets.get() + "\n") 
         self.txtPrescription.insert(END, "Lot: \t" + self. Lot.get() + "\n")
         self.txtPrescription.insert(END, "Issue Date:\t" + self.Issuedate.get() + "\n") 
         self.txtPrescription.insert(END, "Exp date:\t" + self.ExpDate.get() + "\n")
         self.txtPrescription.insert(END, "daily Dose:\t" + self.DailyDose.get() + "\n")
         self.txtPrescription.insert(END, "Side Effect: \t" + self.sideEfect.get() + "\n")
         self.txtPrescription.insert(END, "Further Information: \t" + self.FurtherInformation.get() + "\n")
         self.txtPrescription.insert(END, "StorageAdvice:\t" + self.StorageAdvice.get() + "\n")
         self.txtPrescription.insert(END, "DrivingUsingMachine:\t" + self.DrivingUsingMachine.get() + "\n")
         self.txtPrescription.insert(END," PatientId: \t" + self.PatientId.get() + "\n")
         self.txtPrescription.insert(END, "NHSNumber: \t" + self.nhsNumber.get() + "\n")
         self.txtPrescription.insert(END, "PatientName:\t" + self.PatientName.get() + "\n")
         self.txtPrescription.insert(END, "DateOfBirth: \t" + self.DateOfBirth.get() + "\\n")
         self.txtPrescription.insert(END, "PatientAddress:\t" + self.PatientAddress.get() + "\n")
    def idelete(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="BISHWaa0326",database="hospital_data")
         my_cursor=conn.cursor()
         query="delete from new_table where Reference_No=%s"
         value=(self.ref.get(),)
         my_cursor.execute(query,value)

         conn.commit()
         conn.close()
         self.fetchdata()
         messagebox.showinfo("Delete","Patient record has been deleted successfully")
    
    def clear(self):
         self.Nameoftablets.set("")
         self.ref.set("")
         self.Dose.set("")
         self.NumberofTablets.set("")
         self.Lot.set("")
         self.Issuedate.set("") 
         self.ExpDate.set("")
         self.DailyDose.set("")
         self.sideEfect.set("")
         self.FurtherInformation.set("")
         self.StorageAdvice.set("") 
         self.DrivingUsingMachine.set("")
         self.HowToUseMedication.set("")
         self.PatientId.set("")
         self.nhsNumber.set("")
         self.PatientName.set("")
         self.DateOfBirth.set("")
         self.PatientAddress.set("")
         self.txtPrescription.delete("1.0", END)

    def iexit(self):
         iexit=messagebox.askyesno ("Hospital managemnt system", "Confirm you want to exit") 
         if iexit>0: 
            root.destroy()
            return     
root=Tk()
ob=Hospital(root)

root.mainloop()
