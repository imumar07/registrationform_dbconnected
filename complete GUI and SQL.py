import re
from tkinter import *
from tkinter import messagebox as m
from tkinter import Frame as f
import mysql.connector as mc

#Creating the mysql process
conn=mc.connect(host="localhost",user="root",password="root",database="cai")

def get_radio_result():
    if(radio_var1.get()==1):
        return "I"
    elif(radio_var1.get()==2):
        return "II"    
    elif(radio_var1.get()==3):
        return "III"   
    else:
        return "IV"  

def get_checkbox_result():
    s=""
    if(check_var1.get()==1):
        s=s+"C"+" "
    else:
        s+=""
    if(check_var2.get()==1):
        s+="C++"+" "
    else:
        s+=""
    if(check_var3.get()==1):
        s+="JAVA"+" "
    else:
        s+=""
    if(check_var4.get()==1):
        s+="Python"+" "
    else:
        s+=""         
    return s                                    

def insert():
    a=(re.search("^[A-Za-z ]",entry_name.get()))

    b= (re.search("^[0-9]{10}$",entry_phone.get()))
         
    c= (re.search("@gmail.com",entry_email.get()))
        
    if(a and b and c):
        cur=conn.cursor()
        cur.execute("INSERT INTO student1 VALUES(%s,%s,%s,%s,%s,%s,%s)",
        (entry_rollno.get(),entry_name.get(),(str(day_listbox.get(ANCHOR))+"-"+str(month_listbox.get(ANCHOR))+"-"+str(year_listbox.get(ANCHOR))),email_var.get(),phone_var.get(),get_radio_result(),get_checkbox_result()))
        conn.commit()
        m.showinfo("result","Insert sucesfully")
    elif(not a):
        m.showerror("result","name is incorrect")
    elif(not b):
        m.showerror("result","phone is incorrect") 
    elif(not c):
        m.showwarning("result","email is incorrect")



    
def display():
    s=""
    try:
        s+="ROLLNO: "+str(entry_rollno.get())+"\n"
    except:
        print("Error in roll_no")
    try:
        s+="NAME: "+str(entry_name.get())+"\n"
    except:
        print("Error in name")    
    try:
        s+="DOB: "+str(day_listbox.get(ANCHOR))+"-"+str(day_listbox.get(ANCHOR))+"-"+str(year_listbox.get(ANCHOR))+"\n"
    except:
        print("Error in DOB")    
    try:
        s+="EMAIL: "+str(email_var.get())+"\n"
    except:
        print("Error in EMAIL") 
    try:
        s+="PHONE_NO: "+str(phone_var.get())+"\n"
    except:
        print("Error in phone_number") 
    s+="SEM: "+get_radio_result()+"\n"
    s+="PROGRAMMING_LANGUAGES: "+get_checkbox_result()+"\n"
    m.showinfo("display",s)



#Start of program

months=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
year=[str(i) for i in range(2001,2031)]
top=Tk()
top.title("Complete GUI")
radio_var1=IntVar()
check_var1,check_var2,check_var3,check_var4=IntVar(),IntVar(),IntVar(),IntVar()
roll_var,name_var,email_var,phone_var=StringVar(),StringVar(),StringVar(),StringVar()
frame1=f(top)
frame1.pack()
frame2=f(frame1)
frame2.grid(row=2,column=1)
frame3=f(frame1)
frame3.grid(row=2,column=2)
frame4=f(frame1)
frame4.grid(row=2,column=3)

#Main Heading Label
main_heading=Label(frame1,text="Student Registration Page")
main_heading.grid(row=0,column=2)

#ROLLNO Label and Entry
rollno_label=Label(frame1,text="Rollno")
rollno_label.grid(row=1,column=0,padx=10)
entry_rollno=Entry(frame1,width=10,textvariable=roll_var)
entry_rollno.grid(row=1,column=1,padx=10)

#Name Label and Entry
name_label=Label(frame1,text="Name")
name_label.grid(row=1,column=3,padx=10)
entry_name=Entry(frame1,width=10,textvariable=name_var)
entry_name.grid(row=1,column=4,padx=10)

#DOB label
DOB_label=Label(frame1,text="DOB")
DOB_label.grid(row=2,column=0,padx=10)


#Day listbox and scroll bar

day_scrollbar=Scrollbar(frame2)
day_scrollbar.pack(side=RIGHT)
day_listbox=Listbox(frame2,yscrollcommand=day_scrollbar.set,height=1,width=5)
for i in range(1,32):
    day_listbox.insert(END,str(i))
day_listbox.pack(side=LEFT)
day_scrollbar.config(command=day_listbox.yview)

#Month listbox and scroll bar
month_scrollbar=Scrollbar(frame3)
month_scrollbar.pack(side=RIGHT)
month_listbox=Listbox(frame3,yscrollcommand=month_scrollbar.set,height=1,width=5)
for i in months:
    month_listbox.insert(END,str(i))
month_listbox.pack(side=LEFT)
month_scrollbar.config(command=month_listbox.yview)

#Year listbox and scroll bar
year_scrollbar=Scrollbar(frame4)
year_scrollbar.pack(side=RIGHT)
year_listbox=Listbox(frame4,yscrollcommand=year_scrollbar.set,height=1,width=5)
for i in year:
    year_listbox.insert(END,str(i))
year_listbox.pack(side=LEFT)
year_scrollbar.config(command=year_listbox.yview)


#Email Label and Entry
email_label=Label(frame1,text="Email")
entry_email=Entry(frame1,width=10,textvariable=email_var)
email_label.grid(row=3,column=0,padx=10)
entry_email.grid(row=3,column=1,padx=10)

#Phone Label and Entry
phone_label=Label(frame1,text="Phone")
phone_label.grid(row=3,column=3,padx=10)
entry_phone=Entry(frame1,width=10,textvariable=phone_var)
entry_phone.grid(row=3,column=4,padx=10)

#Year and radiobutton
college_year_label=Label(frame1,text="Year")
college_year_label.grid(row=5,column=0)

college_year_radiobutton_1=Radiobutton(frame1,value=1,text="I",variable=radio_var1)
college_year_radiobutton_1.grid(row=5,column=1)

college_year_radiobutton_1=Radiobutton(frame1,value=2,text="II",variable=radio_var1)
college_year_radiobutton_1.grid(row=6,column=1)

college_year_radiobutton_1=Radiobutton(frame1,value=3,text="III",variable=radio_var1)
college_year_radiobutton_1.grid(row=7,column=1)

college_year_radiobutton_1=Radiobutton(frame1,value=4,text="IV",variable=radio_var1)
college_year_radiobutton_1.grid(row=8,column=1)

#Programming Language and checkbutton
programming_language_label=Label(frame1,text="Programming Language")
programming_language_label.grid(row=5,column=2)

programming_language_checkbutton_1=Checkbutton(frame1,offvalue=0,onvalue=1,text="C",variable=check_var1)
programming_language_checkbutton_1.grid(row=5,column=3)

programming_language_checkbutton_2=Checkbutton(frame1,offvalue=0,onvalue=1,text="C++",variable=check_var2)
programming_language_checkbutton_2.grid(row=6,column=3)

programming_language_checkbutton_3=Checkbutton(frame1,offvalue=0,onvalue=1,text="java",variable=check_var3)
programming_language_checkbutton_3.grid(row=7,column=3)

programming_language_checkbutton_4=Checkbutton(frame1,offvalue=0,onvalue=1,text="python",variable=check_var4)
programming_language_checkbutton_4.grid(row=8,column=3)

#Display and Insert button
insert_button=Button(frame1,text="Insert",command=insert)
insert_button.grid(row=9,column=1,pady=10)

display_button=Button(frame1,text="Display",command=display)
display_button.grid(row=9,column=3,pady=10)


top.mainloop()



